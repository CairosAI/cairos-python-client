from enum import Enum


class AIMessagePublicRole(str, Enum):
    AI = "ai"

    def __str__(self) -> str:
        return str(self.value)
