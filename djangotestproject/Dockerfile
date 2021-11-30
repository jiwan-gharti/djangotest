FROM python:3.6-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir blogapp
WORKDIR /blogapp
RUN pip install --upgrade pip
COPY requirements.txt /blogapp/


RUN pip install -r requirements.txt
COPY . /blogapp/

EXPOSE 8000


CMD ["python","manage.py","runserver","0.0.0:8000"]