# Base image
FROM python:3.7

# Maintainer
MAINTAINER David Laganière

# Create app directory
RUN mkdir -p /squoia_api
WORKDIR /sequoia_api

# Install dependencies
#RUN pip install gunicorn django decouple
COPY Pipfile Pipfile.lock /sequoia_api/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the application folder inside the container
COPY . /sequoia_api

# Expose the port
EXPOSE 8000
 
CMD ["gunicorn", "--bind", ":8000", "sequoia.wsgi:application"]
