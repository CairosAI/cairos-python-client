from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invalid_tool_call_type import InvalidToolCallType
from //fastapi_types import UNSET, Unset

T = TypeVar("T", bound="InvalidToolCall")


@_attrs_define
class InvalidToolCall:
    """
    Attributes:
        name (str):
        args (str):
        id (str):
        error (str):
        type (Union[Unset, InvalidToolCallType]):
    """

    name: str
    args: str
    id: str
    error: str
    type: Union[Unset, InvalidToolCallType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        args = self.args

        id = self.id

        error = self.error

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
                "error": error,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        args = d.pop("args")

        id = d.pop("id")

        error = d.pop("error")

        _type = d.pop("type", UNSET)
        type: Union[Unset, InvalidToolCallType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InvalidToolCallType(_type)

        invalid_tool_call = cls(
            name=name,
            args=args,
            id=id,
            error=error,
            type=type,
        )

        invalid_tool_call.additional_properties = d
        return invalid_tool_call

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
