from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_login_outseta_login_post import BodyLoginOutsetaLoginPost
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BodyLoginOutsetaLoginPost,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/login",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

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
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyLoginOutsetaLoginPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Login Outseta

     Login via Outseta. Since users now login on the Outseta page, this endpoint is meant for clients
    other than the web app.
    Sends login data to Outseta, on successful return sets the cookie in the same way as Outseta.

    Args:
        body (BodyLoginOutsetaLoginPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyLoginOutsetaLoginPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Login Outseta

     Login via Outseta. Since users now login on the Outseta page, this endpoint is meant for clients
    other than the web app.
    Sends login data to Outseta, on successful return sets the cookie in the same way as Outseta.

    Args:
        body (BodyLoginOutsetaLoginPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyLoginOutsetaLoginPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Login Outseta

     Login via Outseta. Since users now login on the Outseta page, this endpoint is meant for clients
    other than the web app.
    Sends login data to Outseta, on successful return sets the cookie in the same way as Outseta.

    Args:
        body (BodyLoginOutsetaLoginPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyLoginOutsetaLoginPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Login Outseta

     Login via Outseta. Since users now login on the Outseta page, this endpoint is meant for clients
    other than the web app.
    Sends login data to Outseta, on successful return sets the cookie in the same way as Outseta.

    Args:
        body (BodyLoginOutsetaLoginPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
