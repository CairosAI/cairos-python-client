from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.animation import Animation


T = TypeVar("T", bound="ChatOutput")


@_attrs_define
class ChatOutput:
    """
    Attributes:
        trigger_msg (UUID):
        messages (List[Any]):
        btl_objs (str):
        animation (Animation):
    """

    trigger_msg: UUID
    messages: List[Any]
    btl_objs: str
    animation: "Animation"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trigger_msg = str(self.trigger_msg)

        messages = self.messages

        btl_objs = self.btl_objs

        animation = self.animation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_msg": trigger_msg,
                "messages": messages,
                "btl_objs": btl_objs,
                "animation": animation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.animation import Animation

        d = src_dict.copy()
        trigger_msg = UUID(d.pop("trigger_msg"))

        messages = cast(List[Any], d.pop("messages"))

        btl_objs = d.pop("btl_objs")

        animation = Animation.from_dict(d.pop("animation"))

        chat_output = cls(
            trigger_msg=trigger_msg,
            messages=messages,
            btl_objs=btl_objs,
            animation=animation,
        )

        chat_output.additional_properties = d
        return chat_output

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
