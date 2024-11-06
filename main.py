"""
main.py
It processes audio files or directories containing audio files, transcribes the audio
using Whisper, translates the transcribed text using MarianMT
(or later whisper or some other model local/api idk),
and saves the results
as SRT subtitle, and txt translated and untranslated.
"""

import sys
from src import WhisperAudioTranscriber, MarianTranslator, SRTFormatter, FileHandler


class AudioTranscriber:
    """
    AudioTranscriber is responsible for orchestrating the transcription,
    translation, and subtitle creation process.

    Attributes:
        model_size (str): The size of the Whisper model to use for transcription.
        transcriber (AudioTranscriber): An instance of AudioTranscriber for transcription.
        translator (Translator): An instance of Translator for translation.
        formatter (SRTFormatter): An instance of SRTFormatter to format SRT files.
        file_handler (FileHandler): An instance of FileHandler to handle file operations.
    """

    def __init__(self, model_size="medium", translate=False):
        self.transcriber = WhisperAudioTranscriber(model_size)
        self.mariantranslator = MarianTranslator() if translate else None
        self.formatter = SRTFormatter()
        self.filehandler = FileHandler()

    def input_processing(self, input_path):
        """
        Process an input path (either a single file or a directory of files).

        Args:
            input_path (str): Path to an audio file or folder containing audio files.
        """
        audio_files = self.filehandler.get_audio_files(input_path)
        for file in audio_files:
            self.process_file(file)

    def process_file(self, audio_file):
        """
        Process a single audio file. Transcribe and translate
        the audio file and save it as an SRT file.

        Args:
            audio_path (str): Path to the audio file to be processed.
        """
        print(f"Processing {audio_file}")
        result = self.transcriber.transcribe(audio_file)
        output_path = self.filehandler.get_output_path(audio_file)
        self.formatter.create_srt(
            result["segments"], output_path, self.mariantranslator
        )
        print(f"Created subtitles: {output_path}")


def main():
    """
    Main function to parse arguments and initiate transcript creation
    based on the provided file or directory.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py [path] [model size (medium/large ect.)]")
        sys.exit()
    input_path = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "medium"
    translate_choice = (
        input("Do you want to include English translations? (y/n): ").strip().lower()
    )
    translate = True if translate_choice == "y" else False
    creator = AudioTranscriber(model_size, translate)
    creator.input_processing(input_path)


if __name__ == "__main__":
    main()
