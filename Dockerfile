FROM python:3

RUN mkdir ms-auth/

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-b 0.0.0.0", "--reload", \
     "-w 4", "app"]
     