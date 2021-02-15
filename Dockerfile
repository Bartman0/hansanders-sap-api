FROM python:3.8-slim

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD app app/
ADD yaml-resolved/swagger.yaml app/

CMD python app/main.py
