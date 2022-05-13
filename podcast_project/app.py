from transformers import pipeline
from huggingsound import SpeechRecognitionModel
import pandas as pd
import s3fs
import os
import glob
from dotenv import load_dotenv
import boto3


load_dotenv()
os.environ["AWS_ACCESS_KEY_ID"] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv('AWS_SECRET_ACCESS_KEY')


def get_transcriptions(file_path: str) -> pd.DataFrame:
    model = SpeechRecognitionModel(
        "jonatasgrosman/wav2vec2-large-xlsr-53-english")
    audio_path = [file_path]
    transcriptions = model.transcribe(audio_path)
    return transcriptions


def generate_text_classification(text: str):
    classifcations = pd.read_csv(os.getenv('IAB_CLASSIFICATION_FILE_PATH'))
    canidate_labels = classifcations['Tier 1'].to_list()

    canidate_labels = list(set(canidate_labels))

    classifier = pipeline('zero-shot-classification')
    labels = classifier(text, canidate_labels)

    filtered_t2_classifcations = classifcations.loc[classifcations['Tier 1'].isin(
        labels['labels'][:5])]['Tier 2']

    labels = classifier(text, list(set(filtered_t2_classifcations.to_list())))
    return labels['labels'][:5]


def clean_up_tmp():
    files = glob.glob('/tmp/*')
    for f in files:
        os.remove(f)


if __name__ == "__main__":

    s3 = boto3.client('s3', aws_access_key_id=os.getenv(
        'AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    # s3.download_file('podcast-audio-files-demo',
    #                 'ListenNotes.com-XauZDEjNsyS-1652461854.mp3', 'tmp/ListenNotes.com-XauZDEjNsyS-1652461854.mp3')

    file_path = 'tmp/ListenNotes.com-XauZDEjNsyS-1652461854.mp3'
    transcriptions_full = get_transcriptions(file_path)
    transcriptions_text = transcriptions_full[0]['transcription']

    classifications = generate_text_classification(transcriptions_text)

    body = {'file_name': file_path, 'classifications': classifications,
            'transcription': transcriptions_text}

    print(body)
