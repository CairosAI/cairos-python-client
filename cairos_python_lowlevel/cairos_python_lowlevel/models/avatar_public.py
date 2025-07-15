from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.avatar_status import AvatarStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AvatarPublic")


@_attrs_define
class AvatarPublic:
    """
    Attributes:
        id (UUID):
        user_id (str):
        label (str):
        status (Union[Unset, List[AvatarStatus]]):
    """

    id: UUID
    user_id: str
    label: str
    status: Union[Unset, List[AvatarStatus]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = str(self.id)

        user_id = self.user_id

        label = self.label

        status: Union[Unset, List[str]] = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "label": label,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        user_id = d.pop("user_id")

        label = d.pop("label")

        status = []
        _status = d.pop("status", UNSET)
        for status_item_data in _status or []:
            status_item = AvatarStatus(status_item_data)

            status.append(status_item)

        avatar_public = cls(
            id=id,
            user_id=user_id,
            label=label,
            status=status,
        )

        avatar_public.additional_properties = d
        return avatar_public

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
