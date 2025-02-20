from flask import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

creds = 100
flag = None
rations = {"2 oz. Water":10, "Clamato Juice":35, "Bowl of Gruel":100, "Literal Rubber":5}
rations = [["2 oz. Water",10,"/static/images/water.jpg"],["Clamato Juice",35,"/static/images/water.jpg"],["Bowl of Gruel",100,"/static/images/water.jpg"],["Literal Rubber",5,"/static/images/water.jpg"]]

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

@app.route('/', methods=['GET'])
def get_index():
    global creds, rations
    ration_prods = ''
    for r in rations:
        ration_prods += create_ration_html(r)
    return render_template('index.html', creds=creds, ration_products=ration_prods)

@app.route('/submit', methods=['POST'])
def submit():
    global creds
    print(request.json)
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    cost = 0
    # what awful programming
    for r in rations:
        if r[0] == name:
            cost = r[1]
    total = cost * quantity
    if total > creds:
        return jsonify({"message": "Not enough funds for ration. Perish."})
    creds -= total
    return jsonify({"message": f"'{name}' successfully purchased. You now have {creds} credits"})

@app.route('/feast', methods=['GET'])
def get_feast():
    if creds > 1000000:
        return render_template('feast.html', flag=flag)
    return render_template('bb.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=31337, debug=True)
