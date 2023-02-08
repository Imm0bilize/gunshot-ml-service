from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T')


class AbstractModel(ABC):
    @abstractmethod
    def forward(self, data: T):
        raise NotImplemented

    @abstractmethod
    def preprocess(self, data: bytes) -> T:
        raise NotImplemented

    @abstractmethod
    def postprocess(self, data: T):
        raise NotImplemented

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplemented
