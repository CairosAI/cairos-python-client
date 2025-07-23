import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Motion")


@_attrs_define
class Motion:
    """
    Attributes:
        sg_id (int):
        description (str):
        input_ (str):
        created_at (datetime.datetime):
        shot_description (str):
    """

    sg_id: int
    description: str
    input_: str
    created_at: datetime.datetime
    shot_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sg_id = self.sg_id

        description = self.description

        input_ = self.input_

        created_at = self.created_at.isoformat()

        shot_description = self.shot_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sg_id": sg_id,
                "description": description,
                "input": input_,
                "created_at": created_at,
                "shot_description": shot_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sg_id = d.pop("sg_id")

        description = d.pop("description")

        input_ = d.pop("input")

        created_at = isoparse(d.pop("created_at"))

        shot_description = d.pop("shot_description")

        motion = cls(
            sg_id=sg_id,
            description=description,
            input_=input_,
            created_at=created_at,
            shot_description=shot_description,
        )

        motion.additional_properties = d
        return motion

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
