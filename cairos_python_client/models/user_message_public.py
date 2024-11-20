import datetime
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_message_public_role import UserMessagePublicRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMessagePublic")


@_attrs_define
class UserMessagePublic:
    """
    Attributes:
        id (UUID):
        session_id (str):
        content (str):
        created_at (datetime.datetime):
        role (Union[Unset, UserMessagePublicRole]):  Default: UserMessagePublicRole.HUMAN.
    """

    id: UUID
    session_id: str
    content: str
    created_at: datetime.datetime
    role: Union[Unset, UserMessagePublicRole] = UserMessagePublicRole.HUMAN
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = str(self.id)

        session_id = self.session_id

        content = self.content

        created_at = self.created_at.isoformat()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "content": content,
                "created_at": created_at,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        session_id = d.pop("session_id")

        content = d.pop("content")

        created_at = isoparse(d.pop("created_at"))

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserMessagePublicRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserMessagePublicRole(_role)

        user_message_public = cls(
            id=id,
            session_id=session_id,
            content=content,
            created_at=created_at,
            role=role,
        )

        user_message_public.additional_properties = d
        return user_message_public

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
