from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_post_avatar_avatar_new_label_post import BodyPostAvatarAvatarNewLabelPost
from ...models.http_validation_error import HTTPValidationError
from ...fastapi_types import Response


def _get_kwargs(
    label: str,
    *,
    body: BodyPostAvatarAvatarNewLabelPost,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/avatar/new/{label}",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 202:
        response_202 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
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
    body: BodyPostAvatarAvatarNewLabelPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Post Avatar

    Args:
        label (str):
        body (BodyPostAvatarAvatarNewLabelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        label=label,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyPostAvatarAvatarNewLabelPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Post Avatar

    Args:
        label (str):
        body (BodyPostAvatarAvatarNewLabelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        label=label,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyPostAvatarAvatarNewLabelPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Post Avatar

    Args:
        label (str):
        body (BodyPostAvatarAvatarNewLabelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        label=label,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyPostAvatarAvatarNewLabelPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Post Avatar

    Args:
        label (str):
        body (BodyPostAvatarAvatarNewLabelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            label=label,
            client=client,
            body=body,
        )
    ).parsed
