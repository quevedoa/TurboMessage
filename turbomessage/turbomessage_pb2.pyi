from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Correo(_message.Message):
    __slots__ = ["destinatario", "emisor", "id", "leido", "mensaje", "tema"]
    DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    EMISOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEIDO_FIELD_NUMBER: _ClassVar[int]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    TEMA_FIELD_NUMBER: _ClassVar[int]
    destinatario: str
    emisor: str
    id: int
    leido: bool
    mensaje: str
    tema: str
    def __init__(self, id: _Optional[int] = ..., tema: _Optional[str] = ..., emisor: _Optional[str] = ..., destinatario: _Optional[str] = ..., mensaje: _Optional[str] = ..., leido: bool = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["exito", "razon"]
    EXITO_FIELD_NUMBER: _ClassVar[int]
    RAZON_FIELD_NUMBER: _ClassVar[int]
    exito: bool
    razon: str
    def __init__(self, exito: bool = ..., razon: _Optional[str] = ...) -> None: ...

class Usuario(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
