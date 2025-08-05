from enum import Enum


class BodyUpdateAvatarMappingAvatarUuidMappingPatchMapping(str, Enum):
    AUTOMATIC = "automatic"
    MIXAMO = "mixamo"

    def __str__(self) -> str:
        return str(self.value)
