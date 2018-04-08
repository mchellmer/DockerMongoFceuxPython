FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip python3-dev && pip3 install --upgrade pip && apt-get install -y python3-tk

ADD . /dockerUbuntuPython
WORKDIR /app

CMD ["python3", "app.py"]

# Run with sudo docker run -ti --rm --device /dev/snd --group-add audio -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix

