FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0", "-p", "80", "--reload"]