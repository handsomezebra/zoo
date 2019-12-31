# Sentence-BERT

This is the docker container for the following model: *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks* [[paper]](https://arxiv.org/abs/1908.10084) [[code]](https://github.com/UKPLab/sentence-transformers)

## Build docker
`docker build -t sentence-bert:1.0-cpu .`  
`docker build -f Dockerfile_gpu -t sentence-bert:1.0-gpu .`

## Run docker
`docker run -d -p 10000:10000 sentence-bert:1.0-cpu` 
`docker run -d -p 10000:10000 --runtime=nvidia sentence-bert:1.0-gpu` 