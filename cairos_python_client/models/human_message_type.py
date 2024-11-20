from enum import Enum


class HumanMessageType(str, Enum):
    HUMAN = "human"

    def __str__(self) -> str:
        return str(self.value)
