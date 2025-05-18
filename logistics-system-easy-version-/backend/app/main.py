from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", "sqlite:///../database/logistics.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    volume = db.Column(db.Float)
    weight = db.Column(db.Float)
    notes = db.Column(db.Text)
    date = db.Column(db.String(10))  # YYYY-MM-DD

@app.route('/api/goods', methods=['POST'])
def add_good():
    data = request.json
    good = Good(**data)
    db.session.add(good)
    db.session.commit()
    return jsonify({"message": "货物添加成功"}), 201

@app.route('/api/goods', methods=['GET'])
def list_goods():
    goods = Good.query.all()
    return jsonify([{
        "id": g.id,
        "name": g.name,
        "manufacturer": g.manufacturer,
        "quantity": g.quantity,
        "volume": g.volume,
        "weight": g.weight,
        "notes": g.notes,
        "date": g.date
    } for g in goods])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
