import sys
from src import WhisperAudioTranscriber, MarianTranslator, SRTFormatter, FileHandler


class AudioTranscriber:
    def __init__(self, model_size):
        self.transcriber = WhisperAudioTranscriber(model_size)
        self.mariantranslator = MarianTranslator()
        self.formatter = SRTFormatter()
        self.filehandler = FileHandler()

    def input_processing(self, input_path):
        audio_files = self.filehandler.get_audio_files(input_path)
        for file in audio_files:
            self.process_file(file)

    def process_file(self, audio_file):
        print(f"Processing {audio_file}")
        result = self.transcriber.transcribe(audio_file)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [path] [model size (medium/large ect.)]")
        sys.exit()
    input_path = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "medium"
    creator = AudioTranscriber(model_size)
    creator.input_processing(input_path)


if __name__ == "__main__":
    main()
