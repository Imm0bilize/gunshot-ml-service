from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ["ids", "payloads"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    payloads: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., payloads: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ["ids", "prob"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    PROB_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    prob: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., prob: _Optional[_Iterable[float]] = ...) -> None: ...
