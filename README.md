# Cairos python client

This is a realization of the Cairos OpenAPI spec as a Python library.

It allows logging in to, and using the Cairos API.

## Example

``` python
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_output import ChatOutput
from cairos_houdini_client import list_threads, request_motions_sequence, motions_from_chat_output
client = login("http://example.com:8000", "bob", "bobspassword")

threads: List[ChatThreadInList] = list_threads(client)
chat_output: ChatOutput = request_motions_sequence("Running on all fours", threads[0].id, client)
motions = motions_from_chat_output(chat_output)
```

## API
``` python
def login(url: str, user: str, password: str) -> AuthenticatedClient:
def send_chat(prompt: str, thread_id: str, client: AuthenticatedClient) -> ChatOutput:
def request_motions_sequence(prompt: str, thread_id: str, client: AuthenticatedClient) -> ChatOutput:
def list_threads(client: AuthenticatedClient) -> list[ChatThreadInList] | None:
def create_thread(client: AuthenticatedClient) -> ChatThreadPublic:
def get_thread_by_id(thread_id: str, client: AuthenticatedClient) -> ChatThreadPublic | HTTPValidationError | None:
def list_avatars(client: AuthenticatedClient) -> Sequence[AvatarMetadata]:
def get_avatar(uuid: str, client: AuthenticatedClient) -> bytes:
def motions_from_chat_output(chat_output: ChatOutput) -> Motions | None:
```

## Using the async functions
For the time being, the high-level interface only exposes synchronous functions.

It is possible to write analogous functions that use the low-level async functions instead.
Each module in the low-level client exposes a sync and async version of each method.

For instance:
``` python
from cairos_python_lowlevel.cairos_python_lowlevel.api.default import post_thread_thread_post
chat_output = await post_thread_thread_post.asyncio(
    "Running on all fours",
    threads[0].id,
    client)
```
See `cairos_python_lowlevel/README.md` for more information.

## Server-Sent Events

Cairos uses [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) as a mechanism for returning results from long-running processes. Most Cairos functionality involves long-running processes - animation sequencing, avatar rigging, etc.

For this reason, SSE is a crucial component of the API.

In addition to the OpenAPI-defined HTTP operations, this library includes a component for handling SSE - `CairosSSEHandler`. It provides both sync and async paths.

Here is an example, handling only `animation_success`. Client is the same as above, obtained by logging in.

``` python
from cairos_python_lowlevel.cairos_python_lowlevel.models.orm_animation import OrmAnimation
from cairos_python_lowlevel.cairos_python_lowlevel.api.default import export_anim_anim_thread_id_trigger_msg_id_export_post

url = f"{client._base_url}/event_log"

async def export_animation(client: AuthenticatedClient, thread_id: str, trigger_msg: UUID):
    """ Final result is received by sse, export_success or export_error.
    """
    await export_anim_anim_thread_id_trigger_msg_id_export_post.asyncio(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg.hex,
        client=client,
        outseta_nocode_access_token=client._cookies.get(cairos_python_client.token_cookie_name, ""),
        cairos_session=cairos_python_client.session_or_unset(client._cookies))

def on_animation_success(client: AuthenticatedClient, animation: OrmAnimation):
    print("Received sequencer success")
    # Now that animation is done, export it for retrieval
    await export_animation(client, animation.job_thread, animation.job_trigger)

async def test_handler(client: AuthenticatedClient):
    handler = CairosSSEHandler(
        client=client,
        url=url,
        error_on_unknown=True,
        unknown_handler=print)

    handler.register_message(SSEMessageDef(
        event=CairosSSEMessages.animation_success,
        response_model=OrmAnimation,
        callback=on_animation_success,
        parse_model=True))

    await handler.arun()

if __name__ == "__main__":
    import asyncio

    # Login, obtain client
    # ...

    asyncio.run(test_handler(client))
```
