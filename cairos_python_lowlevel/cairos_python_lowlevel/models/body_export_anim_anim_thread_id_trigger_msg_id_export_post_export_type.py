from enum import Enum


class BodyExportAnimAnimThreadIdTriggerMsgIdExportPostExportType(str, Enum):
    VALUE_0 = ".glb"
    VALUE_1 = ".fbx"

    def __str__(self) -> str:
        return str(self.value)
