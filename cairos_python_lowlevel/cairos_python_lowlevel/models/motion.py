from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Motion")


@_attrs_define
class Motion:
    """
    Attributes:
        sg_id (int):
        description (str):
        input_ (str):
        tags (List[Any]):
    """

    sg_id: int
    description: str
    input_: str
    tags: List[Any]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sg_id = self.sg_id

        description = self.description

        input_ = self.input_

        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sg_id": sg_id,
                "description": description,
                "input": input_,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sg_id = d.pop("sg_id")

        description = d.pop("description")

        input_ = d.pop("input")

        tags = cast(List[Any], d.pop("tags"))

        motion = cls(
            sg_id=sg_id,
            description=description,
            input_=input_,
            tags=tags,
        )

        motion.additional_properties = d
        return motion

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
