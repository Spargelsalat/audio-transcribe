import os


class FileHandler:
    def __init__(self):
        self.supportedformats = (".wav", ".mp3")

    def get_audio_files(self, file_path):
        if os.path.isfile(file_path):
            return [file_path] if self.is_audio_file(file_path) else []
        audio_files = []
        for root, _, files in os.walk(file_path):
            for file in files:
                if self.is_audio_file(file):
                    audio_files.append(os.path.join(root, file))
        return audio_files

    def is_audio_file(self, file_path):
        return file_path.lower().endswith(self.supportedformats)

    def get_output_path(self, file_path):
        return os.path.splitext(file_path)[0] + ".srt"
