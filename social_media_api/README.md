# Social Media API

## Setup

1. Clone repo
2. Create virtual environment and activate
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Run server: `python manage.py runserver`

## Endpoints

- **Register**: POST `/api/accounts/register/`
- **Login**: POST `/api/accounts/login/`
- Returns JWT `access` and `refresh` tokens