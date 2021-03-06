FROM python:3.6.7

ENV LANG C.UTF-8

RUN mkdir /beer
WORKDIR /beer
ADD requirements.txt /beer
ADD djangoinit.sh /beer

RUN pip install -r requirements.txt
ADD ./beer_api /beer/

RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
RUN python manage.py test
RUN chmod +x djangoinit.sh
ENTRYPOINT ["python", "/beer/manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["/beer/djangoinit.sh"]

EXPOSE 8000
