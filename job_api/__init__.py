import logging

from flask import Flask, Blueprint
from flask_restful import Api

from job_api.job_parser_resource import JobParserResource, \
    job_parser_resource_path

logger = logging.getLogger()

try:
    application = Flask(__name__)
    api_bp = Blueprint('api', __name__, url_prefix='/v1')
    api = Api(api_bp)

    api.add_resource(
        JobParserResource,
        job_parser_resource_path,
    )

    application.register_blueprint(api_bp)
except Exception as e:
    logger.exception(str(e))
