FROM python:3.10

WORKDIR /PW02

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "__main__.py"]