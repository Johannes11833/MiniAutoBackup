# set base image (host OS)
FROM python:3.10.12-slim-buster

# install rclone
RUN apt-get update && apt install rclone -y

# set the working directory in the container
WORKDIR /backup

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD [ "python", "main.py" ]