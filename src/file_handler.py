"""
A module for handling file-related tasks:
such as validating audio file formats and generating output paths.

Classes:
    FileHandler: Handles tasks related to file identification and path management.
"""

import os


class FileHandler:
    """
    A utility class to manage the file operations related to audio files and SRT generation.

    Attributes:
    -----------
    supported_formats : tuple
        File extensions that are considered valid for processing.

    Methods:
    --------
    is_audio_file(file_path):
        Checks if a given file path points to a valid audio file format.

    get_output_path(input_path):
        Generates the output SRT file path from an input audio file path.

    get_audio_files(path):
        Recursively scans a folder and retrieves all audio files with supported formats.
    """

    def __init__(self):
        self.supportedformats = (".wav", ".mp3")

    def get_audio_files(self, file_path):
        """
        Recursively searches a directory for audio files with supported formats.
        """
        if os.path.isfile(file_path):
            return [file_path] if self.is_audio_file(file_path) else []
        audio_files = []
        for root, _, files in os.walk(file_path):
            for file in files:
                if self.is_audio_file(file):
                    audio_files.append(os.path.join(root, file))
        return audio_files

    def is_audio_file(self, file_path):
        """
        Checks if the given file path is an audio file with a supported extension.
        """
        return file_path.lower().endswith(self.supportedformats)

    def get_output_path(self, file_path):
        """
        Generates the SRT output file path from the input audio file path.
        """
        return os.path.splitext(file_path)[0] + ".srt"
