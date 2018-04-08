FROM python:3
ADD . /app
WORKDIR /app
CMD ["python3","app.py"]

# Run with sudo docker run -ti --rm --device /dev/snd --group-add audio -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
