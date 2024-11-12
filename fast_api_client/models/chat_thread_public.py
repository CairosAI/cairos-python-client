import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..fastapi_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_message_public import AIMessagePublic
    from ..models.user_message_public import UserMessagePublic


T = TypeVar("T", bound="ChatThreadPublic")


@_attrs_define
class ChatThreadPublic:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        messages (Union[Unset, List[Union['AIMessagePublic', 'UserMessagePublic']]]):
    """

    id: str
    created_at: datetime.datetime
    messages: Union[Unset, List[Union["AIMessagePublic", "UserMessagePublic"]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_message_public import UserMessagePublic

        id = self.id

        created_at = self.created_at.isoformat()

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: Dict[str, Any]
                if isinstance(messages_item_data, UserMessagePublic):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_message_public import AIMessagePublic
        from ..models.user_message_public import UserMessagePublic

        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(data: object) -> Union["AIMessagePublic", "UserMessagePublic"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = UserMessagePublic.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_1 = AIMessagePublic.from_dict(data)

                return messages_item_type_1

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        chat_thread_public = cls(
            id=id,
            created_at=created_at,
            messages=messages,
        )

        chat_thread_public.additional_properties = d
        return chat_thread_public

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
