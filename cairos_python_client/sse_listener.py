from enum import Enum

from dataclasses import dataclass
from cairos_python_lowlevel.cairos_python_lowlevel.client import Client, AuthenticatedClient
from cairos_python_lowlevel.cairos_python_lowlevel.models.orm_animation import OrmAnimation

from typing import Callable, Protocol, TypeVar, ClassVar, Type, Generic
import json

import httpx_sse

_R = TypeVar('_R')
class CairosSSEResponseModel(Protocol):
    @classmethod
    def from_dict(cls: Type[_R], src_dict: dict) -> _R:
        ...

class CairosSSEMessages(Enum):
    animation_success = "animation_success"
    animation_error = "animation_error"
    export_success = "export_success"
    export_error = "export_error"
    avatar_upload_success = "avatar_upload_success"
    avatar_upload_err = "avatar_upload_err"
    avatar_autorig_success = "avatar_autorig_success"
    avatar_autorig_err = "avatar_autorig_err"
    avatar_mapping_success = "avatar_mapping_success"
    avatar_mapping_err = "avatar_mapping_err"
    avatar_export_success = "avatar_export_success"
    avatar_export_error = "avatar_export_error"
    animation_retarget_success = "animation_retarget_success"
    animation_retarget_err = "animation_retarget_err"
    usage_report = "usage_report"


@dataclass
class SSEMessageDef(Generic[_R]):
    event: CairosSSEMessages
    response_model: Type[_R] | None
    callback: Callable
    parse_model: bool


class UnknownSSEMessage(Exception):
    pass


class CairosSSEHandler():
    def __init__(self,
                 client: AuthenticatedClient,
                 url: str,
                 error_on_unknown: bool = True,
                 unknown_handler: Callable | None = None
                 ):
        self._client = client
        self._url = url
        self._error_on_unknown = error_on_unknown
        self._registered_messages: dict[str, SSEMessageDef[CairosSSEResponseModel]] = {}
        self._unknown_handler = unknown_handler

    def register_message(self, msg: SSEMessageDef[CairosSSEResponseModel]):
        self._registered_messages[msg.event.value] = msg

    def run(self):
        with httpx_sse.connect_sse(
                client=self._client.get_httpx_client(),
                method="GET",
                url=self._url) as event_source:
            session_id = event_source.response.cookies.get("cairos_session")
            if session_id:
                self._client._cookies["cairos_session"] = session_id

            sse_iter = event_source.iter_sse()
            for evt in sse_iter:
                if self._client.get_async_httpx_client().is_closed:
                    break

                if evt.event in self._registered_messages:
                    msg = self._registered_messages[evt.event]
                    if msg.parse_model and msg.response_model:
                        msg.callback(
                            self._client,
                            msg.response_model.from_dict(json.loads(evt.data)))
                    else:
                        msg.callback(self._client, evt.data)
                elif self._error_on_unknown:
                    raise UnknownSSEMessage(evt.data)

    async def arun(self):
        async with httpx_sse.aconnect_sse(
                client=self._client.get_async_httpx_client(),
                method="GET",
                url=self._url) as event_source:
            # save session cookie
            session_id = event_source.response.cookies.get("cairos_session")
            if session_id:
                self._client._cookies["cairos_session"] = session_id

            sse_iter = event_source.aiter_sse()
            async for evt in sse_iter:
                if self._client.get_async_httpx_client().is_closed:
                    break

                if evt.event in self._registered_messages:
                    msg = self._registered_messages[evt.event]
                    if msg.parse_model and msg.response_model:
                        await msg.callback(
                            self._client,
                            msg.response_model.from_dict(json.loads(evt.data)))
                    else:
                        await msg.callback(self._client, evt.data)
                elif self._error_on_unknown:
                    raise UnknownSSEMessage(evt.data)
                elif self._unknown_handler:
                    await self._unknown_handler(self._client, evt.data)
