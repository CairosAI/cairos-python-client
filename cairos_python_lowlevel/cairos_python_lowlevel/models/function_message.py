from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_message_type import FunctionMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_message_additional_kwargs import FunctionMessageAdditionalKwargs
    from ..models.function_message_content_type_1_item_type_1 import FunctionMessageContentType1ItemType1
    from ..models.function_message_response_metadata import FunctionMessageResponseMetadata


T = TypeVar("T", bound="FunctionMessage")


@_attrs_define
class FunctionMessage:
    """Message for passing the result of executing a tool back to a model.

    FunctionMessage are an older version of the ToolMessage schema, and
    do not contain the tool_call_id field.

    The tool_call_id field is used to associate the tool call request with the
    tool call response. This is useful in situations where a chat model is able
    to request multiple tool calls in parallel.

        Attributes:
            content (Union[List[Union['FunctionMessageContentType1ItemType1', str]], str]):
            name (str):
            additional_kwargs (Union[Unset, FunctionMessageAdditionalKwargs]):
            response_metadata (Union[Unset, FunctionMessageResponseMetadata]):
            type (Union[Unset, FunctionMessageType]):  Default: FunctionMessageType.FUNCTION.
            id (Union[Unset, str]):
    """

    content: Union[List[Union["FunctionMessageContentType1ItemType1", str]], str]
    name: str
    additional_kwargs: Union[Unset, "FunctionMessageAdditionalKwargs"] = UNSET
    response_metadata: Union[Unset, "FunctionMessageResponseMetadata"] = UNSET
    type: Union[Unset, FunctionMessageType] = FunctionMessageType.FUNCTION
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.function_message_content_type_1_item_type_1 import FunctionMessageContentType1ItemType1

        content: Union[List[Union[Dict[str, Any], str]], str]
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: Union[Dict[str, Any], str]
                if isinstance(content_type_1_item_data, FunctionMessageContentType1ItemType1):
                    content_type_1_item = content_type_1_item_data.to_dict()
                else:
                    content_type_1_item = content_type_1_item_data
                content.append(content_type_1_item)

        else:
            content = self.content

        name = self.name

        additional_kwargs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_kwargs, Unset):
            additional_kwargs = self.additional_kwargs.to_dict()

        response_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "name": name,
            }
        )
        if additional_kwargs is not UNSET:
            field_dict["additional_kwargs"] = additional_kwargs
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.function_message_additional_kwargs import FunctionMessageAdditionalKwargs
        from ..models.function_message_content_type_1_item_type_1 import FunctionMessageContentType1ItemType1
        from ..models.function_message_response_metadata import FunctionMessageResponseMetadata

        d = src_dict.copy()

        def _parse_content(data: object) -> Union[List[Union["FunctionMessageContentType1ItemType1", str]], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in _content_type_1:

                    def _parse_content_type_1_item(data: object) -> Union["FunctionMessageContentType1ItemType1", str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_1 = FunctionMessageContentType1ItemType1.from_dict(data)

                            return content_type_1_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(Union["FunctionMessageContentType1ItemType1", str], data)

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[Union["FunctionMessageContentType1ItemType1", str]], str], data)

        content = _parse_content(d.pop("content"))

        name = d.pop("name")

        _additional_kwargs = d.pop("additional_kwargs", UNSET)
        additional_kwargs: Union[Unset, FunctionMessageAdditionalKwargs]
        if isinstance(_additional_kwargs, Unset):
            additional_kwargs = UNSET
        else:
            additional_kwargs = FunctionMessageAdditionalKwargs.from_dict(_additional_kwargs)

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: Union[Unset, FunctionMessageResponseMetadata]
        if isinstance(_response_metadata, Unset):
            response_metadata = UNSET
        else:
            response_metadata = FunctionMessageResponseMetadata.from_dict(_response_metadata)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FunctionMessageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FunctionMessageType(_type)

        id = d.pop("id", UNSET)

        function_message = cls(
            content=content,
            name=name,
            additional_kwargs=additional_kwargs,
            response_metadata=response_metadata,
            type=type,
            id=id,
        )

        function_message.additional_properties = d
        return function_message

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
