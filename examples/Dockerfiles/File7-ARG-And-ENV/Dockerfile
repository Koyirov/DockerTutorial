FROM debian

ARG install_software=python3

RUN apt-get update && apt-get install -y $install_software

WORKDIR /projekt

COPY main.py .

ENV PROGRAM=python3

CMD $PROGRAM "main.py"