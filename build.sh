
set -o errexit

cd django_blog
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
