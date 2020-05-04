#!/usr/bin/python3
""" Module for State objects that handles all defaults RestFul API """
from api.v1.views import app_views
from models.city import City
from models.state import State
from models import storage
from flask import jsonify, request, abort


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def cities(state_id):
    """ Method that retrieves the list of all State objects """
    if request.method == 'GET':
        states = storage.get(State, state_id)
        if states:
            print(states)
        else:
            abort(404)
        cities = [city.to_dict() for city in states.cities]
        return jsonify(cities)

    if request.method == 'POST':
        states = storage.get(State, state_id)
        if states is None:
            abort(404)
        info = request.get_json()
        info['state_id'] = state_id
        if info is None:
            abort(400, 'Not a JSON')
        if 'name' not in info:
            abort(400, 'Missing name')
        city = City(**info)
        city.save()
        return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['DELETE', 'GET'])
def del_cities(city_id):
    """ Method that deletes a State object """
    if request.method == 'DELETE':
        cities = storage.get(City, city_id)
        if cities:
            storage.delete(cities)
            storage.save()
            return jsonify({}), 200
        abort(404)

    if request.method == 'GET':
        cities = storage.get(City, city_id)
        if cities:
            return jsonify(cities.to_dict())
        abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def put_cities(city_id):
    """ Method that updates a State object """
    cities = storage.get(City, city_id)
    if cities:
        if request.is_json is False:
            abort(400, 'Not a JSON')
        info = request.get_json()
        cities.update(info)
        return jsonify(cities.to_dict())
    abort(404)
