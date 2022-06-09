import boto3
import os
import glob
import os
from cloudpathlib import CloudPath
from huggingsound import (
    TrainingArguments,
    ModelArguments,
    SpeechRecognitionModel,
    TokenSet,
)

# https://github.com/jonatasgrosman/huggingsound


class TranscriptionRefinement:
    def __init__(self, mp3_file_path, file_transcription):
        self.mp3_file_path = mp3_file_path
        self.file_transcription = file_transcription

    session = boto3.Session(
        aws_access_key_id="",
        aws_secret_access_key="",
    )
    s3 = session.resource("s3")

    try:
        BUCKET_NAME = "mlops-huggingsound-models/models/"
        cp = CloudPath(BUCKET_NAME)
        cp.download_to("models/")
    except:
        model = SpeechRecognitionModel("facebook/wav2vec2-large-xlsr-53")

    output_dir = "models/"

    tokens = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "'",
    ]
    token_set = TokenSet(tokens)

    training_args = TrainingArguments(
        learning_rate=3e-4,
        max_steps=1000,
        eval_steps=200,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        overwrite_output_dir=True,
    )
    model_args = ModelArguments(
        activation_dropout=0.1,
        hidden_dropout=0.1,
    )

    train_data = [
        {
            "path": "~/Downloads/test_audio.mp3",
            "transcription": "The quick brown fox jumps over the lazy dog",
        },
    ]

    try:
        model.finetune(
            output_dir,
            train_data=train_data,
            token_set=token_set,
        )
    except:

        files = glob.glob("models/*")
        for f in files:
            os.remove(f)
        model.finetune(
            output_dir,
            train_data=train_data,
            token_set=token_set,
        )

        model.finetune(
            output_dir,
            train_data=train_data,
            token_set=token_set,
        )
