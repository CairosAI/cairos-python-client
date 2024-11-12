from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..fastapi_types import UNSET, Unset

T = TypeVar("T", bound="ChatOutput")


@_attrs_define
class ChatOutput:
    """
    Attributes:
        btl_objs (str):
        output (Union[Unset, Any]):
    """

    btl_objs: str
    output: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        btl_objs = self.btl_objs

        output = self.output

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btl_objs": btl_objs,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        btl_objs = d.pop("btl_objs")

        output = d.pop("output", UNSET)

        chat_output = cls(
            btl_objs=btl_objs,
            output=output,
        )

        chat_output.additional_properties = d
        return chat_output

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
