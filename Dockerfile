FROM python:3.10

# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

#ENV DJANGO_ALLOWED_HOSTS 45.8.251.243 перенес в докер композе

# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app/

# Копирует все файлы из нашего локального проекта в контейнер
ADD . /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]







# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

#
#EXPOSE 8000
#
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tictactoe.wsgi"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tictactoe.wsgi"]

#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' e36260aa7314
