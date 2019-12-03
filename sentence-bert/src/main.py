# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI
import logging
from sentence_transformers import SentenceTransformer

from src.utility import load_config, setup_logging
conf = load_config()

logger = logging.getLogger(__name__)

app = FastAPI()


pretrained_weights = 'bert-large-nli-stsb-mean-tokens'
model = SentenceTransformer(pretrained_weights)

@app.post("/predict")
async def predict(data: dict):
    logger.info("Received data")

    sentence_embeddings = model.encode(data["text_list"])

    sentence_embeddings = [x.tolist() for x in sentence_embeddings]

    logger.info("Done generating embeddings")

    return sentence_embeddings


if __name__ == "__main__":
    setup_logging()
    uvicorn.run(app, host="0.0.0.0", port=conf["server_port"])
