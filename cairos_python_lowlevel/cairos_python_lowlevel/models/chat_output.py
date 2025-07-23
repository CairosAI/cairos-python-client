from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.animation import Animation


T = TypeVar("T", bound="ChatOutput")


@_attrs_define
class ChatOutput:
    """
    Attributes:
        trigger_msg (UUID):
        messages (list[Any]):
        btl_objs (str):
        animation (Union['Animation', None, Unset]):
    """

    trigger_msg: UUID
    messages: list[Any]
    btl_objs: str
    animation: Union["Animation", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.animation import Animation

        trigger_msg = str(self.trigger_msg)

        messages = self.messages

        btl_objs = self.btl_objs

        animation: Union[None, Unset, dict[str, Any]]
        if isinstance(self.animation, Unset):
            animation = UNSET
        elif isinstance(self.animation, Animation):
            animation = self.animation.to_dict()
        else:
            animation = self.animation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_msg": trigger_msg,
                "messages": messages,
                "btl_objs": btl_objs,
            }
        )
        if animation is not UNSET:
            field_dict["animation"] = animation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.animation import Animation

        d = dict(src_dict)
        trigger_msg = UUID(d.pop("trigger_msg"))

        messages = cast(list[Any], d.pop("messages"))

        btl_objs = d.pop("btl_objs")

        def _parse_animation(data: object) -> Union["Animation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                animation_type_0 = Animation.from_dict(data)

                return animation_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Animation", None, Unset], data)

        animation = _parse_animation(d.pop("animation", UNSET))

        chat_output = cls(
            trigger_msg=trigger_msg,
            messages=messages,
            btl_objs=btl_objs,
            animation=animation,
        )

        chat_output.additional_properties = d
        return chat_output

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
