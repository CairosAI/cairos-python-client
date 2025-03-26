from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_message_status import ToolMessageStatus
from ..models.tool_message_type import ToolMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_message_additional_kwargs import ToolMessageAdditionalKwargs
    from ..models.tool_message_content_type_1_item_type_1 import ToolMessageContentType1ItemType1
    from ..models.tool_message_response_metadata import ToolMessageResponseMetadata


T = TypeVar("T", bound="ToolMessage")


@_attrs_define
class ToolMessage:
    """Message for passing the result of executing a tool back to a model.

    ToolMessages contain the result of a tool invocation. Typically, the result
    is encoded inside the `content` field.

    Example: A ToolMessage representing a result of 42 from a tool call with id

        .. code-block:: python

            from langchain_core.messages import ToolMessage

            ToolMessage(content='42', tool_call_id='call_Jja7J89XsjrOLA5r!MEOW!SL')


    Example: A ToolMessage where only part of the tool output is sent to the model
        and the full output is passed in to artifact.

        .. versionadded:: 0.2.17

        .. code-block:: python

            from langchain_core.messages import ToolMessage

            tool_output = {
                "stdout": "From the graph we can see that the correlation between x and y is ...",
                "stderr": None,
                "artifacts": {"type": "image", "base64_data": "/9j/4gIcSU..."},
            }

            ToolMessage(
                content=tool_output["stdout"],
                artifact=tool_output,
                tool_call_id='call_Jja7J89XsjrOLA5r!MEOW!SL',
            )

    The tool_call_id field is used to associate the tool call request with the
    tool call response. This is useful in situations where a chat model is able
    to request multiple tool calls in parallel.

        Attributes:
            content (Union[List[Union['ToolMessageContentType1ItemType1', str]], str]):
            tool_call_id (str):
            additional_kwargs (Union[Unset, ToolMessageAdditionalKwargs]):
            response_metadata (Union[Unset, ToolMessageResponseMetadata]):
            type (Union[Unset, ToolMessageType]):  Default: ToolMessageType.TOOL.
            name (Union[Unset, str]):
            id (Union[Unset, str]):
            artifact (Union[Unset, Any]):
            status (Union[Unset, ToolMessageStatus]):  Default: ToolMessageStatus.SUCCESS.
    """

    content: Union[List[Union["ToolMessageContentType1ItemType1", str]], str]
    tool_call_id: str
    additional_kwargs: Union[Unset, "ToolMessageAdditionalKwargs"] = UNSET
    response_metadata: Union[Unset, "ToolMessageResponseMetadata"] = UNSET
    type: Union[Unset, ToolMessageType] = ToolMessageType.TOOL
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    artifact: Union[Unset, Any] = UNSET
    status: Union[Unset, ToolMessageStatus] = ToolMessageStatus.SUCCESS
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.tool_message_content_type_1_item_type_1 import ToolMessageContentType1ItemType1

        content: Union[List[Union[Dict[str, Any], str]], str]
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: Union[Dict[str, Any], str]
                if isinstance(content_type_1_item_data, ToolMessageContentType1ItemType1):
                    content_type_1_item = content_type_1_item_data.to_dict()
                else:
                    content_type_1_item = content_type_1_item_data
                content.append(content_type_1_item)

        else:
            content = self.content

        tool_call_id = self.tool_call_id

        additional_kwargs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_kwargs, Unset):
            additional_kwargs = self.additional_kwargs.to_dict()

        response_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name

        id = self.id

        artifact = self.artifact

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "tool_call_id": tool_call_id,
            }
        )
        if additional_kwargs is not UNSET:
            field_dict["additional_kwargs"] = additional_kwargs
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tool_message_additional_kwargs import ToolMessageAdditionalKwargs
        from ..models.tool_message_content_type_1_item_type_1 import ToolMessageContentType1ItemType1
        from ..models.tool_message_response_metadata import ToolMessageResponseMetadata

        d = src_dict.copy()

        def _parse_content(data: object) -> Union[List[Union["ToolMessageContentType1ItemType1", str]], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in _content_type_1:

                    def _parse_content_type_1_item(data: object) -> Union["ToolMessageContentType1ItemType1", str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_1 = ToolMessageContentType1ItemType1.from_dict(data)

                            return content_type_1_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(Union["ToolMessageContentType1ItemType1", str], data)

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[Union["ToolMessageContentType1ItemType1", str]], str], data)

        content = _parse_content(d.pop("content"))

        tool_call_id = d.pop("tool_call_id")

        _additional_kwargs = d.pop("additional_kwargs", UNSET)
        additional_kwargs: Union[Unset, ToolMessageAdditionalKwargs]
        if isinstance(_additional_kwargs, Unset):
            additional_kwargs = UNSET
        else:
            additional_kwargs = ToolMessageAdditionalKwargs.from_dict(_additional_kwargs)

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: Union[Unset, ToolMessageResponseMetadata]
        if isinstance(_response_metadata, Unset):
            response_metadata = UNSET
        else:
            response_metadata = ToolMessageResponseMetadata.from_dict(_response_metadata)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ToolMessageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ToolMessageType(_type)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        artifact = d.pop("artifact", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ToolMessageStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ToolMessageStatus(_status)

        tool_message = cls(
            content=content,
            tool_call_id=tool_call_id,
            additional_kwargs=additional_kwargs,
            response_metadata=response_metadata,
            type=type,
            name=name,
            id=id,
            artifact=artifact,
            status=status,
        )

        tool_message.additional_properties = d
        return tool_message

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
