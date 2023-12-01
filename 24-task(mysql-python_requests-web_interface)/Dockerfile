FROM python:3.8

COPY setup_db.py /app/

WORKDIR /app

RUN pip install mysql-connector-python

#EXPOSE 3306

CMD ["python", "setup_db.py"]
