from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_motd_motd_post import BodyCreateMotdMotdPost
from ...models.http_validation_error import HTTPValidationError
from ...models.motd import Motd
from ...types import Response


def _get_kwargs(
    *,
    body: BodyCreateMotdMotdPost,
    outseta_nocode_access_token: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/motd",
        "cookies": cookies,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Motd]]:
    if response.status_code == 202:
        response_202 = Motd.from_dict(response.json())

        return response_202
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Motd]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyCreateMotdMotdPost,
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, Motd]]:
    """Create Motd

    Args:
        outseta_nocode_access_token (str):
        body (BodyCreateMotdMotdPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Motd]]
    """

    kwargs = _get_kwargs(
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyCreateMotdMotdPost,
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, Motd]]:
    """Create Motd

    Args:
        outseta_nocode_access_token (str):
        body (BodyCreateMotdMotdPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Motd]
    """

    return sync_detailed(
        client=client,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyCreateMotdMotdPost,
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, Motd]]:
    """Create Motd

    Args:
        outseta_nocode_access_token (str):
        body (BodyCreateMotdMotdPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Motd]]
    """

    kwargs = _get_kwargs(
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyCreateMotdMotdPost,
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, Motd]]:
    """Create Motd

    Args:
        outseta_nocode_access_token (str):
        body (BodyCreateMotdMotdPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Motd]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            outseta_nocode_access_token=outseta_nocode_access_token,
        )
    ).parsed
