"""
Cities controller module
"""

from flask import request, abort, jsonify
from src.models.city import City
from flask_jwt_extended import jwt_required
from src.controllers.login import check_admin


def get_cities():
    """Returns all cities"""
    cities: list[City] = City.get_all()

    return [city.to_dict() for city in cities]

@jwt_required()
def create_city():
    """Creates a new city"""
    if check_admin() == True:
        data = request.get_json()

        try:
            city = City.create(data)
        except KeyError as e:
            abort(400, f"Missing field: {e}")
        except ValueError as e:
            abort(400, str(e))

        return city.to_dict(), 201
    else: 
        return jsonify({'msg': 'Not allowed'})     


def get_city_by_id(city_id: str):
    """Returns a city by ID"""
    city: City | None = City.get(city_id)

    if not city:
        abort(404, f"City with ID {city_id} not found")

    return city.to_dict()


def update_city(city_id: str):
    """Updates a city by ID"""
    data = request.get_json()

    try:
        city: City | None = City.update(city_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not city:
        abort(404, f"City with ID {city_id} not found")

    return city.to_dict()

@jwt_required()
def delete_city(city_id: str):
    """Deletes a city by ID"""
    if check_admin() == True:
        if not City.delete(city_id):
            abort(404, f"City with ID {city_id} not found")

        return "", 204
    else:
        return jsonify({'msg': 'Not allowed'})
