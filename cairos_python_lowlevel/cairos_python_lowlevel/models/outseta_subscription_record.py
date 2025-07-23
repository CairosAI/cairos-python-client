import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outseta_plan_record import OutsetaPlanRecord


T = TypeVar("T", bound="OutsetaSubscriptionRecord")


@_attrs_define
class OutsetaSubscriptionRecord:
    """
    Attributes:
        plan (OutsetaPlanRecord):
        uid (str):
        renewal_date (datetime.datetime):
        start_date (datetime.datetime):
        end_date (Union[Unset, datetime.datetime]):
    """

    plan: "OutsetaPlanRecord"
    uid: str
    renewal_date: datetime.datetime
    start_date: datetime.datetime
    end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.to_dict()

        uid = self.uid

        renewal_date = self.renewal_date.isoformat()

        start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Plan": plan,
                "Uid": uid,
                "RenewalDate": renewal_date,
                "StartDate": start_date,
            }
        )
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outseta_plan_record import OutsetaPlanRecord

        d = dict(src_dict)
        plan = OutsetaPlanRecord.from_dict(d.pop("Plan"))

        uid = d.pop("Uid")

        renewal_date = isoparse(d.pop("RenewalDate"))

        start_date = isoparse(d.pop("StartDate"))

        _end_date = d.pop("EndDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        outseta_subscription_record = cls(
            plan=plan,
            uid=uid,
            renewal_date=renewal_date,
            start_date=start_date,
            end_date=end_date,
        )

        outseta_subscription_record.additional_properties = d
        return outseta_subscription_record

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
