# Base image
FROM python:3.7

# Maintainer
MAINTAINER David Laganière

# Create app directory
RUN mkdir -p /sequoia_api
WORKDIR /sequoia_api

# Install dependencies
COPY Pipfile Pipfile.lock /sequoia_api/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the application folder inside the container
COPY . /sequoia_api

# For static files
RUN python manage.py collectstatic

# Expose the port
EXPOSE 8000
 
CMD ["gunicorn", "--bind", ":8000", "sequoia.wsgi:application"]
