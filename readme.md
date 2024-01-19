```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
cd cap
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_sample_data  
python manage.py runserver
```
http://127.0.0.1:8000/
