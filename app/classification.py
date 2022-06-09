from transformers import pipeline
from datetime import datetime
import pandas as pd
import os
import logging


class Classification:

    def __init__(self, transcribed_test):
        self.transcribed_test = transcribed_test
        

    def _generate_text_classification(self, text: str):
        start = datetime.now()
        logging.info('Generate Text Classification called')
        classifications = pd.read_csv('app/IAB_classifications_v2.csv')
        candidate_labels = classifications['Tier 1'].to_list()

        candidate_labels = list(set(candidate_labels))

        classifier = pipeline('zero-shot-classification')
        labels = classifier(text, candidate_labels)

        filtered_t2_classifications = classifications.loc[classifications['Tier 1'].isin(
            labels['labels'][:5])]['Tier 2']

        labels = classifier(text, list(
            set(filtered_t2_classifications.to_list())))
        logging.info('Text classification generated in {}'.format(
            datetime.now()-start))
        return labels['labels'][:5]



    def classifier(self):
        logging.info('Classifier called')

        classifications = self._generate_text_classification(
            self.transcribed_test)

        return classifications


