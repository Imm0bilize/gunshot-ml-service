import logging
from typing import Dict


from src.domain.abstract_model import AbstractModel
from src.domain.exceptions import UnknownModelName


class ModelServicer(object):
    def __init__(self, *args: AbstractModel):
        self.models: Dict[str, AbstractModel] = {model.name: model for model in args}
        self.logger = logging.getLogger("model-servicer")

    @staticmethod
    def _make_forward(model, data):
        preprocessed_data = model.preprocess(data)

        output = model.forward(preprocessed_data)

        return model.postprocess(output)

    def __call__(self, model_name: str, data: bytes):
        try:
            model = self.models[model_name]
        except KeyError:
            raise UnknownModelName

        return self._make_forward(model, data)