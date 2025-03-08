import os
import redis
import subprocess
from uuid import uuid4
from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

db_name = 'blog_comments.db'

app.config['SECRET_KEY'] = 'secret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# just for storing session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')

socketio = SocketIO(app)
db = SQLAlchemy(app)
server_session = Session(app)

with open("templates/server_code.py",'r') as inf:
    source = inf.read()

# jank, done in such a way that everyone has their own comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String)
    author = db.Column(db.String)
    comment = db.Column(db.String)

    def __init__(self, uuid, author, comment):
        self.uuid = uuid
        self.author = author
        self.comment = comment

@socketio.on('submit comment')
def handle_comment(data):
    new_record = Comment(session['uuid'], data['author'], data['comment'])
    db.session.add(new_record)
    db.session.commit()
    emit('new comment', broadcast=True)

# this just simulates the admin coming to your page
@socketio.on('waive admin')
def waive_admin():
    session_cookie = request.cookies.get('session')
    subprocess.run(['python3', 'admin.py', f'{session_cookie}'])

@app.route('/', methods=['GET'])
def news():
    if not session.get('uuid'):
        session['uuid'] = str(uuid4())
    comments = Comment.query.filter_by(uuid=session['uuid']).order_by(Comment.id).all()
    comment_list = []
    for comment in comments:
        comment_list.append("<p class=\"comment\"><strong>" + comment.author + ":</strong> " + comment.comment + "</p>")
    if 'flag' in request.cookies:
        return render_template('/news.html', comments=comment_list)
    else:
        resp = make_response(render_template('/news.html', comments=comment_list))
        resp.set_cookie('flag', 'if only you were the admin lol')
        return resp

@app.route('/source', methods=['GET'])
def show_source():
    response = make_response(source,200)
    response.mimetype = "text/plain"
    return response

if __name__=='__main__':
    app.run(host="0.0.0.0",port=31337)
