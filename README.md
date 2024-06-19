# Petter API

## Installing using GitHub

Python should be installed

```shell
git clone https://github.com/DanSheremeta/airport-api.git
cd team-project-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Getting access

- create user via /api/user/register/
- get access token via /api/user/token/
- refresh access token via /api/user/token/refresh/

## Documentation

- Documentation available via /api/doc/swagger/
