from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_call_type import ToolCallType
from ..fastapi_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_call_args import ToolCallArgs


T = TypeVar("T", bound="ToolCall")


@_attrs_define
class ToolCall:
    """
    Attributes:
        name (str):
        args (ToolCallArgs):
        id (str):
        type (Union[Unset, ToolCallType]):
    """

    name: str
    args: "ToolCallArgs"
    id: str
    type: Union[Unset, ToolCallType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        args = self.args.to_dict()

        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "args": args,
                "id": id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tool_call_args import ToolCallArgs

        d = src_dict.copy()
        name = d.pop("name")

        args = ToolCallArgs.from_dict(d.pop("args"))

        id = d.pop("id")

        _type = d.pop("type", UNSET)
        type: Union[Unset, ToolCallType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ToolCallType(_type)

        tool_call = cls(
            name=name,
            args=args,
            id=id,
            type=type,
        )

        tool_call.additional_properties = d
        return tool_call

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
