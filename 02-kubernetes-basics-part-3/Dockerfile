FROM python:alpine as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apk update \
    && apk upgrade \
    && apk add g++ gcc make libpq python3-dev musl-dev postgresql-dev

RUN pip install --upgrade pip

COPY app/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install \
    --user \
    --no-warn-script-location \
    -r requirements.txt
COPY app/ /app/


FROM python:alpine as app

LABEL maintainer="Ildyakov Aleksandr"

RUN apk update \
    && apk upgrade \
    && apk add libpq

ENV PYTHONBUNUFFERED 1
EXPOSE 8000

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/ /app/
WORKDIR /app/
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
