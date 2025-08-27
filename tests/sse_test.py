from typing import AsyncIterator
from cairos_python_lowlevel.cairos_python_lowlevel.client import Client, AuthenticatedClient
from cairos_python_lowlevel.cairos_python_lowlevel.models.orm_animation import OrmAnimation
from cairos_python_client.sse_listener import CairosSSEHandler, SSEMessageDef, CairosSSEMessages
import json

import pytest
import pytest_asyncio
import httpx
from starlette.requests import Request
from starlette.types import ASGIApp
from sse_starlette.sse import EventSourceResponse
from starlette.routing import Route
from starlette.applications import Starlette


@pytest.fixture
def app() -> ASGIApp:
    async def events(request: Request):
        async def event_source() -> AsyncIterator[dict]:
            yield {
                "event": "animation_success",
                "data": '{"job_trigger": "243bafdd-d97d-4a61-9d84-603645e7505f", "job_thread": "03ec84a4b1409a38e327bc16c3732e52", "user_id": "00000000", "filepath_bgeo": "/mothership3/projects/crs/global/output/sequences/03ec84a4b1409a38e327bc16c3732e52/243bafdd-d97d-4a61-9d84-603645e7505f.bgeo.sc", "filepath_gltf": "/mothership3/projects/crs/global/output/sequences/03ec84a4b1409a38e327bc16c3732e52/243bafdd-d97d-4a61-9d84-603645e7505f.glb", "created_at": "2025-08-19T15:24:19.124646+00:00"}'}

            yield {
                "event": "animation_error",
                "data": '{"detail": "Well that failed"}'}

            yield {
                "event": "unknown",
                "data": "into the unknown"}

        return EventSourceResponse(event_source())

    return Starlette(routes=[Route("/event_log", endpoint=events)])

@pytest_asyncio.fixture
async def base_client(app: ASGIApp) -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app)) as client:
        yield client

@pytest.mark.asyncio
async def test_handler(base_client: httpx.AsyncClient) -> None:
    cookies = {}
    url = "http://testserver/event_log"

    client = AuthenticatedClient(
        base_url=url,
        token=cookies.get("Outseta.nocode.accessToken", ""),
        verify_ssl=False,
        cookies=cookies,
        raise_on_unexpected_status=True)
    client.set_async_httpx_client(base_client)

    async def on_animation_success(_, animation):
        assert isinstance(animation, OrmAnimation)

    async def on_animation_error(_, error_msg):
        try:
            e = json.loads(error_msg)
            assert "detail" in e
        except:
            pytest.fail(error_msg)

    async def on_unknown_message(_, msg):
        print(msg)

    handler = CairosSSEHandler(
        client=client,
        url=url,
        error_on_unknown=False,
        unknown_handler=on_unknown_message)

    handler.register_message(SSEMessageDef(
        event=CairosSSEMessages.animation_success,
        response_model=OrmAnimation,
        callback=on_animation_success,
        parse_model=True))

    handler.register_message(SSEMessageDef(
        event=CairosSSEMessages.animation_error,
        response_model=None,
        callback=on_animation_error,
        parse_model=False))

    await handler.arun()
