FROM python:alpine

LABEL maintainer="Ildyakov Aleksandr"

ENV PYTHONBUNUFFERED 1
EXPOSE 8000

RUN apk update && apk upgrade

WORKDIR /app/
COPY app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
