from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.outseta_person_account import OutsetaPersonAccount


T = TypeVar("T", bound="OutsetaRegistrationRecord")


@_attrs_define
class OutsetaRegistrationRecord:
    """
    Attributes:
        person_account (List['OutsetaPersonAccount']):
    """

    person_account: List["OutsetaPersonAccount"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        person_account = []
        for person_account_item_data in self.person_account:
            person_account_item = person_account_item_data.to_dict()
            person_account.append(person_account_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PersonAccount": person_account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.outseta_person_account import OutsetaPersonAccount

        d = src_dict.copy()
        person_account = []
        _person_account = d.pop("PersonAccount")
        for person_account_item_data in _person_account:
            person_account_item = OutsetaPersonAccount.from_dict(person_account_item_data)

            person_account.append(person_account_item)

        outseta_registration_record = cls(
            person_account=person_account,
        )

        outseta_registration_record.additional_properties = d
        return outseta_registration_record

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
