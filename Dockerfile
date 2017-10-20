# Builds an image for SAM celery worker

#FROM python:3
FROM quanted/qed_py3

# Install requirements for SAM Celery
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Copy the project code
COPY . /src/
WORKDIR /src