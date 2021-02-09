FROM python:3.8

COPY requirement.txt /usr/share/app/

WORKDIR /usr/share/app

RUN pip install -r requirement.txt

COPY . /usr/share/app

EXPOSE 5000

CMD python /usr/share/app/app.py
