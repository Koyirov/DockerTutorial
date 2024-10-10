FROM ubuntu

RUN apt-get update && apt-get install -y vim

WORKDIR /app

COPY ./text.txt .

ENTRYPOINT ["vim"]
CMD ["text.txt"]