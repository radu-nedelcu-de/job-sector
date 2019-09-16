import json

import en_core_web_lg
from sklearn.externals import joblib

nlp_model = en_core_web_lg.load()

category_model = joblib.load('job_api/job_parser/model.hdf5')

label_to_category = json.load(
    open('job_api/job_parser/label_to_category.json')
)
