# Django BoilerPlate

## Setup

~~~shell
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements
python manage.py makemigrations
python manage.py loaddata fixtures/data
python manage.py migrate
python manage.py autoload
~~~

comment out the `theme` app from INSTALLED_APPS in settings.py

```python
INSTALLED_APPS = [
    ...,
    'tailwind',
    # 'theme',
    ...
]
```

```bash
python manage.py tailwind init
````

uncomment out the `theme` app from INSTALLED_APPS in settings.py

```python
INSTALLED_APPS = [
    ...,
    'tailwind',
    'theme',
    ...
]
```

```bash
python manage.py tailwind install
python manage.py npm start
```