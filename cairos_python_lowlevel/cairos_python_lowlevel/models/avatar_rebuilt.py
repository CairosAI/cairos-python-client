import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AvatarRebuilt")


@_attrs_define
class AvatarRebuilt:
    """
    Attributes:
        id (UUID):
        user_id (str):
        created_at (datetime.datetime):
        label (str):
        filepath (str):
    """

    id: UUID
    user_id: str
    created_at: datetime.datetime
    label: str
    filepath: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        label = self.label

        filepath = self.filepath

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "created_at": created_at,
                "label": label,
                "filepath": filepath,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = d.pop("user_id")

        created_at = isoparse(d.pop("created_at"))

        label = d.pop("label")

        filepath = d.pop("filepath")

        avatar_rebuilt = cls(
            id=id,
            user_id=user_id,
            created_at=created_at,
            label=label,
            filepath=filepath,
        )

        avatar_rebuilt.additional_properties = d
        return avatar_rebuilt

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
