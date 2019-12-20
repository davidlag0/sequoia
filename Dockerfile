# Base image
FROM python:3.7-alpine

# Create app directory
RUN mkdir -p /sequoia_api
WORKDIR /sequoia_api

# Copy the application folder inside the container and install dependencies
#COPY Pipfile Pipfile.lock /sequoia_api/
COPY . /sequoia_api
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Create symlink to secrets.
RUN ln -s /run/secrets/django_secrets .env

# Expose the port
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sequoia.wsgi:application"]
