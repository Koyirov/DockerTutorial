FROM debian

RUN apt-get update && apt-get install -y python3

WORKDIR /projekt

COPY main.py .

ENTRYPOINT ["python3"]
CMD ["main.py"]