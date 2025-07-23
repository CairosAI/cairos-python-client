from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_call_type import ToolCallType
from ..types import UNSET, Unset

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
        type_ (Union[Unset, ToolCallType]):
    """

    name: str
    args: "ToolCallArgs"
    id: str
    type_: Union[Unset, ToolCallType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        args = self.args.to_dict()

        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "args": args,
                "id": id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_call_args import ToolCallArgs

        d = dict(src_dict)
        name = d.pop("name")

        args = ToolCallArgs.from_dict(d.pop("args"))

        id = d.pop("id")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ToolCallType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ToolCallType(_type_)

        tool_call = cls(
            name=name,
            args=args,
            id=id,
            type_=type_,
        )

        tool_call.additional_properties = d
        return tool_call

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
