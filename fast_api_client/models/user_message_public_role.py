from enum import Enum


class UserMessagePublicRole(str, Enum):
    HUMAN = "human"

    def __str__(self) -> str:
        return str(self.value)
