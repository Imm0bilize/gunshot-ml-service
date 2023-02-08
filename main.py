import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from src.controller.grpc.service import GRPCServer
from src.api.v1.ml_service_pb2_grpc import add_ModelServiceServicer_to_server
from src.models.classification.gunshot_detection.model import Model as GunshotDetection
from src.domain.service import ModelServicer


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger("main")

    cfg = {
        "address": "localhost:8080"
    }

    logger.debug("Creating models")
    models = [GunshotDetection("", "gunshot-detection")]
    model_servicer = ModelServicer(*models)

    server = grpc.server(ThreadPoolExecutor())

    add_ModelServiceServicer_to_server(GRPCServer(model_servicer), server)
    server.add_insecure_port(cfg["address"])
    server.start()
    logger.info(f"Server serving at {cfg['address']}")
    server.wait_for_termination()


if __name__ == '__main__':
    main()