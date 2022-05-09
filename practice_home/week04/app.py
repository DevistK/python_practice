from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['order_database']


@app.route('/')
def index():
    return render_template('itemview.html')


@app.route('/orderConfirm', methods=['POST'])
def orderPost():
    order_name = request.form['name']
    order_address = request.form['address']
    order_number = request.form['number']
    order_ea = request.form['ea']

    data = {
        'od_name': order_name,
        'od_address': order_address,
        'od_num': order_number,
        'od_ea': order_ea,
        'od_date': datetime.datetime.utcnow()
    }

    db.orders.insert_one(data)

    return jsonify({
        'flag': 'success',
    })


@app.route('/orderConfirm', methods=['GET'])
def orderGet():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({
        'flag': 'success',
        'orders': orders
    })


if __name__ == '__main__':
    app.run()
