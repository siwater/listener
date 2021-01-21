FROM python:3.8-buster

COPY listener.py .
CMD ["python", "listener.py"]
