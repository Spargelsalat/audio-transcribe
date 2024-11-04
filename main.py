import sys
from src import WhisperAudioTranscriber, Translator, SRTFormatter, FileHandler


class AudioTranscriber:
    def __init__(self, model_size):
        self.transcriber = WhisperAudioTranscriber(model_size)
        self.translator = Translator()
        self.formatter = SRTFormatter()
        self.filehandler = FileHandler()

    def input_processing(self, input_path):
        pass

    def process_file(self, audio_file):
        pass


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
