FROM python:3.11
WORKDIR /usr/src/app
COPY . .
ENV PYTHONUNBUFFERED 1
CMD ["python3", "-i"]
