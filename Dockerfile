# our base image
FROM ubuntu:17.10

RUN apt-get update

RUN apt-get install -qyy \
    -o APT::Install-Recommends=false -o APT::Install-Suggests=false \
    python-virtualenv \
    python-pip \
    pypy \
    libffi6 \
    openssl \
    iputils-ping \
    openssh-server

    
# RUN pip install virtualenv
# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install -U pip setuptools 
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY frontend-service.log /usr/src/app/
COPY parse_logfile.py /usr/src/app/
COPY device.py /usr/src/app/
COPY connect_to_devices.py /usr/src/app/



