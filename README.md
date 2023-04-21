# Django Backend app for Flight Bookings

## Demo of Application:
- Drive link [Link](https://drive.google.com/file/d/1QY6SYgLPStZfl7mG8qnWoNUHV9-20nmc/view?usp=sharing)

## Hosted Application link:
- Link to Hosted App - [Link](https://devrev-production.up.railway.app/)
- You cannota access /admin without credentials


## Steps to follow to run app


#### Installation :

- Fork the Repository (top-right) or clone it with :
- Use the cmd to the folder where you want to install app
```
$ git clone https://github.com/DhruvBajaj01/Devrev.git 
```
- From cmd navigate into the Project folder flight_booking :
```
$ cd flight_booking
```

#### Activating Virtual Environment :

```
$ venv\Scripts\activate
```

#### Install requirements :

```
$ pip install -r requirements.txt
```
- Once all the packages are installed, run the app using :

#### Run the app:

```
$ python mange.py runserver
```

## Project Tree/ Directory Structure

```
flight
└─ flight_booking
   ├─ app
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  ├─ __init__.py
   │  │  └─ __pycache__
   │  │     ├─ 0001_initial.cpython-39.pyc
   │  │     └─ __init__.cpython-39.pyc
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  ├─ views.py
   │  ├─ __init__.py
   │  └─ __pycache__
   │     ├─ admin.cpython-39.pyc
   │     ├─ apps.cpython-39.pyc
   │     ├─ forms.cpython-39.pyc
   │     ├─ models.cpython-39.pyc
   │     ├─ urls.cpython-39.pyc
   │     ├─ views.cpython-39.pyc
   │     └─ __init__.cpython-39.pyc
   ├─ db.sqlite3
   ├─ flight_booking
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  ├─ views.py
   │  ├─ wsgi.py
   │  ├─ __init__.py
   │  └─ __pycache__
   │     ├─ settings.cpython-39.pyc
   │     ├─ urls.cpython-39.pyc
   │     ├─ views.cpython-39.pyc
   │     ├─ wsgi.cpython-39.pyc
   │     └─ __init__.cpython-39.pyc
   ├─ manage.py
   └─ templates
      ├─ base.html
      ├─ bookflight.html
      ├─ home.html
      ├─ mybookings.html
      ├─ registration
      │  ├─ login.html
      │  └─ signup.html
      └─ searchflight.html

```

## About Application

#### Type of Users
- User 
- Admin

#### User Use Cases(features)
- Login
- Sign up
- Searching for flights based on date and time
- Booking tickets on a flight based on availability (assuming the default
seat count is 60)
- My Booking -&gt; to list out all the bookings made by that user
- Logout

#### Admin Use Cases(freatures)
- Login (Seperate login for Admin)
- Add Flights
- Remove flights
- View all the booking based on flight number and time

## Tech stack to build Backend

- Django (Backend-Development)
- sqlite (Database)
- HTML  (Rendering UI)
- Postman (API testing)


