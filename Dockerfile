FROM python:3-alpine

RUN apk --no-cache add git

RUN mkdir data_cache

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./worker.py"]
