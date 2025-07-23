from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_context import ChatContext
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    thread_id: str,
    *,
    body: ChatContext,
    outseta_nocode_access_token: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/oneshot/thread/{thread_id}",
        "cookies": cookies,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatContext,
    outseta_nocode_access_token: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Generate Thread Name From Context

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        body (ChatContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatContext,
    outseta_nocode_access_token: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Generate Thread Name From Context

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        body (ChatContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatContext,
    outseta_nocode_access_token: str,
) -> Response[Union[Any, HTTPValidationError]]:
    """Generate Thread Name From Context

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        body (ChatContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatContext,
    outseta_nocode_access_token: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Generate Thread Name From Context

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        body (ChatContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            body=body,
            outseta_nocode_access_token=outseta_nocode_access_token,
        )
    ).parsed
