FROM python:3.11-slim

ADD main.py .
ADD second_acc.session .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
