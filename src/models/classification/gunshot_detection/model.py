import logging

# import torch

from src.domain.abstract_model import AbstractModel, T


class Model(AbstractModel):
    def __init__(self, path_to_weights: str, model_name: str):
        self._model_name = model_name
        self._logger = logging.getLogger(f"Model: {self._model_name}")

        # self._device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # self._logger.debug(f"Using device: {self._device}")

        # self._model: torch.nn.Module = torch.load(path_to_weights)
        # self._model.to(self._device)
        # self._model.eval()

    def postprocess(self, data: T):
        pass

    @property
    def name(self) -> str:
        return self._model_name

    def preprocess(self, data: bytes) -> T:
        pass

    def forward(self, data: T):
        pass
