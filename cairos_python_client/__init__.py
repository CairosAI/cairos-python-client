from typing import Sequence
from cairos_python_lowlevel.cairos_python_lowlevel.models.avatar_rebuilt import AvatarRebuilt
from cairos_types.core import Motions

from pathlib import Path
from cairos_python_lowlevel.cairos_python_lowlevel import AuthenticatedClient, Client
from cairos_python_lowlevel.cairos_python_lowlevel.api.default import (
    get_avatar_avatar_uuid_get,
    get_avatars_avatar_get,
    get_avatar_with_file_avatar_uuid_file_get,
    get_avatars_rebuilt_avatar_rebuilt_get,
    get_avatar_rebuilt_by_id_avatar_rebuilt_uuid_get,
    create_blank_avatar_avatar_new_label_post,
    get_session_id_session_id_get,
    post_avatar_avatar_uuid_upload_post,
    update_avatar_mapping_avatar_uuid_mapping_patch,
    process_message_thread_thread_id_post,
    process_message_nosequence_thread_thread_id_nosequence_post,
    get_threads_thread_get,
    login_outseta_login_post,
    new_thread_thread_post,
    get_thread_thread_thread_id_get,
    get_anim_file_anim_thread_id_trigger_msg_id_file_get,
    delete_avatar_route_avatar_uuid_delete)

from cairos_python_lowlevel.cairos_python_lowlevel.models.body_update_avatar_mapping_avatar_uuid_mapping_patch import BodyUpdateAvatarMappingAvatarUuidMappingPatch
from cairos_python_lowlevel.cairos_python_lowlevel.models.body_post_avatar_avatar_uuid_upload_post import BodyPostAvatarAvatarUuidUploadPost
from cairos_python_lowlevel.cairos_python_lowlevel.models.body_login_outseta_login_post import BodyLoginOutsetaLoginPost
from cairos_python_lowlevel.cairos_python_lowlevel.models.body_update_avatar_mapping_avatar_uuid_mapping_patch_mapping import BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping
from cairos_python_lowlevel.cairos_python_lowlevel.types import File, Unset, UNSET
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_output import ChatOutput
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_input import ChatInput
from cairos_python_lowlevel.cairos_python_lowlevel.models.http_validation_error import HTTPValidationError
from cairos_python_lowlevel.cairos_python_lowlevel.models.human_message import HumanMessage
from cairos_python_lowlevel.cairos_python_lowlevel.models.avatar_public import AvatarPublic
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_thread_public import ChatThreadPublic
from cairos_python_lowlevel.cairos_python_lowlevel.models.chat_thread_in_list import ChatThreadInList
from uuid import uuid4


token_cookie_name = "Outseta.nocode.accessToken"

def parse_cookies(cookies: str | None) -> dict[str, str]:
    if cookies is None:
        return {}

    return dict(map(
        lambda c: c.split(";")[0].strip().split("="),
        cookies.split(",")))

def request_session_id(client: AuthenticatedClient):
    sess = get_session_id_session_id_get.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))
    assert isinstance(sess, str)
    client._cookies["cairos_session"] = sess
    return client

def get_session(cookies) -> str:
    if "cairos_session" in cookies:
        return cookies.get("cairos_session")
    else:
        raise ValueError("Session id is required")

def motions_from_chat_output(chat_output: ChatOutput) -> Motions | None:
    artifact = next(
        (msg["artifact"] for msg in
         chat_output.messages
         if "artifact" in msg),
        None)
    if artifact:
        return Motions.parse_obj(artifact)
    else:
        return None

def login(url: str, user: str, password: str) -> AuthenticatedClient:
    unauth_client = Client(
        base_url=url,
        verify_ssl=False,
        raise_on_unexpected_status=True)

    response = login_outseta_login_post.sync_detailed(
        client=unauth_client,
        body=BodyLoginOutsetaLoginPost(
            username=user,
            password=password))

    print(f"response: {response}")
    cookies = parse_cookies(response.headers.get("Set-Cookie"))

    return AuthenticatedClient(
        base_url=url,
        token=cookies.get(token_cookie_name, ""),
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
            btl_objs=[]),
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))
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
            btl_objs=[]),
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))
    if isinstance(response, ChatOutput):
        return response
    else:
        raise Exception(str(response))

