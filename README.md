# Django-Cassandra

# Installation

pip install django-cassandra-engine

# Include in settings.py file

INSTALLED_APPS = [
    ...
    ...
    'django_cassandra_engine',
]

# Database connection in settings.py 

Simple Strategy

DATABASES = {
    'default': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': 'vehicle_info',
        'TEST_NAME': 'test_vehicle_info',
        'HOST': 'localhost',
        'OPTIONS': {
            'replication': {
                'strategy_class': 'SimpleStrategy',
                'replication_factor': 1
            }
        }
    }
}

##

define your model in models.py and then run the command python manage.py sync_cassandra