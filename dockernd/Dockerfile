FROM ubuntu:latest

# Add all files
ADD . dockernd

# Install setup python stuff
RUN apt-get update && apt-get install -y python3-pip python3-dev && pip3 install --upgrade pip && apt-get install -y python3-tk

RUN pip3 install -r /dockernd/requirements.txt

# Add fceux
RUN apt-get install scons libsdl1.2-dev subversion libgtk2.0-dev -y
RUN svn checkout http://svn.code.sf.net/p/fceultra/code/fceu/trunk ./fceultra
RUN yes | cp -rf /dockernd/cheat.cpp fceultra/src/cheat.cpp
WORKDIR /fceultra
RUN scons install

# Run with sudo docker run -ti --rm --device /dev/snd --group-add audio -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix

