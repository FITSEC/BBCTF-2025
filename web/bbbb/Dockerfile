FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt update -y && apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.11 python3-pip python3-venv sqlite3 redis python-is-python3 wget chromium
RUN python3 -m venv /app/venv
ENV OLDPATH "$PATH"
ENV PATH "/app/venv/bin:$PATH"
RUN pip install flask flask_socketio flask_limiter flask_sqlalchemy flask_session redis \
    werkzeug selenium webdriver-manager gevent-websocket eventlet gunicorn pyppeteer
RUN pyppeteer-install
RUN pip install cement==2.10.14
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt update 
RUN apt install google-chrome-stable -y
ADD /app /app

CMD chmod +x /app/start.sh

RUN useradd -m web; chown -R web /app
EXPOSE 31337/TCP
WORKDIR /app
ENTRYPOINT ["bash", "start.sh"]
