from transformers import pipeline
from huggingsound import SpeechRecognitionModel
import pandas as pd
import os
import glob


class Classification:

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def get_transcriptions(self) -> dict:
        model = SpeechRecognitionModel(
            "jonatasgrosman/wav2vec2-large-xlsr-53-english")
        audio_path = [self.file_path]
        transcriptions = model.transcribe(audio_path)
        return transcriptions

    def generate_text_classification(self, text: str):
        classifications = pd.read_csv('IAB_classifications_v2.csv')
        candidate_labels = classifications['Tier 1'].to_list()

        candidate_labels = list(set(candidate_labels))

        classifier = pipeline('zero-shot-classification')
        labels = classifier(text, candidate_labels)

        filtered_t2_classifications = classifications.loc[classifications['Tier 1'].isin(
            labels['labels'][:5])]['Tier 2']

        labels = classifier(text, list(
            set(filtered_t2_classifications.to_list())))
        return labels['labels'][:5]

    def clean_up_tmp(self):
        files = glob.glob('tmp/*')
        for f in files:
            os.remove(f)

    def classifier(self):
        transcriptions_full = self.get_transcriptions()
        transcriptions_text = transcriptions_full[0]['transcription']

        classifications = self.generate_text_classification(
            transcriptions_text)

        body = {'file_name': self.file_name, 'classifications': classifications,
                'transcription': transcriptions_text}

        # clean_up_tmp()
        return body
