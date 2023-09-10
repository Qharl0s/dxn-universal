#!bin/bash

echo "Creando el projecto..."
python3.9 -m pip install -r requirements.txt

echo "Iniciando migraciones.."

python3.exe .\manage.py makemigrations --noinput
python3.exe .\manage.py migrate --noinput

echo "Colecciones estaticas.."
python3.exe .\manage.py collectstatic --noinput --clear
