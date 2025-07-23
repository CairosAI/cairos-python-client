from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.outseta_person_account import OutsetaPersonAccount
    from ..models.outseta_subscription_record import OutsetaSubscriptionRecord


T = TypeVar("T", bound="OutsetaSubscriptionPlanUpdateRecord")


@_attrs_define
class OutsetaSubscriptionPlanUpdateRecord:
    """
    Attributes:
        person_account (list['OutsetaPersonAccount']):
        subscriptions (list['OutsetaSubscriptionRecord']):
        current_subscription (OutsetaSubscriptionRecord):
    """

    person_account: list["OutsetaPersonAccount"]
    subscriptions: list["OutsetaSubscriptionRecord"]
    current_subscription: "OutsetaSubscriptionRecord"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_account = []
        for person_account_item_data in self.person_account:
            person_account_item = person_account_item_data.to_dict()
            person_account.append(person_account_item)

        subscriptions = []
        for subscriptions_item_data in self.subscriptions:
            subscriptions_item = subscriptions_item_data.to_dict()
            subscriptions.append(subscriptions_item)

        current_subscription = self.current_subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PersonAccount": person_account,
                "Subscriptions": subscriptions,
                "CurrentSubscription": current_subscription,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outseta_person_account import OutsetaPersonAccount
        from ..models.outseta_subscription_record import OutsetaSubscriptionRecord

        d = dict(src_dict)
        person_account = []
        _person_account = d.pop("PersonAccount")
        for person_account_item_data in _person_account:
            person_account_item = OutsetaPersonAccount.from_dict(person_account_item_data)

            person_account.append(person_account_item)

        subscriptions = []
        _subscriptions = d.pop("Subscriptions")
        for subscriptions_item_data in _subscriptions:
            subscriptions_item = OutsetaSubscriptionRecord.from_dict(subscriptions_item_data)

            subscriptions.append(subscriptions_item)

        current_subscription = OutsetaSubscriptionRecord.from_dict(d.pop("CurrentSubscription"))

        outseta_subscription_plan_update_record = cls(
            person_account=person_account,
            subscriptions=subscriptions,
            current_subscription=current_subscription,
        )

        outseta_subscription_plan_update_record.additional_properties = d
        return outseta_subscription_plan_update_record

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
