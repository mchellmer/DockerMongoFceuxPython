FROM ubuntu:latest

# Add all files
COPY . dockernd

# Install setup python stuff
RUN apt-get update && apt-get install -y python3-pip python3-dev && pip3 install --upgrade pip && apt-get install -y python3-tk

RUN pip3 install -r /dockernd/requirements.txt

# Add fceux
RUN apt-get install scons libsdl1.2-dev subversion libgtk2.0-dev -y
RUN yes | cp -rf /dockernd/cheat.cpp /dockernd/fceux223/src/cheat.cpp
WORKDIR dockernd/fceux223
RUN scons install

RUN mkdir ../../root/.fceux

RUN yes | cp ../../dockernd/python/ND/NostalgiaDrive/docs/config/fceux.cfg ../../root/.fceux/fceux.cfg
