# A Multi User Data Entry Application
This is a RESTful API for a multiuser data entry application.  
The API allows for multiple categories of data, including 
Health Institutions, Professional Details, and Event Details, with the option to a Custom Category where necessary. 

# Technologies and Libraries Used

Package/Library | Use-Case                                                         
----------------------- |------------------------------------------------------------------|
*Django REST Framework* | *API Endpoints*                                                  
*Insomnia*              | *Api Visualization tool*                                         
*Django TestCase*       | *The Django Test framework*                                      
*Sqlite3*               | *A light and hustle-free database*                               
*Python3.11*            | *Python version used*                                            
*Django*                | *Web Framework Used*                                             
*Black*                 | *The best formatting library for Python to avoid Tabs vs Spaces* 
  

# Setting up



Clone the project
----------------------
``` shell
git clone https://github.com/waWanjohi/data-entry.git
```
Set up your virtual environment
----------------------
``` shell
virtualenv venv 
```
Activate your virtual environment
----------------------
``` shell
source venv/bin/activate
```
Install the required packages
----------------------
``` shell
pip install -r requirements.txt --no-cache-dir
```


Migrate database updates
----------------------
``` shell
python manage.py migrate
```
Run Tests
----------------------
``` shell
python manage.py test

```
Start local server
----------------------
``` shell
python3 manage.py runserver
```
Link to Documentation
----------------------
``` shell
http://127.0.0.1:8000/docs/

```