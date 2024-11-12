from enum import Enum


class InvalidToolCallType(str, Enum):
    INVALID_TOOL_CALL = "invalid_tool_call"

    def __str__(self) -> str:
        return str(self.value)
