Создаем виртуальное окружение:
```python3 -m venv imgvenv```
Переходим в виртуальное окружение
```source imgvenv/bin/activate```   
Обновляем загрузчик зависимостей
```python3 -m pip install --upgrade pip```  
Обновляем зависимости
```pip3 install -r requirements.txt```   
Создаем миграцию в БД
```python3 manage.py makemigrations```
Проводим миграцию в БД
```python3 manage.py migrate```   
Обновляем статичные файлы
```python3 manage.py collectstatic```
Создаем суперюзера
```python3 manage.py createsuperuser```
Запускаем сервер
```python3 manage.py runserver```           
