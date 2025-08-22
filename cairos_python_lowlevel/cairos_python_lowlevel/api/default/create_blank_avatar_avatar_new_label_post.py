from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.avatar_public import AvatarPublic
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    label: str,
    *,
    outseta_nocode_access_token: str,
    cairos_session: str,
) -> dict[str, Any]:
    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    cookies["cairos_session"] = cairos_session

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/avatar/new/{label}",
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    if response.status_code == 201:
        response_201 = AvatarPublic.from_dict(response.json())

        return response_201
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
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
    cairos_session: str,
) -> Response[Union[AvatarPublic, HTTPValidationError]]:
    """Create Blank Avatar

    Args:
        label (str):
        outseta_nocode_access_token (str):
        cairos_session (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvatarPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        label=label,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
    cairos_session: str,
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    """Create Blank Avatar

    Args:
        label (str):
        outseta_nocode_access_token (str):
        cairos_session (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvatarPublic, HTTPValidationError]
    """

    return sync_detailed(
        label=label,
        client=client,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    ).parsed


async def asyncio_detailed(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
    cairos_session: str,
) -> Response[Union[AvatarPublic, HTTPValidationError]]:
    """Create Blank Avatar

    Args:
        label (str):
        outseta_nocode_access_token (str):
        cairos_session (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvatarPublic, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        label=label,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    outseta_nocode_access_token: str,
    cairos_session: str,
) -> Optional[Union[AvatarPublic, HTTPValidationError]]:
    """Create Blank Avatar

    Args:
        label (str):
        outseta_nocode_access_token (str):
        cairos_session (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AvatarPublic, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            label=label,
            client=client,
            outseta_nocode_access_token=outseta_nocode_access_token,
            cairos_session=cairos_session,
        )
    ).parsed
