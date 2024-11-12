from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.motion import Motion


T = TypeVar("T", bound="Animation")


@_attrs_define
class Animation:
    """
    Attributes:
        sequence (List['Motion']):
        description (str):
    """

    sequence: List["Motion"]
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequence = []
        for sequence_item_data in self.sequence:
            sequence_item = sequence_item_data.to_dict()
            sequence.append(sequence_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequence": sequence,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.motion import Motion

        d = src_dict.copy()
        sequence = []
        _sequence = d.pop("sequence")
        for sequence_item_data in _sequence:
            sequence_item = Motion.from_dict(sequence_item_data)

            sequence.append(sequence_item)

        description = d.pop("description")

        animation = cls(
            sequence=sequence,
            description=description,
        )

        animation.additional_properties = d
        return animation

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
