FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /api /api
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.1/wait /wait
RUN chmod +x /wait
ENTRYPOINT /wait && python3 api/app.py
