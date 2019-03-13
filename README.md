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

### Run
First activate the virtualenv
~~~shell
python manage.py makemigrations restaurant
python manage.py migrate restaurant
python manage.py runserver
~~~