from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_message_type import AIMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_message_additional_kwargs import AIMessageAdditionalKwargs
    from ..models.ai_message_content_type_1_item_type_1 import AIMessageContentType1ItemType1
    from ..models.ai_message_response_metadata import AIMessageResponseMetadata
    from ..models.invalid_tool_call import InvalidToolCall
    from ..models.tool_call import ToolCall
    from ..models.usage_metadata import UsageMetadata


T = TypeVar("T", bound="AIMessage")


@_attrs_define
class AIMessage:
    """Message from an AI.

    AIMessage is returned from a chat model as a response to a prompt.

    This message represents the output of the model and consists of both
    the raw output as returned by the model together standardized fields
    (e.g., tool calls, usage metadata) added by the LangChain framework.

        Attributes:
            content (Union[list[Union['AIMessageContentType1ItemType1', str]], str]):
            additional_kwargs (Union[Unset, AIMessageAdditionalKwargs]):
            response_metadata (Union[Unset, AIMessageResponseMetadata]):
            type_ (Union[Unset, AIMessageType]):  Default: AIMessageType.AI.
            name (Union[Unset, str]):
            id (Union[Unset, str]):
            example (Union[Unset, bool]):  Default: False.
            tool_calls (Union[Unset, list['ToolCall']]):
            invalid_tool_calls (Union[Unset, list['InvalidToolCall']]):
            usage_metadata (Union[Unset, UsageMetadata]):
    """

    content: Union[list[Union["AIMessageContentType1ItemType1", str]], str]
    additional_kwargs: Union[Unset, "AIMessageAdditionalKwargs"] = UNSET
    response_metadata: Union[Unset, "AIMessageResponseMetadata"] = UNSET
    type_: Union[Unset, AIMessageType] = AIMessageType.AI
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    example: Union[Unset, bool] = False
    tool_calls: Union[Unset, list["ToolCall"]] = UNSET
    invalid_tool_calls: Union[Unset, list["InvalidToolCall"]] = UNSET
    usage_metadata: Union[Unset, "UsageMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_message_content_type_1_item_type_1 import AIMessageContentType1ItemType1

        content: Union[list[Union[dict[str, Any], str]], str]
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: Union[dict[str, Any], str]
                if isinstance(content_type_1_item_data, AIMessageContentType1ItemType1):
                    content_type_1_item = content_type_1_item_data.to_dict()
                else:
                    content_type_1_item = content_type_1_item_data
                content.append(content_type_1_item)

        else:
            content = self.content

        additional_kwargs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.additional_kwargs, Unset):
            additional_kwargs = self.additional_kwargs.to_dict()

        response_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        id = self.id

        example = self.example

        tool_calls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data.to_dict()
                tool_calls.append(tool_calls_item)

        invalid_tool_calls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_tool_calls, Unset):
            invalid_tool_calls = []
            for invalid_tool_calls_item_data in self.invalid_tool_calls:
                invalid_tool_calls_item = invalid_tool_calls_item_data.to_dict()
                invalid_tool_calls.append(invalid_tool_calls_item)

        usage_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage_metadata, Unset):
            usage_metadata = self.usage_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if additional_kwargs is not UNSET:
            field_dict["additional_kwargs"] = additional_kwargs
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if example is not UNSET:
            field_dict["example"] = example
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if invalid_tool_calls is not UNSET:
            field_dict["invalid_tool_calls"] = invalid_tool_calls
        if usage_metadata is not UNSET:
            field_dict["usage_metadata"] = usage_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_message_additional_kwargs import AIMessageAdditionalKwargs
        from ..models.ai_message_content_type_1_item_type_1 import AIMessageContentType1ItemType1
        from ..models.ai_message_response_metadata import AIMessageResponseMetadata
        from ..models.invalid_tool_call import InvalidToolCall
        from ..models.tool_call import ToolCall
        from ..models.usage_metadata import UsageMetadata

        d = dict(src_dict)

        def _parse_content(data: object) -> Union[list[Union["AIMessageContentType1ItemType1", str]], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in _content_type_1:

                    def _parse_content_type_1_item(data: object) -> Union["AIMessageContentType1ItemType1", str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_1 = AIMessageContentType1ItemType1.from_dict(data)

                            return content_type_1_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(Union["AIMessageContentType1ItemType1", str], data)

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[Union["AIMessageContentType1ItemType1", str]], str], data)

        content = _parse_content(d.pop("content"))

        _additional_kwargs = d.pop("additional_kwargs", UNSET)
        additional_kwargs: Union[Unset, AIMessageAdditionalKwargs]
        if isinstance(_additional_kwargs, Unset):
            additional_kwargs = UNSET
        else:
            additional_kwargs = AIMessageAdditionalKwargs.from_dict(_additional_kwargs)

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: Union[Unset, AIMessageResponseMetadata]
        if isinstance(_response_metadata, Unset):
            response_metadata = UNSET
        else:
            response_metadata = AIMessageResponseMetadata.from_dict(_response_metadata)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AIMessageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AIMessageType(_type_)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        example = d.pop("example", UNSET)

        tool_calls = []
        _tool_calls = d.pop("tool_calls", UNSET)
        for tool_calls_item_data in _tool_calls or []:
            tool_calls_item = ToolCall.from_dict(tool_calls_item_data)

            tool_calls.append(tool_calls_item)

        invalid_tool_calls = []
        _invalid_tool_calls = d.pop("invalid_tool_calls", UNSET)
        for invalid_tool_calls_item_data in _invalid_tool_calls or []:
            invalid_tool_calls_item = InvalidToolCall.from_dict(invalid_tool_calls_item_data)

            invalid_tool_calls.append(invalid_tool_calls_item)

        _usage_metadata = d.pop("usage_metadata", UNSET)
        usage_metadata: Union[Unset, UsageMetadata]
        if isinstance(_usage_metadata, Unset):
            usage_metadata = UNSET
        else:
            usage_metadata = UsageMetadata.from_dict(_usage_metadata)

        ai_message = cls(
            content=content,
            additional_kwargs=additional_kwargs,
            response_metadata=response_metadata,
            type_=type_,
            name=name,
            id=id,
            example=example,
            tool_calls=tool_calls,
            invalid_tool_calls=invalid_tool_calls,
            usage_metadata=usage_metadata,
        )

        ai_message.additional_properties = d
        return ai_message

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
