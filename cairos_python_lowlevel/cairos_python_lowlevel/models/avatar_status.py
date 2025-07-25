from enum import Enum


class AvatarStatus(str, Enum):
    AUTORIGGED = "autorigged"
    UPLOADED = "uploaded"

    def __str__(self) -> str:
        return str(self.value)
