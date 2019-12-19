# Base image
FROM python:3.8-alpine

# Maintainer
MAINTAINER David Laganière

# Create app directory
RUN mkdir -p /sequoia_api
WORKDIR /sequoia_api

# Expose the port
EXPOSE 8000

# Install dependencies
COPY Pipfile Pipfile.lock /sequoia_api/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the application folder inside the container
COPY . /sequoia_api
RUN ln -s /run/secrets/django_secrets .env
COPY ./config/temp_vars .env

# Update static files
RUN python manage.py collectstatic --no-input
RUN rm .env
 
CMD ["gunicorn", "--bind", ":8000", "sequoia.wsgi:application"]
