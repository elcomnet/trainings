FROM python:3.8-slim-buster

LABEL version="6.0"
LABEL engine="python"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
