# Reviews Site

### Live site

[Reviews](https://mohasreviews.herokuapp.com/)


#### Built by

[Mohamed Abdullahi](https://github.com/aenshtyn)

## Description

This is a django application that will allow a user to post a project he/she has created and get it reviewed by his/her peers.


## User Story

* Sign in to the application to start using.
* Upload pictures to the application.
* See profile with all pictures.
* Follow other users and see their pictures on timeline.
* Like a picture and leave a comment on it.


## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/aenshtyn/Reviews.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd instagram pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

## Technologies Used

* Python3.8
* Virtualenv
* HTML
* Bootsrap & CSS
* Git Version Control
* Postgresql
* Django

## Known Bugs  
* Still working on the App... Still has some bugs to be cleared

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

###### LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
