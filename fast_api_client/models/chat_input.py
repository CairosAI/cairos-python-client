from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from //fastapi_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_message import AIMessage
    from ..models.animation import Animation
    from ..models.avatar_metadata import AvatarMetadata
    from ..models.function_message import FunctionMessage
    from ..models.human_message import HumanMessage
    from ..models.system_message import SystemMessage


T = TypeVar("T", bound="ChatInput")


@_attrs_define
class ChatInput:
    """
    Attributes:
        prompt (HumanMessage): Message from a human.

            HumanMessages are messages that are passed in from a human to the model.

            Example:

                .. code-block:: python

                    from langchain_core.messages import HumanMessage, SystemMessage

                    messages = [
                        SystemMessage(
                            content="You are a helpful assistant! Your name is Bob."
                        ),
                        HumanMessage(
                            content="What is your name?"
                        )
                    ]

                    # Instantiate a chat model and invoke it with the messages
                    model = ...
                    print(model.invoke(messages))
        history (List[Union['AIMessage', 'FunctionMessage', 'HumanMessage', 'SystemMessage']]):
        avatar (AvatarMetadata):
        btl_objs (List[Any]):
        animation (Union[Unset, List['Animation']]):
    """

    prompt: "HumanMessage"
    history: List[Union["AIMessage", "FunctionMessage", "HumanMessage", "SystemMessage"]]
    avatar: "AvatarMetadata"
    btl_objs: List[Any]
    animation: Union[Unset, List["Animation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ai_message import AIMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage

        prompt = self.prompt.to_dict()

        history = []
        for history_item_data in self.history:
            history_item: Dict[str, Any]
            if isinstance(history_item_data, HumanMessage):
                history_item = history_item_data.to_dict()
            elif isinstance(history_item_data, AIMessage):
                history_item = history_item_data.to_dict()
            elif isinstance(history_item_data, SystemMessage):
                history_item = history_item_data.to_dict()
            else:
                history_item = history_item_data.to_dict()

            history.append(history_item)

        avatar = self.avatar.to_dict()

        btl_objs = self.btl_objs

        animation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.animation, Unset):
            animation = []
            for animation_item_data in self.animation:
                animation_item = animation_item_data.to_dict()
                animation.append(animation_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "history": history,
                "avatar": avatar,
                "btl_objs": btl_objs,
            }
        )
        if animation is not UNSET:
            field_dict["animation"] = animation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_message import AIMessage
        from ..models.animation import Animation
        from ..models.avatar_metadata import AvatarMetadata
        from ..models.function_message import FunctionMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage

        d = src_dict.copy()
        prompt = HumanMessage.from_dict(d.pop("prompt"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:

            def _parse_history_item(
                data: object,
            ) -> Union["AIMessage", "FunctionMessage", "HumanMessage", "SystemMessage"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    history_item_type_0 = HumanMessage.from_dict(data)

                    return history_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    history_item_type_1 = AIMessage.from_dict(data)

                    return history_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    history_item_type_2 = SystemMessage.from_dict(data)

                    return history_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                history_item_type_3 = FunctionMessage.from_dict(data)

                return history_item_type_3

            history_item = _parse_history_item(history_item_data)

            history.append(history_item)

        avatar = AvatarMetadata.from_dict(d.pop("avatar"))

        btl_objs = cast(List[Any], d.pop("btl_objs"))

        animation = []
        _animation = d.pop("animation", UNSET)
        for animation_item_data in _animation or []:
            animation_item = Animation.from_dict(animation_item_data)

            animation.append(animation_item)

        chat_input = cls(
            prompt=prompt,
            history=history,
            avatar=avatar,
            btl_objs=btl_objs,
            animation=animation,
        )

        chat_input.additional_properties = d
        return chat_input

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
