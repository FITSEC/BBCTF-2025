import os
import subprocess
from uuid import uuid4
from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO, emit

app = Flask(__name__)

limiter = Limiter(
	get_remote_address,
	app=app,
	default_limits=["30 per minute"]
)

app.config['SECRET_KEY'] = 'flask secret'

socketio = SocketIO(app)

comments = []

@socketio.on('submit comment')
def handle_comment(data):
	comments.append("<p class=\"comment\"><strong>" + data['author'] + ":</strong> " + data['comment'] + "</p>");
	emit('new comment', broadcast=True)

# this just simulates the admin coming to your page
@socketio.on('waive admin')
def waive_admin():
	subprocess.run(['python','admin.py'])

@app.route('/', methods=['GET'])
def news():
	if 'flag' in request.cookies:
		return render_template('/news.html', comments=comments)
	else:
		resp = make_response(render_template('/news.html', comments=comments))
		resp.set_cookie('flag','if only you were the admin lol')
		return resp

@app.route('/source',methods=['GET'])
def show_source():
	return render_template('server_code.py')

if __name__=='__main__':
	app.run(host="0.0.0.0",port=31337)
