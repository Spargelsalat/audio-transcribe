"""
A package for transcribing Japanese audio and generating bilingual SRT subtitle files.

Modules:
    - AudioTranscriber: Handles audio transcription using the Whisper model.
    - Translator: Handles text translation using MarianMT model.
    - SRTFormatter: Handles the formatting and writing of SRT files.
    - FileHandler: Manages file paths, extensions, and input validation.

Package-level constants:
    DEFAULT_MODEL_SIZE (str): Default Whisper model size.
"""

from .transcriber import WhisperAudioTranscriber
from .mariantranslator import MarianTranslator
from .srt_formatter import SRTFormatter
from .file_handler import FileHandler

__all__ = ["WhisperAudioTranscriber", "MarianTranslator", "SRTFormatter", "FileHandler"]
DEFAULT_MODEL_SIZE = "medium"
