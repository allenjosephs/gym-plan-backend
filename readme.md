# gym-plan-backend

## Project Overview
This repo is the backend of an application called "Gym Plan".  For more information on the overall purpose/intent of the application, please reference the front-end repo linked below.

## Important Links
- [Front-end repo](https://github.com/allenjosephs/gym-plan)
- [Back-end repo (yes, the repo that you're currently in)](https://github.com/lilspikey333/better_IMDB)

## Technologies Overview
- Django
- Django REST Framework (DRF)
- PostgresSQL
- JSON Web Tokens (JWT)

## Prerequisites for setting up this application locally
- Python (recommend v3.8.0+)
- Python virtual environment
- PostgreSQL (recommend v12.1+)

## Setup Instructions (Note: all actions were performed on a Mac and assumes Python v3+)
- Clone down this repo and ```cd``` into the local directory
- Activate a python virtual environment: ```python3 -m venv .env```
- Set up a local PostgreSQL db
    - From a terminal: ```psql```
    - `CREATE DATABASE gym_plan;`
    - `CREATE USER gym_plan WITH PASSWORD '<your password here>'`;
    - `GRANT ALL PRIVILEGES ON DATABASE gym_plan TO gym_plan`;
    - ```\q```
- Run the migrate command: ```python3 manage.py migrate```
- Create superuser (using any desired username/pwd): ```python3 manage.py createsuperuser```
- Install the Django REST framework simple JWT library: ```pip install djangorestframework_simplejwt```
- Start the server: ```python3 manage.py runserver```
- Verify server is started by visiting http://localhost:8000 in a browser

## Models used in this application
- Exercise
    - XXX

- Workout
    - XXX

- User
    - name