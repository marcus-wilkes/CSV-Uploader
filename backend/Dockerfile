FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]
