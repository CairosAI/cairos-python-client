from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_message_type import SystemMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_message_additional_kwargs import SystemMessageAdditionalKwargs
    from ..models.system_message_content_type_1_item_type_1 import SystemMessageContentType1ItemType1
    from ..models.system_message_response_metadata import SystemMessageResponseMetadata


T = TypeVar("T", bound="SystemMessage")


@_attrs_define
class SystemMessage:
    """Message for priming AI behavior.

    The system message is usually passed in as the first of a sequence
    of input messages.

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

            # Define a chat model and invoke it with the messages
            print(model.invoke(messages))

        Attributes:
            content (Union[list[Union['SystemMessageContentType1ItemType1', str]], str]):
            additional_kwargs (Union[Unset, SystemMessageAdditionalKwargs]):
            response_metadata (Union[Unset, SystemMessageResponseMetadata]):
            type_ (Union[Unset, SystemMessageType]):  Default: SystemMessageType.SYSTEM.
            name (Union[Unset, str]):
            id (Union[Unset, str]):
    """

    content: Union[list[Union["SystemMessageContentType1ItemType1", str]], str]
    additional_kwargs: Union[Unset, "SystemMessageAdditionalKwargs"] = UNSET
    response_metadata: Union[Unset, "SystemMessageResponseMetadata"] = UNSET
    type_: Union[Unset, SystemMessageType] = SystemMessageType.SYSTEM
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_message_content_type_1_item_type_1 import SystemMessageContentType1ItemType1

        content: Union[list[Union[dict[str, Any], str]], str]
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: Union[dict[str, Any], str]
                if isinstance(content_type_1_item_data, SystemMessageContentType1ItemType1):
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_message_additional_kwargs import SystemMessageAdditionalKwargs
        from ..models.system_message_content_type_1_item_type_1 import SystemMessageContentType1ItemType1
        from ..models.system_message_response_metadata import SystemMessageResponseMetadata

        d = dict(src_dict)

        def _parse_content(data: object) -> Union[list[Union["SystemMessageContentType1ItemType1", str]], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in _content_type_1:

                    def _parse_content_type_1_item(data: object) -> Union["SystemMessageContentType1ItemType1", str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_1 = SystemMessageContentType1ItemType1.from_dict(data)

                            return content_type_1_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(Union["SystemMessageContentType1ItemType1", str], data)

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[Union["SystemMessageContentType1ItemType1", str]], str], data)

        content = _parse_content(d.pop("content"))

        _additional_kwargs = d.pop("additional_kwargs", UNSET)
        additional_kwargs: Union[Unset, SystemMessageAdditionalKwargs]
        if isinstance(_additional_kwargs, Unset):
            additional_kwargs = UNSET
        else:
            additional_kwargs = SystemMessageAdditionalKwargs.from_dict(_additional_kwargs)

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: Union[Unset, SystemMessageResponseMetadata]
        if isinstance(_response_metadata, Unset):
            response_metadata = UNSET
        else:
            response_metadata = SystemMessageResponseMetadata.from_dict(_response_metadata)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SystemMessageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SystemMessageType(_type_)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        system_message = cls(
            content=content,
            additional_kwargs=additional_kwargs,
            response_metadata=response_metadata,
            type_=type_,
            name=name,
            id=id,
        )

        system_message.additional_properties = d
        return system_message

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
