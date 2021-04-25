t-mobs
=======



run | test
----------

    $ cd ~/
    $ git clone https://github.com/sdcasas/tmobs.git
    $ cd tmobs/src
    $ pip install -r src/requirements/local.txt
    $ # edit file config/settings/base.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'tmobs',
                'USER': 'tmobs',
                'PASSWORD': 'tmobs123',
                'HOST': 'localhost',
                'PORT': '3306',
                'OPTIONS': {
                    'sql_mode': 'traditional',
                }
            }
        }

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser    
    $ python manage.py runserver