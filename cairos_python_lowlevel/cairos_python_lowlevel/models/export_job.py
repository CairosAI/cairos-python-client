import datetime
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportJob")


@_attrs_define
class ExportJob:
    """
    Attributes:
        thread_id (str):
        trigger_msg (UUID):
        user_id (str):
        created_at (datetime.datetime):
        avatar_id (Union[Unset, UUID]):
        avatar_user_id (Union[Unset, str]):
    """

    thread_id: str
    trigger_msg: UUID
    user_id: str
    created_at: datetime.datetime
    avatar_id: Union[Unset, UUID] = UNSET
    avatar_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thread_id = self.thread_id

        trigger_msg = str(self.trigger_msg)

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        avatar_id: Union[Unset, str] = UNSET
        if not isinstance(self.avatar_id, Unset):
            avatar_id = str(self.avatar_id)

        avatar_user_id = self.avatar_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
                "trigger_msg": trigger_msg,
                "user_id": user_id,
                "created_at": created_at,
            }
        )
        if avatar_id is not UNSET:
            field_dict["avatar_id"] = avatar_id
        if avatar_user_id is not UNSET:
            field_dict["avatar_user_id"] = avatar_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thread_id = d.pop("thread_id")

        trigger_msg = UUID(d.pop("trigger_msg"))

        user_id = d.pop("user_id")

        created_at = isoparse(d.pop("created_at"))

        _avatar_id = d.pop("avatar_id", UNSET)
        avatar_id: Union[Unset, UUID]
        if isinstance(_avatar_id, Unset):
            avatar_id = UNSET
        else:
            avatar_id = UUID(_avatar_id)

        avatar_user_id = d.pop("avatar_user_id", UNSET)

        export_job = cls(
            thread_id=thread_id,
            trigger_msg=trigger_msg,
            user_id=user_id,
            created_at=created_at,
            avatar_id=avatar_id,
            avatar_user_id=avatar_user_id,
        )

        export_job.additional_properties = d
        return export_job

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
