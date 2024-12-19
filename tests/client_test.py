import pytest

import cairos_python_client

@pytest.fixture
def user_data():
    return ("http://10.1.20.124:8000",
            "user1",
            "secretpass")

@pytest.fixture
def logged_in_client(user_data: tuple[str, str, str]):
    return cairos_python_client.login(*user_data)

def test_list_threads(logged_in_client: cairos_python_client.AuthenticatedClient):
    threads = cairos_python_client.list_threads(logged_in_client)
    print(threads)
    assert threads and len(threads) > 0
    assert threads[0].id is not None
