# Django BoilerPlate

## Setup
~~~shell
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements
python manage.py makemigrations
python manage.py loaddata fixtures/data
python manage.py migrate
~~~