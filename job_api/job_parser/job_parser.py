import re
from typing import Dict

from bs4 import BeautifulSoup


class JobParser:
    def __init__(
            self,
            nlp_model,
            category_model,
            label_to_category: Dict[str, str],
    ):
        self.nlp_model = nlp_model
        self.category_model = category_model
        self.label_to_category = label_to_category

    def process(
            self,
            title: str,
            description: str,
    ) -> Dict[str, str]:
        soup = BeautifulSoup(description, features='html.parser')
        clean_description = soup.get_text(separator=' ')

        text = (title + ' ') * 5 + clean_description

        result = {}

        result.update(self.get_job_category(text))

        result.update(self.get_nlp_data(text))

        result.update(self.get_emails(text))

        return result

    def get_job_category(self, text):
        res = self.category_model.predict([text])
        return {'Category': self.label_to_category[str(res[0])]}

    def get_nlp_data(self, text: str) -> Dict[str, str]:
        spacy_accepted_entity_types = {
            'PERSON': 'Person',
            'GPE': 'Location',
            'ORG': 'Company',
            'MONEY': 'Salary',
        }

        result = {v: None for v in spacy_accepted_entity_types.values()}

        doc = self.nlp_model(text)
        for entity in doc.ents:
            if entity.label_ not in spacy_accepted_entity_types.keys():
                continue
            else:
                result[spacy_accepted_entity_types[entity.label_]] = entity.orth_

        return result

    def get_emails(self, text):
        emails = re.findall(
            r'[\w\.-]+@[\w\.-]+\.[\w-]+',
            text
        ) or None
        return {'E-mails': emails}
