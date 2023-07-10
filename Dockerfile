# set base image (host OS)
FROM python:3.10.12-slim-buster

# install unzip and curl
RUN apt-get update && apt install -y \
    curl \
    unzip

# install rclone
RUN curl https://rclone.org/install.sh | bash

# set the working directory in the container
WORKDIR /backup

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD [ "python", "main.py" ]