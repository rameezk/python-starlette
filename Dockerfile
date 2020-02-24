FROM python:3.7-alpine as base

FROM base as builder

RUN apk add --no-cache gcc musl-dev make

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt


FROM BASE

COPY --from=builder /install /usr/local
COPY src /app/

WORKDIR /app
USER 1001

CMD ["sh", "entrypoint.sh"]
