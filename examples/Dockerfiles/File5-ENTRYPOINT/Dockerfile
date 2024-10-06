FROM debian

RUN apt-get update && apt-get install -y python3

COPY main.py /projekt/main.py

ENTRYPOINT ["python3"]
CMD ["/projekt/main.py"]