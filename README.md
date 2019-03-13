# Test Back End
API that will provide useful information about restaurants to users

## Installation

### Create virtual environment
using virtualenv
~~~
virtualenv -p /usr/bin/python3.6 env
source activate env
pip install -r requirements.txt
~~~
### Configure PostgreSQL
using Docker
~~~
docker run -e POSTGRES_DB=test_back_end \
    -e POSTGRES_USER=test_back_end \
    -e POSTGRES_PASSWORD=test_back_end \
    -e MAX_CONNECTIONS=1000 -p 5432:5432 -d postgres:9.6
~~~
### Run
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