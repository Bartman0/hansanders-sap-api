FROM python:3.8-slim

ADD app app/
ADD yaml-resolved/swagger.yaml app/
