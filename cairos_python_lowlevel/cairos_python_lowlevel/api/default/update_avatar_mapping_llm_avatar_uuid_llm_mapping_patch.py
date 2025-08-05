from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.avatar_public import AvatarPublic
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    outseta_nocode_access_token: str,
) -> dict[str, Any]:
    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/avatar/{uuid}/llm_mapping",
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = AvatarPublic.from_dict(response.json())

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
) -> Response[Union[AvatarPublic, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Response[Union[AvatarPublic, HTTPValidationError]]:
    """Update Avatar Mapping Llm

    Args:
        uuid (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvatarPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    """Update Avatar Mapping Llm

    Args:
        uuid (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvatarPublic, HTTPValidationError]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        outseta_nocode_access_token=outseta_nocode_access_token,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Response[Union[AvatarPublic, HTTPValidationError]]:
    """Update Avatar Mapping Llm

    Args:
        uuid (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvatarPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    """Update Avatar Mapping Llm

    Args:
        uuid (str):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvatarPublic, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            outseta_nocode_access_token=outseta_nocode_access_token,
        )
    ).parsed
