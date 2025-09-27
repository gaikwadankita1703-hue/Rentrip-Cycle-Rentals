@echo off
echo Starting PedalPower Rentals Setup...
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setting up database...
python manage.py makemigrations
python manage.py migrate

echo.
echo Creating superuser and sample data...
python setup_project.py

echo.
echo Starting development server...
echo Visit: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin (admin/admin123)
echo.
python manage.py runserver

pause
