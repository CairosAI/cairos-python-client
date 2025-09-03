""" Example of creating and downloading an animation using cairos.ai
"""
import shutil
from pathlib import Path
import asyncio

from cairos_python_client import AuthenticatedClient, create_thread, token_cookie_name, get_session, login

from cairos_python_lowlevel.cairos_python_lowlevel.models.human_message import HumanMessage
from cairos_python_lowlevel.cairos_python_lowlevel.models.orm_animation import OrmAnimation
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_input import ChatInput
from cairos_python_lowlevel.cairos_python_lowlevel.models.export import Export

from cairos_python_lowlevel.cairos_python_lowlevel.api.default import (
    get_session_id_session_id_get,
    process_message_thread_thread_id_post,
    export_anim_anim_thread_id_trigger_msg_id_export_post)

from cairos_python_client.sse_listener import CairosSSEHandler, SSEMessageDef, CairosSSEMessages
from uuid import UUID, uuid4


async def export_animation(client: AuthenticatedClient, thread_id: str, trigger_msg: UUID):
    """ Request an animation export, which will convert the animation to a format for final use.
    Final result is received by sse, export_success or export_error.
    """
    await export_anim_anim_thread_id_trigger_msg_id_export_post.asyncio(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg.hex,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))

async def request_animation(client: AuthenticatedClient, thread_id: str, prompt_message: str):
    """ Request an animation by sending chat prompt.
    """
    await process_message_thread_thread_id_post.asyncio(
        thread_id=thread_id,
        client=client,
        body=ChatInput(
            prompt=HumanMessage(
                content=prompt_message,
                id=uuid4().hex),
            history=[],
            btl_objs=[]),
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))

async def on_animation_success(client: AuthenticatedClient, animation: OrmAnimation):
    print("Received sequencer success, exporting")
    await export_animation(client, animation.job_thread, animation.job_trigger)

async def download_export(client: AuthenticatedClient, export: Export):
    """ Request to the download endpoint, save the resulting file and unpack it.
    """
    temp_dir = Path("/tmp/cairos_example")
    temp_dir.mkdir(parents=True, exist_ok=True)

    # The export is a zip file. Use the extension of the returned file.
    filename = temp_dir.joinpath(f"{export.job_thread}_{export.job_trigger}")\
                       .with_suffix(Path(export.filepath).suffix)

    # Download the actual file and write it to filesystem
    result = await client.get_async_httpx_client().get(
        url=f"{client._base_url}/anim/{export.job_thread}/{export.job_trigger.hex}/download")

    with open(filename, "wb") as f:
        f.write(result.content)

    shutil.unpack_archive(filename, temp_dir.joinpath("extracted"))
    print(f"Successfully downloaded animation: {filename}\nExtracted to {temp_dir}")

async def on_export_success(client: AuthenticatedClient, export: Export):
    print("Received export success, downloading")
    await download_export(client, export)

async def on_unknown(client, msg):
    print(msg)

async def create_and_run_handler(client: AuthenticatedClient):
    url = f"{client._base_url}/event_log"

    handler = CairosSSEHandler(
        client=client,
        url=url,
        error_on_unknown=False,
        unknown_handler=on_unknown)

    handler.register_message(SSEMessageDef(
        event=CairosSSEMessages.animation_success,
        response_model=OrmAnimation,
        callback=on_animation_success,
        parse_model=True))

    handler.register_message(SSEMessageDef(
        event=CairosSSEMessages.export_success,
        response_model=Export,
        callback=on_export_success,
        parse_model=True))

    await handler.arun()

async def main(client, thread):
    await asyncio.gather(
        create_and_run_handler(client),
        request_animation(
            client,
            thread.id,
            "Pretend to be a mime"))

if __name__ == "__main__":
    client = login(
        url="https://app.cairos.ai/api",
        user="bob",
        password="bobspass")

    # Request a sesssion id for SSE
    sess_id = get_session_id_session_id_get.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(
            token_cookie_name, ""))
    client._cookies["cairos_session"] = sess_id

    # The handler runs in a separate task, not to block the rest of the program.
    thread = create_thread(client)
    asyncio.run(main(client, thread))
