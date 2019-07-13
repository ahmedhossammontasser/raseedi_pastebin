# Pastebin Service
A Django Rest Framework version 3.9.4 web service that share codes and notes with your friends using Token-based authentication system.

### Features
Each user (Logged in User or Anonymous User) can create edit delete any of his pastes. 
User can share paste using 3 types: 

 - Public paste to share with all users 
 -  Private paste to share for the user creator only 
 - Certain user paste to share with certain users

Each paste has a shortened URL using Universally unique identifier (uuid)

We are using sqllte3 for database management system
 
### This application requires:
		Python 3.6.7
		Django Rest Framework version 3.9.4
		Django version 2.2.3

### Installation Instructions
	## Using python 3.6
	pip install django
	pip install djangorestframework
	pip install drf_yasg
	pip install djangorestframework-csv

	## To create tables in database
	python manage.py makemigrations
	python manage.py migrate 

	python manage.py loaddata typepaste_fixtures.json

	## To create admin 
	python manage.py createsuperuser
	
	## To run server 
	python manage.py runserver
