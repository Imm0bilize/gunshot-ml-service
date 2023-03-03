torch-model-archiver \
  --model-name gunshot_detection \
  --version 1.0 \
  --serialized-file handlers/gunshot_detection/weights/mobilenetv2_trace.pt \
  --handler handlers/gunshot_detection/handler.py \
  --requirements-file handlers/gunshot_detection/requirements.txt

mv gunshot_detection.mar model_store/gunshot_detection.mar

