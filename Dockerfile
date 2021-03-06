
FROM python:3.10
#RUN mkdir /app
#WORKDIR "/app"

# Upgrade pip
RUN pip install --upgrade pip

# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD app/requirements.txt /app/
ADD app/main.py /app/

ADD app/classes app/classes/
ADD app/helper app/helper/
ADD app/repository app/repository/
ADD app/views app/views/

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD [ "python", "app/main.py" ]