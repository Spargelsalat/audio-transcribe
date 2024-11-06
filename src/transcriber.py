"""
transcriber.py

This module handles the transcription of audio using OpenAI's Whisper model.
It loads the appropriate Whisper model and provides a method to transcribe audio files.
"""

import whisper


class WhisperAudioTranscriber:
    """
    A class responsible for transcribing audio using the Whisper model.

    Attributes:
        model_size (str): The size of the Whisper model to use.
        model (whisper.Whisper): The loaded Whisper model.
    """

    def __init__(self, model_size):
        self.model = None
        self.model_size = model_size

    def load_model(self):
        """
        Loads the Whisper model with the specified model size.
        """
        self.model = whisper.load_model(self.model_size, device="cpu")

    def transcribe(self, file_path):
        """
        Transcribes the given audio file.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            dict: The transcription result containing text and timing segments.
        """
        if not self.model:
            self.load_model()
        return self.model.transcribe(file_path, language="ja", verbose=True)
