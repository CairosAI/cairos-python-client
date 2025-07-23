from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.outseta_person import OutsetaPerson


T = TypeVar("T", bound="OutsetaPersonAccount")


@_attrs_define
class OutsetaPersonAccount:
    """
    Attributes:
        person (OutsetaPerson):
    """

    person: "OutsetaPerson"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person = self.person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Person": person,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outseta_person import OutsetaPerson

        d = dict(src_dict)
        person = OutsetaPerson.from_dict(d.pop("Person"))

        outseta_person_account = cls(
            person=person,
        )

        outseta_person_account.additional_properties = d
        return outseta_person_account

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
