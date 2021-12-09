FROM python:3.7-alpine
WORKDIR /app
COPY graphdata.py /app
COPY ./requirements.txt /app
COPY ./movies.cypher /app
RUN pip install -r requirements.txt
CMD ["python","graphdata.py"]
