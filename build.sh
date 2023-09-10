#!bin/bash

echo "Creando el projecto..."
python3.9 -m pip install -r requirements.txt

echo "Iniciando migraciones.."

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Colecciones estaticas.."
python3.9 manage.py collectstatic --noinput --clear
