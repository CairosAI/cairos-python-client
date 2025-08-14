from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_input import ChatInput
from ...models.chat_output import ChatOutput
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thread_id: str,
    *,
    body: ChatInput,
    outseta_nocode_access_token: str,
    cairos_session: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    cookies = {}
    cookies["Outseta.nocode.accessToken"] = outseta_nocode_access_token

    if cairos_session is not UNSET:
        cookies["cairos_session"] = cairos_session

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/thread/{thread_id}/nosequence",
        "cookies": cookies,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChatOutput, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ChatOutput.from_dict(response.json())

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
) -> Response[Union[ChatOutput, HTTPValidationError]]:
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
    body: ChatInput,
    outseta_nocode_access_token: str,
    cairos_session: Union[Unset, str] = UNSET,
) -> Response[Union[ChatOutput, HTTPValidationError]]:
    """Process Message Nosequence

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        cairos_session (Union[Unset, str]):
        body (ChatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatOutput, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatInput,
    outseta_nocode_access_token: str,
    cairos_session: Union[Unset, str] = UNSET,
) -> Optional[Union[ChatOutput, HTTPValidationError]]:
    """Process Message Nosequence

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        cairos_session (Union[Unset, str]):
        body (ChatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatOutput, HTTPValidationError]
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatInput,
    outseta_nocode_access_token: str,
    cairos_session: Union[Unset, str] = UNSET,
) -> Response[Union[ChatOutput, HTTPValidationError]]:
    """Process Message Nosequence

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        cairos_session (Union[Unset, str]):
        body (ChatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatOutput, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
        outseta_nocode_access_token=outseta_nocode_access_token,
        cairos_session=cairos_session,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatInput,
    outseta_nocode_access_token: str,
    cairos_session: Union[Unset, str] = UNSET,
) -> Optional[Union[ChatOutput, HTTPValidationError]]:
    """Process Message Nosequence

    Args:
        thread_id (str):
        outseta_nocode_access_token (str):
        cairos_session (Union[Unset, str]):
        body (ChatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatOutput, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            body=body,
            outseta_nocode_access_token=outseta_nocode_access_token,
            cairos_session=cairos_session,
        )
    ).parsed
