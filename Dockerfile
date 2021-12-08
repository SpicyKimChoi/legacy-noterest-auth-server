FROM python:3

RUN mkdir ms-auth/

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["gunicorn", "-b 0.0.0.0:5000", "--reload", "-w 4", "app:app"]