from enum import Enum


class StoredMessageType(str, Enum):
    AI = "ai"
    HUMAN = "human"
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
