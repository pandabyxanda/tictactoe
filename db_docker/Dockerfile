FROM sqlite3



## Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
#ENV PYTHONUNBUFFERED 1
#
##ENV DJANGO_ALLOWED_HOSTS 45.8.251.243 перенес в докер композе
#
## Устанавливает рабочий каталог контейнера — "app"
#WORKDIR /app/
#
## Копирует все файлы из нашего локального проекта в контейнер
#ADD . /app/
#
## Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
##RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
#
#EXPOSE 8000
#
##CMD ["gunicorn", "tictactoe.wsgi", "0.0.0.0:8000"]
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



#python manage.py runserver 127.0.0.1:8000
#docker network inspect -f '{{json .Containers}}' 9f6bc3c15568 | jq '.[] | .Name + ":" + .IPv4Address'
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 75000c343eb7
