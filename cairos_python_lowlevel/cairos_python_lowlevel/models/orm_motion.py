import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OrmMotion")


@_attrs_define
class OrmMotion:
    """
    Attributes:
        sg_id (int):
        name (str):
        description (str):
        input_file (str):
        shot_description (str):
        created_at (datetime.datetime):
    """

    sg_id: int
    name: str
    description: str
    input_file: str
    shot_description: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sg_id = self.sg_id

        name = self.name

        description = self.description

        input_file = self.input_file

        shot_description = self.shot_description

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sg_id": sg_id,
                "name": name,
                "description": description,
                "input_file": input_file,
                "shot_description": shot_description,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sg_id = d.pop("sg_id")

        name = d.pop("name")

        description = d.pop("description")

        input_file = d.pop("input_file")

        shot_description = d.pop("shot_description")

        created_at = isoparse(d.pop("created_at"))

        orm_motion = cls(
            sg_id=sg_id,
            name=name,
            description=description,
            input_file=input_file,
            shot_description=shot_description,
            created_at=created_at,
        )

        orm_motion.additional_properties = d
        return orm_motion

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
