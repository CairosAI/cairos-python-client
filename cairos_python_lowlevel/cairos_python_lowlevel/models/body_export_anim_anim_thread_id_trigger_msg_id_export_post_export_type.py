from enum import Enum


class BodyExportAnimAnimThreadIdTriggerMsgIdExportPostExportType(str, Enum):
    VALUE_0 = ".glb"

    def __str__(self) -> str:
        return str(self.value)
