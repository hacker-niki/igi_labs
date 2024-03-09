FROM python:3.9

ENV Radius 5

WORKDIR /app

COPY main.py .

COPY geometric_lib ./geometric_lib

EXPOSE 8000

RUN pip install flask

ENTRYPOINT ["python", "main.py"]
