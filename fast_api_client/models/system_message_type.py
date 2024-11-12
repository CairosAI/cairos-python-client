from enum import Enum


class SystemMessageType(str, Enum):
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
