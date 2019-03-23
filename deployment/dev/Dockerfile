FROM python:3.6-alpine3.8

RUN apk update && \
    apk upgrade && \
    apk add bash git && \
    mkdir -m 664 /app && \
    git clone -b develop --single-branch https://github.com/siag-sggw/spp-prediction-api.git /app
COPY ./app_config.json /etc/spp_api_config.json

EXPOSE 8000

ENTRYPOINT [ "/app/deployment/dev/run.sh" ]
