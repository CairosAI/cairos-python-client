from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyLoginOutsetaLoginPost")


@_attrs_define
class BodyLoginOutsetaLoginPost:
    """
    Attributes:
        username (str):
        password (str):
        grant_type (Union[Unset, str]):
        scope (Union[Unset, str]):  Default: ''.
        client_id (Union[Unset, str]):
        client_secret (Union[Unset, str]):
    """

    username: str
    password: str
    grant_type: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = ""
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        password = self.password

        grant_type = self.grant_type

        scope = self.scope

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        grant_type = d.pop("grant_type", UNSET)

        scope = d.pop("scope", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        body_login_outseta_login_post = cls(
            username=username,
            password=password,
            grant_type=grant_type,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )

        body_login_outseta_login_post.additional_properties = d
        return body_login_outseta_login_post

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
