#vollov.ca

##About
web site vollov.ca

## versions
1.0 - [anguarjs] static web page with nodejs and angularjs
2.0 - [java] Java implementation with spring, hibernate and twitter-bootstrap

gunicorn --workers=2 vollov.wsgi:application

python manage.py run_gunicorn
--debug


You can use the –env option to set the path to load the settings. In case you need it you can also add your application path to PYTHONPATH using the –pythonpath option:

manage.py collectstatic
$ gunicorn --env DJANGO_SETTINGS_MODULE=vollov.settings vollov.wsgi --daemon -b :7005

