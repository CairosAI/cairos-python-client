import datetime
from typing import Any, Dict, List, Type, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OrmAnimation")


@_attrs_define
class OrmAnimation:
    """
    Attributes:
        job_thread (str):
        job_trigger (UUID):
        avatar_id (UUID):
        avatar_user_id (int):
        created_at (datetime.datetime):
        filepath (str):
    """

    job_thread: str
    job_trigger: UUID
    avatar_id: UUID
    avatar_user_id: int
    created_at: datetime.datetime
    filepath: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_thread = self.job_thread

        job_trigger = str(self.job_trigger)

        avatar_id = str(self.avatar_id)

        avatar_user_id = self.avatar_user_id

        created_at = self.created_at.isoformat()

        filepath = self.filepath

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_thread": job_thread,
                "job_trigger": job_trigger,
                "avatar_id": avatar_id,
                "avatar_user_id": avatar_user_id,
                "created_at": created_at,
                "filepath": filepath,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_thread = d.pop("job_thread")

        job_trigger = UUID(d.pop("job_trigger"))

        avatar_id = UUID(d.pop("avatar_id"))

        avatar_user_id = d.pop("avatar_user_id")

        created_at = isoparse(d.pop("created_at"))

        filepath = d.pop("filepath")

        orm_animation = cls(
            job_thread=job_thread,
            job_trigger=job_trigger,
            avatar_id=avatar_id,
            avatar_user_id=avatar_user_id,
            created_at=created_at,
            filepath=filepath,
        )

        orm_animation.additional_properties = d
        return orm_animation

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
