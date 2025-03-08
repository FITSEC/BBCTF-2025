su -c "redis-server &
PATH="/app/venv/bin:$PATH"
pyppeteer-install
gunicorn -k eventlet --access-logfile - -b 0.0.0.0:31337 --thread 50 server:app" web
