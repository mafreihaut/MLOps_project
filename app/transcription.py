from huggingsound import SpeechRecognitionModel
from datetime import datetime
import os
import pandas as pd
import logging


class Transcription:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def _make_transcriptions(self) -> dict:
        model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")
        transcriptions = model.transcribe([self.file_path])
        return transcriptions

    def _clean_up_file(self, file_name):
        logging.info("tmp folder cleaned up")
        os.remove(file_name)

    def transcriber(self):
        start = datetime.now()
        logging.info("Get transcriptions called")
        transcriptions = self._make_transcriptions()
        transcriptions_text = transcriptions[0]["transcription"]

        logging.info("Transcriptions generated in {}".format(datetime.now() - start))
        self._clean_up_file(self.file_path)

        return transcriptions_text
