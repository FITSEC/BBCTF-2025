from flask import *
from uuid import uuid4
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
cred_map = {}

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

max_creds = 100
flag = None
rations = [["2 oz. Water",10,"/static/images/water.jpg"],["Clamato Juice",35,"/static/images/clamato.jpg"],["Bowl of Gruel",100,"/static/images/gruel.jpg"],["Literal Rubber",5,"/static/images/rubber.avif"]]
with open('secret.txt', 'r') as s:
    app.config['SECRET_KEY'] = s.read()

with open('flag.txt', 'r') as f:
    flag = f.read()

def create_ration_html(ration):
    return f'''
        <div class="product">
            <p class="name"><b>{ration[0]}</b></p>
            <img src="{ration[2]}" alt="{ration[2].split('/')[-1]}">
            <p>Price: {ration[1]} credits</p>
            <div class="controls">
                <button class="minus">-</button>
                <span class="quantity">1</span>
                <button class="plus">+</button>
            </div>
            <button class="buy-btn">Buy</button>
        </div>
    '''

def get_user():
    global cred_map
    user_id = None
    if not 'user_id' in session:
        user_id = uuid4()
        session['user_id'] = user_id
        cred_map[user_id] = max_creds
    else:
        user_id = session['user_id']
        if user_id not in cred_map:
            user_id = uuid4()
            session['user_id'] = user_id
            cred_map[user_id] = max_creds
    return user_id

@app.route('/', methods=['GET'])
def get_index():
    global cred_map, rations
    user_id = get_user()
    ration_prods = ''
    for r in rations:
        ration_prods += create_ration_html(r)
    return render_template('index.html', creds=cred_map[user_id], ration_products=ration_prods)

@app.route('/submit', methods=['POST'])
def submit():
    global cred_map
    user_id = get_user()
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    cost = 0
    # what awful programming
    for r in rations:
        if r[0] == name:
            cost = r[1]
    total = cost * quantity
    if total > cred_map[user_id]:
        return jsonify({"message": "Not enough funds for ration. Perish.", "creds": cred_map[user_id]})
    cred_map[user_id] -= total
    return jsonify({"message": f"'{name}' successfully purchased. You now have {cred_map[user_id]} credits.", "creds": cred_map[user_id]})

@app.route('/feast', methods=['GET'])
def get_feast():
    user_id = get_user()
    if cred_map[user_id] > 1000000:
        return render_template('feast.html', flag=flag)
    return render_template('bb.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=31337, debug=True)
