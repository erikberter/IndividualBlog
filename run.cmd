python manage.py migrate --settings=config.settings.base
python manage.py collectstatic --settings=config.settings.base
python manage.py runserver --settings=config.settings.base