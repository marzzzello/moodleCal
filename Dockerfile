FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Create output directory
RUN mkdir -p /app/out

WORKDIR /app

VOLUME ["/app/out"]

COPY getcal.py /app/getcal.py

CMD ["python", "-u", "/app/getcal.py"]

