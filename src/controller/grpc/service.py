import logging
from typing import Iterable

from src.api.v1.ml_service_pb2 import PredictRequest
from src.api.v1.ml_service_pb2_grpc import ModelServiceServicer
from src.domain.service import ModelServicer


class GRPCServer(ModelServiceServicer):
    def __init__(self, domain_service: ModelServicer):
        self.logger = logging.getLogger("grpc-server")
        self.domain_service = domain_service

    def Predict(self, request_iterator: Iterable[PredictRequest], context):
        for request in request_iterator:
            self.logger.info(request)