import whisper


class WhisperAudioTranscriber:
    def __init__(self, model_size):
        self.model = None
        self.model_size = model_size

    def load_model(self):
        self.model = whisper.load_model(self.model_size, device="cpu")

    def transcribe(self, file_path):
        if not self.model:
            self.load_model()
        return self.model.transcribe(file_path, language="ja", verbose=True)
