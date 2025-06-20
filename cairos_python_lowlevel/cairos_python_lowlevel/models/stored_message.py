from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stored_message_type import StoredMessageType

if TYPE_CHECKING:
    from ..models.ai_message import AIMessage
    from ..models.human_message import HumanMessage
    from ..models.system_message import SystemMessage
    from ..models.tool_message import ToolMessage


T = TypeVar("T", bound="StoredMessage")


@_attrs_define
class StoredMessage:
    """
    Attributes:
        type (StoredMessageType):
        data (Union['AIMessage', 'HumanMessage', 'SystemMessage', 'ToolMessage']):
    """

    type: StoredMessageType
    data: Union["AIMessage", "HumanMessage", "SystemMessage", "ToolMessage"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ai_message import AIMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage

        type = self.type.value

        data: Dict[str, Any]
        if isinstance(self.data, HumanMessage):
            data = self.data.to_dict()
        elif isinstance(self.data, AIMessage):
            data = self.data.to_dict()
        elif isinstance(self.data, SystemMessage):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_message import AIMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_message import ToolMessage

        d = src_dict.copy()
        type = StoredMessageType(d.pop("type"))

        def _parse_data(data: object) -> Union["AIMessage", "HumanMessage", "SystemMessage", "ToolMessage"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HumanMessage.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = AIMessage.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = SystemMessage.from_dict(data)

                return data_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_3 = ToolMessage.from_dict(data)

            return data_type_3

        data = _parse_data(d.pop("data"))

        stored_message = cls(
            type=type,
            data=data,
        )

        stored_message.additional_properties = d
        return stored_message

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
