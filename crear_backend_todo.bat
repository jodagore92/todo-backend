@echo off
echo ================================
echo Creando proyecto ToDo Backend
echo ================================

REM Carpetas principales
mkdir app
mkdir tests

REM Subcarpetas app
mkdir app\api
mkdir app\api\v1
mkdir app\core
mkdir app\models
mkdir app\schemas
mkdir app\services
mkdir app\db

REM Archivos base
type nul > app\main.py
type nul > app\api\v1\todos.py
type nul > app\core\config.py
type nul > app\models\todo.py
type nul > app\schemas\todo.py
type nul > app\services\todo_service.py
type nul > app\db\database.py
type nul > app\db\init_db.py

type nul > tests\test_todos.py

type nul > requirements.txt
type nul > .env

echo.
echo Proyecto creado correctamente ✔
echo Puedes empezar a trabajar en todo-backend
pause