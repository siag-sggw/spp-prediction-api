FROM python:3.6-alpine3.8

# Donwload project
RUN apk update && \
    apk upgrade && \
    apk add bash git && \
    mkdir -m 664 /app && \
    git clone -b develop --single-branch https://github.com/KowalikJakub/spp-prediction-api.git /app

# Copy app configuration
COPY ./app_config.json /etc/spp_api_config.json

# Install dependencies
COPY ./requirements.txt /app
RUN pip install $(cat /app/requirements.txt)

EXPOSE 8000

ENTRYPOINT python /app/src/main.py -c /etc/spp_api_config.json
