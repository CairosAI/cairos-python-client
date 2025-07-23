from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.body_update_avatar_mapping_avatar_uuid_mapping_patch_mapping import (
    BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping,
)
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyUpdateAvatarMappingAvatarUuidMappingPatch")


@_attrs_define
class BodyUpdateAvatarMappingAvatarUuidMappingPatch:
    """
    Attributes:
        mapping (Union[Unset, BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping]):
        mapping_file (Union[Unset, File]):
    """

    mapping: Union[Unset, BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping] = UNSET
    mapping_file: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapping: Union[Unset, str] = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = self.mapping.value

        mapping_file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.mapping_file, Unset):
            mapping_file = self.mapping_file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if mapping_file is not UNSET:
            field_dict["mapping_file"] = mapping_file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.mapping, Unset):
            files.append(("mapping", (None, str(self.mapping.value).encode(), "text/plain")))

        if not isinstance(self.mapping_file, Unset):
            files.append(("mapping_file", self.mapping_file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mapping = d.pop("mapping", UNSET)
        mapping: Union[Unset, BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping]
        if isinstance(_mapping, Unset):
            mapping = UNSET
        else:
            mapping = BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping(_mapping)

        _mapping_file = d.pop("mapping_file", UNSET)
        mapping_file: Union[Unset, File]
        if isinstance(_mapping_file, Unset):
            mapping_file = UNSET
        else:
            mapping_file = File(payload=BytesIO(_mapping_file))

        body_update_avatar_mapping_avatar_uuid_mapping_patch = cls(
            mapping=mapping,
            mapping_file=mapping_file,
        )

        body_update_avatar_mapping_avatar_uuid_mapping_patch.additional_properties = d
        return body_update_avatar_mapping_avatar_uuid_mapping_patch

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
