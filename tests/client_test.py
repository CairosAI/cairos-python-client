from typing import Generator, Any
import pytest
import tempfile
from pathlib import Path
import cairos_python_client
from cairos_python_lowlevel.cairos_python_lowlevel import AuthenticatedClient
from cairos_python_lowlevel.cairos_python_lowlevel.models.avatar_public import AvatarPublic

@pytest.fixture
def user_data():
    return ("http://10.1.20.124:8000",
            "user1",
            "secretpass")

@pytest.fixture
def logged_in_client(user_data: tuple[str, str, str]):
    return cairos_python_client.login(*user_data)

@pytest.fixture
def avatar_path() -> Generator[Path, Any, Any]:
    with tempfile.NamedTemporaryFile(
            suffix=".fbx") as avatar_input:
        avatar_input.write(b'Kaydara FBX Binary  ')
        avatar_input.seek(0)
        yield Path(avatar_input.name)


@pytest.mark.dependency(name="test_create_get_thread")
def test_create_get_thread(logged_in_client: AuthenticatedClient):
    new_thread = cairos_python_client.create_thread(logged_in_client)
    thread = cairos_python_client.get_thread_by_id(new_thread.id, logged_in_client)
    print(f"----------\nThread: {thread}\n")
    assert thread, "Thread not found"

@pytest.mark.dependency(depends=["test_create_get_thread"])
def test_list_threads(logged_in_client: AuthenticatedClient):
    threads = cairos_python_client.list_threads(logged_in_client)
    print(f"----------\nThreads: {threads}\n")
    assert threads and len(threads) > 0, f"No threads found {threads}"
    assert threads[0].id is not None, f"Thread incorrect {threads[0]}"

@pytest.mark.dependency(name="test_create_avatar")
def test_create_avatar(
        logged_in_client: AuthenticatedClient):
    avatar = cairos_python_client.create_avatar(
        "Test label",
        client=logged_in_client)

    assert avatar, "Avatar was not created"

    return avatar

@pytest.mark.dependency(name="test_upload_avatar", depends=["test_create_avatar"])
def test_upload_avatar(
        logged_in_client: AuthenticatedClient,
        avatar_path: Path):
    avatars = cairos_python_client.list_avatars(client=logged_in_client)
    if len(avatars) > 0:
        avatar = avatars[0]
    else:
        raise ValueError("Avatars are empty")

    response = cairos_python_client.upload_avatar(
        uuid=avatar.id.hex,
        avatar_path=avatar_path,
        client=logged_in_client)
    print(f"----------\nAvatar upload: {response}\n")
    assert response, f"Avatar could not be uploaded {avatar_path}"
    assert isinstance(response, AvatarPublic), f"Avatar could not be uploaded {avatar_path}"

@pytest.mark.dependency(depends=["test_upload_avatar"])
def test_list_avatars(logged_in_client: AuthenticatedClient):
    avatars = cairos_python_client.list_avatars(logged_in_client)
    print(f"----------\nAvatars: {avatars}\n")
    assert avatars and len(avatars) > 0, "No avatars found"

@pytest.mark.dependency(depends=["test_create_get_thread", "test_upload_avatar"])
def test_motions_sequence(logged_in_client):
    prompt = "Knee warmup. Perform immediately, without prompting."
    threads = cairos_python_client.list_threads(logged_in_client)
    assert threads and len(threads) > 0
    sequence = cairos_python_client.request_motions_sequence(
        prompt=prompt,
        thread_id=threads[0].id,
        client=logged_in_client)

    assert sequence

@pytest.mark.dependency(depends=["test_upload_avatar"])
def test_delete_avatar(logged_in_client):
    avatar = cairos_python_client.list_avatars(logged_in_client)[-1]
    cairos_python_client.delete_avatar(
        avatar.id.hex,
        client=logged_in_client)
