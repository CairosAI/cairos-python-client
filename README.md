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
```
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

It is possible to write analogous functions, that use the low-level async functions instead.
Each module in the low-level client exposes a sync and async version of each method.

For instance:
```
from cairos_python_lowlevel.cairos_python_lowlevel.api.default import post_thread_thread_post
chat_output = await post_thread_thread_post.async("Running on all fours", threads[0].id, client)
```
See `cairos_python_lowlevel/README.md` for more information.
