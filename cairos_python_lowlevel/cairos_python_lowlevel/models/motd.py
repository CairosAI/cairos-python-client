import datetime
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Motd")


@_attrs_define
class Motd:
    """
    Attributes:
        id (UUID):
        message (str):
        user_id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
    """

    id: UUID
    message: str
    user_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = str(self.id)

        message = self.message

        user_id = self.user_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "message": message,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        message = d.pop("message")

        user_id = d.pop("user_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        motd = cls(
            id=id,
            message=message,
            user_id=user_id,
            created_at=created_at,
        )

        motd.additional_properties = d
        return motd

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
