from typing import Sequence
from cairos_types.core import Motions
import json
from cairos_python_lowlevel.cairos_python_lowlevel import AuthenticatedClient, Client
from cairos_python_lowlevel.cairos_python_lowlevel.api.default import (
    get_avatar_with_file_avatar_uuid_get,
    get_avatars_avatar_get,
    login_auth_login_post,
    process_message_thread_thread_id_post,
    process_message_nosequence_thread_thread_id_nosequence_post,
    get_threads_thread_get,
    post_thread_thread_post,
    get_thread_thread_thread_id_get)

from cairos_python_lowlevel.cairos_python_lowlevel.models import BodyLoginAuthLoginPost
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_output import ChatOutput
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_input import ChatInput
from cairos_python_lowlevel.cairos_python_lowlevel.models.http_validation_error import HTTPValidationError
from cairos_python_lowlevel.cairos_python_lowlevel.models.human_message import HumanMessage
from cairos_python_lowlevel.cairos_python_lowlevel.models.avatar_metadata import AvatarMetadata
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_thread_public import ChatThreadPublic
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_thread_in_list import ChatThreadInList
from uuid import uuid4

def parse_cookies(cookies: str | None) -> dict[str, str]:
    if cookies is None:
        return {}

    return dict(map(
        lambda c: c.split(";")[0].strip().split("="),
        cookies.split(",")))

def motions_from_chat_output(chat_output: ChatOutput) -> Motions | None:
    return Motions(**json.loads(chat_output.btl_objs).get('motions'))

def login(url: str, user: str, password: str) -> AuthenticatedClient:
    unauth_client = Client(
        base_url=url,
        verify_ssl=False,
        raise_on_unexpected_status=True)

    response = login_auth_login_post.sync_detailed(
        client=unauth_client,
        body=BodyLoginAuthLoginPost(
            grant_type="password",
            username=user,
            password=password))

    print(f"response: {response}")
    cookies = parse_cookies(response.headers.get("Set-Cookie"))
    return AuthenticatedClient(
        base_url=url,
        token=cookies.get("id", ""),
        verify_ssl=False,
        cookies=cookies)

def send_chat(prompt: str, thread_id: str, client: AuthenticatedClient) -> ChatOutput:
    """ Send a prompt to AI, receive structured output, containing animations, etc.
    """
    response = process_message_thread_thread_id_post.sync(
            thread_id=thread_id,
            client=client,
            body=ChatInput(
                prompt=HumanMessage(content=prompt, id=uuid4().hex),
                history=[],
                avatar=AvatarMetadata(id=uuid4(), label="Test", thumbnail=None),
                btl_objs=[]))
    if isinstance(response, ChatOutput):
        return response
    else:
        raise Exception(str(response))

def request_motions_sequence(prompt: str, thread_id: str, client: AuthenticatedClient) -> ChatOutput:
    """ Similar to send_chat, but does not trigger a sequencing job.
    Useful for when you only want to retrieve the list of motions.
    """
    response = process_message_nosequence_thread_thread_id_nosequence_post.sync(
        thread_id=thread_id,
        client=client,
        body=ChatInput(
            prompt=HumanMessage(content=prompt, id=uuid4().hex),
            history=[],
            avatar=AvatarMetadata(id=uuid4(), label="Test", thumbnail=None),
            btl_objs=[]))
    if isinstance(response, ChatOutput):
        return response
    else:
        raise Exception(str(response))

def list_threads(client: AuthenticatedClient) -> list[ChatThreadInList] | None:
    return get_threads_thread_get.sync(client=client)

def create_thread(client: AuthenticatedClient) -> ChatThreadPublic:
    thread = (post_thread_thread_post.sync(client=client))
    assert thread is not None, "Thread should not be empty"
    return thread

def get_thread_by_id(thread_id: str, client: AuthenticatedClient) -> ChatThreadPublic | HTTPValidationError | None:
    return get_thread_thread_thread_id_get.sync(
        thread_id=thread_id,
        client=client)

def list_avatars(client: AuthenticatedClient) -> Sequence[AvatarMetadata]:
    avatar_response = get_avatars_avatar_get.sync(client=client)
    if avatar_response:
        return list(map(
            lambda a: AvatarMetadata(**a.to_dict()),
            avatar_response))
    else:
        return []

def get_avatar(uuid: str, client: AuthenticatedClient) -> bytes:
    """ Return the avatar file as bytes.
    """
    return get_avatar_with_file_avatar_uuid_get.sync_detailed(uuid=uuid, client=client).content
