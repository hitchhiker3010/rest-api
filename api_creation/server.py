from flask import Flask, jsonify, request
from utils import price_calc

app = Flask(__name__)

@app.route("/checkout",methods=["POST"])
def api_call():
    """
    
    """
    item_list = request.get_json()
    cart_price = price_calc(item_list)
    resp = jsonify(price=cart_price)
    resp.headers["Content-Type"] = "application/json"
    resp.status_code = 200
    
    return resp

if __name__ == "__main__":
    app.run()
