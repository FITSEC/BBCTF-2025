from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# TODO: funnify
prole_text = ['1','2','3','4']

proles = 'User-agent: *\n\nDisallow: /government-secrets'

@app.route('/', methods=['GET'])
def index():
    resp = make_response(render_template('/index.html'))
    if 'IsBigBrother' not in request.cookies:
        resp.set_cookie('IsBigBrother','False')
    return resp

@app.route('/get-slogans', methods=['POST'])
def get_slogans():
    if 'IsBigBrother' in request.cookies:
        if request.cookies['IsBigBrother'] == 'True':
            # TODO: Put actual flag lol
            prole_text.append('Flag 2: bbctf{pr4is3_0c34ni4_0h_ri9h730u5_13ad3r!}')
    return jsonify(prole_text)

@app.route('/proles.txt')
def get_proles():
    return render_template('proles.txt')

@app.route('/government-secrets', methods=['GET'])
def get_gov_secrets():
    return render_template('/government-secrets.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=31337)
