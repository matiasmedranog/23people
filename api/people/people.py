from flask import abort, Blueprint, request
import logging
people = Blueprint('people', __name__)
logger = logging.getLogger()

@people.route("/", methods=['GET', 'POST'])
def people_all():
    if request.method == 'POST':
        logger.info(request.headers.getlist('Content-Type'))
        if request.headers.getlist('Content-Type') == 'application/json':
            logger.info("POST users")
            return "POST"
        else:
            abort(400)
    else:
        logger.info("Getting all users")
        return "Hi"


@people.route("/<int:id>", methods=['GET', 'POST'])
def people_id(id):
    if request.method == 'GET':
        logger.info("ID: "+str(id))
        #if(request.get_json()):
    return "ID: "+str(id)
