from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.orm_animation import OrmAnimation
from ...types import Response


def _get_kwargs(
    thread_id: str,
    trigger_msg_id: str,
    *,
    outseta_nocode_access_token: str,
) -> Dict[str, Any]:
    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/anim/{thread_id}/{trigger_msg_id}",
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, OrmAnimation]]:
    if response.status_code == 200:
        response_200 = OrmAnimation.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, OrmAnimation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    trigger_msg_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, OrmAnimation]]:
    """Get Anim

    Args:
        thread_id (str):
        trigger_msg_id (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, OrmAnimation]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg_id,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    trigger_msg_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, OrmAnimation]]:
    """Get Anim

    Args:
        thread_id (str):
        trigger_msg_id (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, OrmAnimation]
    """

    return sync_detailed(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg_id,
        client=client,
        outseta_nocode_access_token=outseta_nocode_access_token,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    trigger_msg_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, OrmAnimation]]:
    """Get Anim

    Args:
        thread_id (str):
        trigger_msg_id (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, OrmAnimation]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        trigger_msg_id=trigger_msg_id,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    trigger_msg_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, OrmAnimation]]:
    """Get Anim

    Args:
        thread_id (str):
        trigger_msg_id (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, OrmAnimation]
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            trigger_msg_id=trigger_msg_id,
            client=client,
            outseta_nocode_access_token=outseta_nocode_access_token,
        )
    ).parsed
