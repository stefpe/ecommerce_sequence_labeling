FROM python:3

WORKDIR /usr/src/app

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3"]