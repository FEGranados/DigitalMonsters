FROM python:3.10.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /DigitalMonster
RUN pip3 install --upgrade pip
COPY requirements.txt /DigitalMonster/

RUN pip3 install Django
RUN pip3 install -r requirements.txt
COPY ./DigitalMonster /DigitalMonster

RUN ls -la /DigitalMonster

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
