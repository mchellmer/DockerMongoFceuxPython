# Get and prepair a ubuntu image
FROM ubuntu
EXPOSE 27017
ADD . /dockermongoonly
RUN apt-get dist-upgrade -y
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe

# Add python and pip
RUN apt-get update && apt-get install python3 -y
RUN apt-get update && apt-get install python3-pip -y
RUN apt-get upgrade -y

# Add mongodb
RUN apt-get update && apt-get install mongodb -y

#  Get dependencies and kickstart mongdodb
WORKDIR /dockermongoonly
RUN pip3 install -r requirements.txt
RUN rm /var/lib/mongodb/mongod.lock || true
RUN mkdir -p /data/db/
RUN chown `id -u` /data/db
RUN mongod --repair
RUN service mongodb start
RUN service mongodb status

# Run pymongo app
CMD ["python3", "mImport.py"]

# Run and it should print out the the lines from nesGamesfinal.tsv as they are in the mongodb
