import pytest

import cairos_python_client
from cairos_python_lowlevel.cairos_python_lowlevel import AuthenticatedClient

@pytest.fixture
def user_data():
    return ("http://10.1.20.124:8000",
            "user1",
            "secretpass")

@pytest.fixture
def logged_in_client(user_data: tuple[str, str, str]):
    return cairos_python_client.login(*user_data)

def test_list_threads(logged_in_client: AuthenticatedClient):
    threads = cairos_python_client.list_threads(logged_in_client)
    print(threads)
    assert threads and len(threads) > 0
    assert threads[0].id is not None

def test_create_get_thread(logged_in_client: AuthenticatedClient):
    new_thread = cairos_python_client.create_thread(logged_in_client)
    thread = cairos_python_client.get_thread_by_id(new_thread.id, logged_in_client)
    print(f"Thread: {thread}")
    assert thread, "Thread not found"

def test_list_avatars(logged_in_client: AuthenticatedClient):
    avatars = cairos_python_client.list_avatars(logged_in_client)
    print(avatars)
    assert avatars and len(avatars) > 0

def test_motions_sequence(logged_in_client):
    prompt = "Hugging a pig"
    threads = cairos_python_client.list_threads(logged_in_client)
    assert threads and len(threads) > 0
    sequence = cairos_python_client.request_motions_sequence(
        prompt,
        threads[0].id,
        logged_in_client)

    assert sequence
