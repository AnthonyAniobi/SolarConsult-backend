FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY /src/ /code/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver" ]