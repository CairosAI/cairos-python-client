from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ai_message import AIMessage
    from ..models.human_message import HumanMessage
    from ..models.system_message import SystemMessage
    from ..models.tool_message import ToolMessage


T = TypeVar("T", bound="ChatContext")


@_attrs_define
class ChatContext:
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
        history (list[Union['AIMessage', 'HumanMessage', 'SystemMessage', 'ToolMessage']]):
    """

    prompt: "HumanMessage"
    history: list[Union["AIMessage", "HumanMessage", "SystemMessage", "ToolMessage"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_message import AIMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage

        prompt = self.prompt.to_dict()

        history = []
        for history_item_data in self.history:
            history_item: dict[str, Any]
            if isinstance(history_item_data, HumanMessage):
                history_item = history_item_data.to_dict()
            elif isinstance(history_item_data, AIMessage):
                history_item = history_item_data.to_dict()
            elif isinstance(history_item_data, SystemMessage):
                history_item = history_item_data.to_dict()
            else:
                history_item = history_item_data.to_dict()

            history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_message import AIMessage
        from ..models.human_message import HumanMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_message import ToolMessage

        d = dict(src_dict)
        prompt = HumanMessage.from_dict(d.pop("prompt"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:

            def _parse_history_item(data: object) -> Union["AIMessage", "HumanMessage", "SystemMessage", "ToolMessage"]:
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
                history_item_type_3 = ToolMessage.from_dict(data)

                return history_item_type_3

            history_item = _parse_history_item(history_item_data)

            history.append(history_item)

        chat_context = cls(
            prompt=prompt,
            history=history,
        )

        chat_context.additional_properties = d
        return chat_context

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
