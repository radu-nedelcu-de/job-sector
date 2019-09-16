from flask_restful import Resource, reqparse, abort

from job_api.job_parser import nlp_model, category_model, label_to_category
from job_api.job_parser.job_parser import JobParser

job_parser_resource_path = '/job_parser'

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, location='json', required=True)
post_parser.add_argument('description', type=str, location='json',
                         required=True)


class JobParserResource(Resource):
    def __init__(self):
        self.job_parser = JobParser(
            nlp_model=nlp_model,
            category_model=category_model,
            label_to_category=label_to_category,
        )

    def post(self):
        args = post_parser.parse_args()
        title = args.get('title')
        description = args.get('description')
        try:
            return self.job_parser.process(
                title=title,
                description=description
            )
        except ValueError as e:
            abort(400, description=e)
