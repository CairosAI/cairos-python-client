from enum import Enum


class BodyPostAvatarAvatarNewLabelPostMapping(str, Enum):
    MIXAMO = "mixamo"

    def __str__(self) -> str:
        return str(self.value)
