import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stored_message import StoredMessage


T = TypeVar("T", bound="ChatThreadPublic")


@_attrs_define
class ChatThreadPublic:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        messages (Union[Unset, list['StoredMessage']]):
        nice_name (Union[Unset, str]):
    """

    id: str
    created_at: datetime.datetime
    messages: Union[Unset, list["StoredMessage"]] = UNSET
    nice_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        nice_name = self.nice_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages
        if nice_name is not UNSET:
            field_dict["nice_name"] = nice_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stored_message import StoredMessage

        d = dict(src_dict)
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = StoredMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        nice_name = d.pop("nice_name", UNSET)

        chat_thread_public = cls(
            id=id,
            created_at=created_at,
            messages=messages,
            nice_name=nice_name,
        )

        chat_thread_public.additional_properties = d
        return chat_thread_public

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
