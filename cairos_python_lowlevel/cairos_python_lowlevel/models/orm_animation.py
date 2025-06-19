import datetime
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrmAnimation")


@_attrs_define
class OrmAnimation:
    """
    Attributes:
        job_thread (str):
        job_trigger (UUID):
        user_id (str):
        created_at (datetime.datetime):
        filepath_gltf (str):
        filepath_bgeo (str):
        avatar_id (Union[Unset, UUID]):
        avatar_user_id (Union[Unset, str]):
        nice_name (Union[Unset, str]):
    """

    job_thread: str
    job_trigger: UUID
    user_id: str
    created_at: datetime.datetime
    filepath_gltf: str
    filepath_bgeo: str
    avatar_id: Union[Unset, UUID] = UNSET
    avatar_user_id: Union[Unset, str] = UNSET
    nice_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_thread = self.job_thread

        job_trigger = str(self.job_trigger)

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        filepath_gltf = self.filepath_gltf

        filepath_bgeo = self.filepath_bgeo

        avatar_id: Union[Unset, str] = UNSET
        if not isinstance(self.avatar_id, Unset):
            avatar_id = str(self.avatar_id)

        avatar_user_id = self.avatar_user_id

        nice_name = self.nice_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_thread": job_thread,
                "job_trigger": job_trigger,
                "user_id": user_id,
                "created_at": created_at,
                "filepath_gltf": filepath_gltf,
                "filepath_bgeo": filepath_bgeo,
            }
        )
        if avatar_id is not UNSET:
            field_dict["avatar_id"] = avatar_id
        if avatar_user_id is not UNSET:
            field_dict["avatar_user_id"] = avatar_user_id
        if nice_name is not UNSET:
            field_dict["nice_name"] = nice_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_thread = d.pop("job_thread")

        job_trigger = UUID(d.pop("job_trigger"))

        user_id = d.pop("user_id")

        created_at = isoparse(d.pop("created_at"))

        filepath_gltf = d.pop("filepath_gltf")

        filepath_bgeo = d.pop("filepath_bgeo")

        _avatar_id = d.pop("avatar_id", UNSET)
        avatar_id: Union[Unset, UUID]
        if isinstance(_avatar_id, Unset):
            avatar_id = UNSET
        else:
            avatar_id = UUID(_avatar_id)

        avatar_user_id = d.pop("avatar_user_id", UNSET)

        nice_name = d.pop("nice_name", UNSET)

        orm_animation = cls(
            job_thread=job_thread,
            job_trigger=job_trigger,
            user_id=user_id,
            created_at=created_at,
            filepath_gltf=filepath_gltf,
            filepath_bgeo=filepath_bgeo,
            avatar_id=avatar_id,
            avatar_user_id=avatar_user_id,
            nice_name=nice_name,
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
