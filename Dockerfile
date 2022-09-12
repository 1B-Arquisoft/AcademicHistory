FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:8000

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]