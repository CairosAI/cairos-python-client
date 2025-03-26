from enum import Enum


class UserMessagePublicType(str, Enum):
    HUMAN = "human"

    def __str__(self) -> str:
        return str(self.value)
