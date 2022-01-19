FROM debian:stable-20211220

RUN apt update \
    && apt upgrade -y \
    && apt install python3 -y \
    && apt install python3-pip -y \
    && apt install sqlite3 -y

# app dir
WORKDIR /blog

COPY . /blog

# dependencies
RUN pip3 install -r requirements.txt

# running
CMD ["python3", "index.py"]