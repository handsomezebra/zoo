FROM continuumio/miniconda3:4.7.12

RUN \
  apt-get update && apt-get install -y --no-install-recommends build-essential && \
  rm -rf /var/lib/apt/lists/* && \
  conda install -y pytorch torchvision cpuonly -c pytorch && \
  conda clean --all -y && \
  pip install --no-cache-dir fastapi uvicorn pyyaml sentence-transformers && \
  rm -rf /root/.cache && \
  apt-get purge -y --auto-remove build-essential && \
  mkdir /root/sentence-bert && mkdir /root/sentence-bert/log

RUN python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('bert-large-nli-stsb-mean-tokens')"


ENV LOG_FILE=/root/sentence-bert/sentence-bert.log
EXPOSE 10000
WORKDIR /root/sentence-bert
COPY src src
ENTRYPOINT ["python", "-m", "src.transformers_main"]