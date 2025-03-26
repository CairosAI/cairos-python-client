from enum import Enum


class ToolMessageType(str, Enum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
