# Base image
FROM python:3.7-alpine

# Create app directory
RUN mkdir -p /sequoia_api
WORKDIR /sequoia_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY Pipfile Pipfile.lock /sequoia_api/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the application folder inside the container
COPY . /sequoia_api
RUN ln -s /run/secrets/django_secrets .env

# Expose the port
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sequoia.wsgi:application"]
