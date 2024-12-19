from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Motion")


@_attrs_define
class Motion:
    """
    Attributes:
        id (int):
        description (str):
        sg_file_animation (str):
        tags (List[Any]):
    """

    id: int
    description: str
    sg_file_animation: str
    tags: List[Any]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        description = self.description

        sg_file_animation = self.sg_file_animation

        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "sg_file_animation": sg_file_animation,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        description = d.pop("description")

        sg_file_animation = d.pop("sg_file_animation")

        tags = cast(List[Any], d.pop("tags"))

        motion = cls(
            id=id,
            description=description,
            sg_file_animation=sg_file_animation,
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
