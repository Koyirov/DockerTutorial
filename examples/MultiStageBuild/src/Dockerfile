FROM debian AS stage-debian
RUN apt-get update && apt-get install -y neofetch
WORKDIR /app
RUN neofetch > debian.txt

FROM ubuntu AS stage-ubuntu
RUN apt-get update && apt-get install -y neofetch
WORKDIR /app
RUN neofetch > ubuntu.txt

FROM alpine
WORKDIR /app
COPY --from=stage-debian /app/debian.txt .
COPY --from=stage-ubuntu /app/ubuntu.txt .






