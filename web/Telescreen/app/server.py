from flask import *
from uuid import uuid4
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

prole_text = ['YOU MUST NOT MAKE FUN OF MARCUS FELICIANO','YOU MUST WEAR YOUR GOVERNMENT MANDATED PROGRAMMER SOCKS AND CAT EARS','DO NOT CALL LUIS ABRAHAM THE PHRASE "VICTIM WEIGHT"','THE DUCKS IN THE ACADEMIC QUAD ARE NOT FREE, DO NOT PICK THEM UP, DO NOT TAKE THEM HOME']
with open('secret.txt', 'r') as s:
    app.config['SECRET_KEY'] = s.read()
text_map = {}

proles = 'User-agent: *\nDisallow: /government-secrets'

def get_user():
    global prole_text
    user_id = None
    if not 'user_id' in session:
        user_id = uuid4()
        session['user_id'] = user_id
        text_map[user_id] = prole_text.copy()
    else:
        user_id = session['user_id']
        if user_id not in text_map:
            user_id = uuid4()
            session['user_id'] = user_id
            text_map[user_id] = prole_text.copy()
    return user_id

@app.route('/', methods=['GET'])
def index():
    resp = make_response(render_template('/index.html'))
    user_id = get_user()
    if 'IsBigBrother' not in request.cookies:
        resp.set_cookie('IsBigBrother','False')
    return resp

@app.route('/get-slogans', methods=['POST'])
def get_slogans():
    global text_map
    user_id = get_user()
    if 'IsBigBrother' in request.cookies:
        if request.cookies['IsBigBrother'] == 'True':
            if 'bbctf' not in text_map[user_id]:
                [text_map[user_id].insert(i,'Flag 2: bbctf{pr4is3_0c34ni4_0h_ri9h730u5_13ad3r!}') for i in range(len(prole_text)-1, -1, -1) if i % 2 == 0]
    return jsonify(text_map[user_id])

@app.route('/proles.txt')
def get_proles():
    get_user()
    return render_template('proles.txt')

@app.route('/government-secrets', methods=['GET'])
def get_gov_secrets():
    get_user()
    return render_template('/government-secrets.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=31337)
