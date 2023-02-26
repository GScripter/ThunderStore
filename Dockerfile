FROM python

WORKDIR /ThunderStore

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000

