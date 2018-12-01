FROM python:3.6.7

ENV LANG C.UTF-8

RUN mkdir /beer
WORKDIR /beer
ADD requirements.txt /beer
RUN pip install -r requirements.txt
ADD ./beer_api /beer/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

ENTRYPOINT ["python", "/beer/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