def list_threads(client: AuthenticatedClient) -> list[ChatThreadInList] | HTTPValidationError | None:
    return get_threads_thread_get.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def create_thread(client: AuthenticatedClient) -> ChatThreadPublic | HTTPValidationError:
    thread = new_thread_thread_post.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))
    assert thread is not None, "Thread should not be empty"
    return thread

def get_thread_by_id(thread_id: str, client: AuthenticatedClient) -> ChatThreadPublic | HTTPValidationError | None:
    return get_thread_thread_thread_id_get.sync(
        thread_id=thread_id,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def create_avatar(label: str, client: AuthenticatedClient) -> AvatarPublic | HTTPValidationError | None:
    return create_blank_avatar_avatar_new_label_post.sync(
        label=label,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))

def upload_avatar(uuid: str, avatar_path: Path, client: AuthenticatedClient) -> AvatarPublic | HTTPValidationError | None:
    with open(avatar_path, "rb") as f:
        return post_avatar_avatar_uuid_upload_post.sync(
            uuid=uuid,
            client=client,
            body=BodyPostAvatarAvatarUuidUploadPost(
                file=File(
                    payload=f,
                    file_name=f.name)),
            outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
            cairos_session=get_session(client._cookies))

def upload_avatar_mapping(uuid: str, mapping_path: Path, client: AuthenticatedClient) -> AvatarPublic | HTTPValidationError | None:
    with open(mapping_path, "rb") as f:
        return update_avatar_mapping_avatar_uuid_mapping_patch.sync(
            uuid=uuid,
            client=client,
            body=BodyUpdateAvatarMappingAvatarUuidMappingPatch(
                mapping_file=File(
                    payload=f,
                    file_name=f.name)),
            outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def set_avatar_mapping_preset(uuid: str, mapping: BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping, client: AuthenticatedClient) -> AvatarPublic | HTTPValidationError | None:
    return update_avatar_mapping_avatar_uuid_mapping_patch.sync(
        uuid=uuid,
        client=client,
        body=BodyUpdateAvatarMappingAvatarUuidMappingPatch(
            mapping=mapping),
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def list_avatars(client: AuthenticatedClient) -> Sequence[AvatarPublic] | HTTPValidationError:
    avatar_response = get_avatars_avatar_get.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""),
        cairos_session=get_session(client._cookies))

    if avatar_response:
        return avatar_response
    else:
        return []

def list_avatars_rebuilt(client: AuthenticatedClient) -> Sequence[AvatarRebuilt] | HTTPValidationError:
    avatar_response = get_avatars_rebuilt_avatar_rebuilt_get.sync(
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

    if avatar_response:
        return avatar_response
    else:
        return []

def get_avatar(uuid: str, client: AuthenticatedClient) -> AvatarPublic | HTTPValidationError | None:
    """ Return the avatar metadata.
    """
    return get_avatar_avatar_uuid_get.sync(
        uuid=uuid,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def get_avatar_file(uuid: str, client: AuthenticatedClient) -> bytes:
    """ Return the avatar metadata.
    """
    return get_avatar_with_file_avatar_uuid_file_get.sync_detailed(
        uuid=uuid,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, "")).content

def get_avatar_rebuilt(uuid: str, client: AuthenticatedClient) -> AvatarRebuilt | HTTPValidationError | None:
    return get_avatar_rebuilt_by_id_avatar_rebuilt_uuid_get.sync(
        uuid=uuid,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))

def delete_avatar(uuid: str, client: AuthenticatedClient) -> None:
    delete_avatar_route_avatar_uuid_delete.sync(
        uuid=uuid,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, ""))
    return None

def get_animation(thread_id: str, trigger_msg_id: str, client: AuthenticatedClient) -> bytes:
    """ Return animation as raw bytes. This is a gltf file.
    """
    return get_anim_file_anim_thread_id_trigger_msg_id_file_get.sync_detailed(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg_id,
        client=client,
        outseta_nocode_access_token=client._cookies.get(token_cookie_name, "")).content
