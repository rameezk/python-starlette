FROM python:3.7-alpine as base

FROM base as builder

# RUN apk add --no-cache gcc mailcap python3-dev build-base linux-headers pcre-dev postgresql-dev libffi-dev libressl-dev
RUN apk add --no-cache gcc musl-dev make

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt


FROM BASE

# RUN mkdir /app

COPY --from=builder /install /usr/local
COPY app.py entrypoint.sh /app/

WORKDIR /app

CMD ["sh", "entrypoint.sh"]

