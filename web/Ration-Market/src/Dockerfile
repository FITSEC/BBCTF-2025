FROM debian:bullseye

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get update -y && apt-get install -y python3 python3-pip
RUN python3 -m pip install flask flask_limiter \
    gevent-websocket eventlet==0.30.2 gunicorn

ADD /app /app

CMD chmod +x /app/start.sh

RUN useradd -m web; chown -R web /app
EXPOSE 31337/TCP
WORKDIR /app
ENTRYPOINT ["bash", "start.sh"]
