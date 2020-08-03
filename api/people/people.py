from flask import abort, Blueprint, Response, request, jsonify
from database.database import People
import logging
people = Blueprint('people', __name__)
logger = logging.getLogger()

@people.route("/people", methods=['GET', 'POST'])
def people_all():
    if request.method == 'POST':
        if request.headers.getlist('Content-Type') == ['application/json']:
            if(request.get_json() != None):
                People.add_user(request.get_json())
                return Response(status=201)
            else:
                abort(500)
        else:
            abort(400)
    elif request.method == 'GET':
        logger.info(People.get_users())
        return People.get_users()


@people.route("/people/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def people_id(id):
    if request.method == 'PUT':
        if request.headers.getlist('Content-Type') == ['application/json']:
            if(request.get_json() != None):
                if People.update_users_by_id(id) != None:
                    return 200
                else:
                    abort(404)
            else:
                abort(500)
        else:
            abort(400)
    elif request.method == 'DELETE':
        if People.delete_users_by_id(id) != None: 
            return jsonify(People.get_users_by_id(id))
        else:
            abort(404)
    elif request.method == 'GET':
        if People.get_users_by_id(id) != None: 
            return jsonify(People.get_users_by_id(id))
        else:
            abort(404)
