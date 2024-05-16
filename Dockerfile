FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

RUN python manage.py makemigrations

CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
