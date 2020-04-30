#!/usr/bin/python3
""" Module for State objects that handles all defaults RestFul API """
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, request, abort


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """ Method that retrieves the list of all State objects """
    if request.method == 'GET':
        states = storage.all(State)
        var = []
        for value in states.values():
            var.append(value.to_dict())
        return jsonify(var)
    if request.method == 'POST':
        info = request.get_json()
        if info is None:
            abort(400, 'Not a JSON')
        if 'name' not in info:
            abort(400, 'Missing name')
        state = State(**info)
        state.save()
        return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['DELETE', 'GET'])
def del_states(state_id):
    """ Method that delets a State object """
    if request.method == 'DELETE':
        states = storage.get(State, state_id)
        if states:
            storage.delete(states)
            storage.save()
            return jsonify({}), 200
        abort(404)
    if request.method == 'GET':
        states = storage.get(State, state_id)
        if states:
            return jsonify(states.to_dict())
        abort(404)


@app_views.route('/states/<state_id>', methods=['PUT'])
def put_states(state_id):
    """ Method that updates a State object """
    states = storage.get(State, state_id)
    if states:
        if request.is_json is False:
            abort(400, 'Not a JSON')
        info = request.get_json()
        states.update(info)
        return jsonify(states.to_dict())
    abort(404)
