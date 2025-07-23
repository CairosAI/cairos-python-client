import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatThreadInList")


@_attrs_define
class ChatThreadInList:
    """This variant does not contain messages, it is for use in list operations.


    Attributes:
        id (str):
        user_id (str):
        created_at (datetime.datetime):
        nice_name (Union[Unset, str]):
    """

    id: str
    user_id: str
    created_at: datetime.datetime
    nice_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        nice_name = self.nice_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "created_at": created_at,
            }
        )
        if nice_name is not UNSET:
            field_dict["nice_name"] = nice_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        created_at = isoparse(d.pop("created_at"))

        nice_name = d.pop("nice_name", UNSET)

        chat_thread_in_list = cls(
            id=id,
            user_id=user_id,
            created_at=created_at,
            nice_name=nice_name,
        )

        chat_thread_in_list.additional_properties = d
        return chat_thread_in_list

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
