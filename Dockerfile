# Base image
FROM python:3.8-alpine

# Create app directory
RUN mkdir -p /sequoia_api
WORKDIR /sequoia_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
#
# It would be best to delete unused dependencies as much as possible but Python seems to
# dynamically link with the PostgreSQL libraries. Thus, I decided to just keep all dependencies
# in the image for now.
#
COPY Pipfile Pipfile.lock /sequoia_api/
#RUN apk add --no-cache --virtual .build-deps \
RUN apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile
#    && apk del --no-cache .build-deps

# Copy the application folder inside the container
COPY . /sequoia_api
RUN ln -s /run/secrets/django_secrets .env

# Expose the port
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--log-level=info", "--access-logfile=-", "--error-logfile=-", "sequoia.wsgi:application"]
