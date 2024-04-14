FROM python:3.11
# у нас дизмараль, мультисборки не будет и пользака тоже не будет!

WORKDIR /data

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

# Указываем порт, на котором Gunicorn будет слушать
EXPOSE 8000

# Запускаем Gunicorn для приложения
#CMD ["tail", "-f", "/dev/null"]
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
#gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080