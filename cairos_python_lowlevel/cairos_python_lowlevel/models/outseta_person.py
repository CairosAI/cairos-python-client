import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OutsetaPerson")


@_attrs_define
class OutsetaPerson:
    """
    Attributes:
        email (str):
        full_name (str):
        uid (str):
        created (datetime.datetime):
    """

    email: str
    full_name: str
    uid: str
    created: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        full_name = self.full_name

        uid = self.uid

        created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Email": email,
                "FullName": full_name,
                "Uid": uid,
                "Created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("Email")

        full_name = d.pop("FullName")

        uid = d.pop("Uid")

        created = isoparse(d.pop("Created"))

        outseta_person = cls(
            email=email,
            full_name=full_name,
            uid=uid,
            created=created,
        )

        outseta_person.additional_properties = d
        return outseta_person

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
