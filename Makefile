.PHONY: gen-proto
gen-proto:
	python -m grpc.tools.protoc -I api/v1 ml_service.proto --python_out=src/api/v1 --grpc_python_out=src/api/v1 --pyi_out=src/api/v1