from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cairos_session: Union[Unset, str] = UNSET,
    outseta_nocode_access_token: str,
) -> dict[str, Any]:
    cookies = {}
    if cairos_session is not UNSET:
        cookies["cairos_session"] = cairos_session

    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/session_id",
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[Union[HTTPValidationError, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cairos_session: Union[Unset, str] = UNSET,
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, str]]:
    """Get Session Id

     This id is used to differentiate sessions of the same user.
    It does not have an authentication role.

    Args:
        cairos_session (Union[Unset, str]):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        cairos_session=cairos_session,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cairos_session: Union[Unset, str] = UNSET,
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, str]]:
    """Get Session Id

     This id is used to differentiate sessions of the same user.
    It does not have an authentication role.

    Args:
        cairos_session (Union[Unset, str]):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return sync_detailed(
        client=client,
        cairos_session=cairos_session,
        outseta_nocode_access_token=outseta_nocode_access_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cairos_session: Union[Unset, str] = UNSET,
    outseta_nocode_access_token: str,
) -> Response[Union[HTTPValidationError, str]]:
    """Get Session Id

     This id is used to differentiate sessions of the same user.
    It does not have an authentication role.

    Args:
        cairos_session (Union[Unset, str]):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        cairos_session=cairos_session,
        outseta_nocode_access_token=outseta_nocode_access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cairos_session: Union[Unset, str] = UNSET,
    outseta_nocode_access_token: str,
) -> Optional[Union[HTTPValidationError, str]]:
    """Get Session Id

     This id is used to differentiate sessions of the same user.
    It does not have an authentication role.

    Args:
        cairos_session (Union[Unset, str]):
        outseta_nocode_access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            cairos_session=cairos_session,
            outseta_nocode_access_token=outseta_nocode_access_token,
        )
    ).parsed
