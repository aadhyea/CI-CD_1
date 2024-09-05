FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN python -m ensurepip --upgrade
RUN pip install --upgrade pip

CMD ["python", "Calc.py"]
