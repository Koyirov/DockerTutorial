FROM golang:1.17-alpine AS builder
WORKDIR /app
COPY src .
RUN go build -o main

FROM alpine
WORKDIR /app
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]