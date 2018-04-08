FROM ubuntu
ADD . /dockerfceuxonly
RUN apt-get dist-upgrade -y
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install scons libsdl1.2-dev subversion libgtk2.0-dev -y
RUN svn checkout http://svn.code.sf.net/p/fceultra/code/fceu/trunk ./fceultra
RUN yes | cp -rf /fceuxonly/cheat.cpp fceultra/src/cheat.cpp
WORKDIR /fceultra
RUN scons install
CMD ["fceux", "/fceuxonly/1942.zip"]

# Run with sudo docker run -ti --rm --device /dev/snd --group-add audio -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
