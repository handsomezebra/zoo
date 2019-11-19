FROM haskell:8 AS builder

RUN apt-get update -qq && \
  apt-get install -qq -y libpcre3 libpcre3-dev build-essential --fix-missing --no-install-recommends && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/facebook/duckling.git
WORKDIR /duckling
RUN stack setup
RUN stack build --copy-bins duckling:exe:duckling-example-exe

FROM debian:stretch-slim

ENV LANG C.UTF-8

RUN apt-get update -qq && \
  apt-get install -qq -y libpcre3 libgmp10 --no-install-recommends && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=builder /root/.local/bin/duckling-example-exe /usr/local/bin/

EXPOSE 10000

CMD ["duckling-example-exe", "-p", "10000", "--no-access-log"]