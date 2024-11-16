from flask import Blueprint, request, jsonify
from app.database import db_session
from app.models import SeasonalFlavor, Ingredient, CustomerSuggestion

bp = Blueprint('api', __name__)

@bp.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'GET':
        flavors = db_session.query(SeasonalFlavor).all()
        return jsonify([{"id": f.id, "name": f.name, "description": f.description, "is_available": f.is_available} for f in flavors])
    elif request.method == 'POST':
        data = request.json
        new_flavor = SeasonalFlavor(name=data['name'], description=data.get('description', ''), is_available=data.get('is_available', True))
        db_session.add(new_flavor)
        db_session.commit()
        return jsonify({"message": "Flavor added successfully!"}), 201

@bp.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'GET':
        ingredients = db_session.query(Ingredient).all()
        return jsonify([{"id": i.id, "name": i.name, "quantity": i.quantity, "low_stock_threshold": i.low_stock_threshold} for i in ingredients])
    elif request.method == 'POST':
        data = request.json
        new_ingredient = Ingredient(name=data['name'], quantity=data['quantity'], low_stock_threshold=data.get('low_stock_threshold', 10))
        db_session.add(new_ingredient)
        db_session.commit()
        return jsonify({"message": "Ingredient added successfully!"}), 201

@bp.route('/suggestions', methods=['POST'])
def suggestions():
    data = request.json
    new_suggestion = CustomerSuggestion(suggestion=data['suggestion'], allergy_concern=data.get('allergy_concern'))
    db_session.add(new_suggestion)
    db_session.commit()
    return jsonify({"message": "Suggestion added successfully!"}), 201
