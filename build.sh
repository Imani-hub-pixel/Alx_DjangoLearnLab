
set -o errexit


cd django_blog

# Install dependencies
pip install -r requirements.txt


python manage.py migrate


python manage.py collectstatic --noinput
