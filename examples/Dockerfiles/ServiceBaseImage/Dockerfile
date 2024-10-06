FROM debian

RUN apt-get update && apt-get install -y iputils-ping

ENTRYPOINT ["ping"]
CMD ["8.8.8.8"]