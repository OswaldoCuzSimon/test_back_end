# Test Back End
________
API that will provide useful information about restaurants to users

## Getting Started
________
### Prerequisites
install GDAL
~~~
sudo dnf install gdal -y
~~~
### Installing
Using virtualenv
~~~
virtualenv -p /usr/bin/python3.6 env
source activate env
pip install -r requirements.txt
~~~
configure PostgreSQL with Docker
~~~
docker run -e POSTGRES_PASSWORD=password -p 5432:5432 -d mdillon/postgis 
~~~
### Run
Rename environ.rc.temp file to environ.rc and replace values by real  values

First activate the virtualenv
~~~shell
source environ.rc
python manage.py makemigrations restaurant
python manage.py migrate restaurant
python manage.py runserver
~~~

### Load data 
~~~
wget -c https://s3-us-west-2.amazonaws.com/lgoveabucket/restaurantes.csv -O restaurantes.csv
python manage.py import_csv restaurantes.csv 
~~~

## Deployment
__________

### Heroku

Config Vars
~~~
BUILD_WITH_GEO_LIBRARIES=1
DISABLE_COLLECTSTATIC=1
~~~