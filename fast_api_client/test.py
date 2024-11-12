from fast_api_client.client import Client

from fast_api_client.api.default import login_auth_login_post as login_endpoint
from fast_api_client.api.default import get_threads_thread_get as list_threads
from fast_api_client.api.default import get_thread_thread_thread_id_get as get_thread
from fast_api_client.api.default import get_avatars_avatar_get as get_avatars
from fast_api_client.api.default import get_avatar_with_file_avatar_uuid_get as get_avatar_file

from fast_api_client.models.body_login_auth_login_post import BodyLoginAuthLoginPost

cl = Client(base_url="https://app.cairos.ai/api")
response = login_endpoint.sync_detailed(
    client=cl,
    body=BodyLoginAuthLoginPost(
        grant_type="password",
        username="user1",
        password="secretpass"))

print(response)
print(response.headers)

chat_threads = list_threads.sync_detailed(
    client=cl)

print("list threads")
print(chat_threads)
# print(get_thread.sync_detailed(thread_id=chat_threads.parsed.id, client=cl))
assert chat_threads.parsed
print("get thread")
thread = get_thread.sync_detailed(thread_id=chat_threads.parsed[0].id, client=cl).parsed
print(thread)

print("list avatars")
avatars = get_avatars.sync_detailed(client=cl).parsed
print(avatars)
print("get avatar")
print(cl.get_httpx_client().request(
    **get_avatar_file._get_kwargs(uuid=avatars[0].id)))
