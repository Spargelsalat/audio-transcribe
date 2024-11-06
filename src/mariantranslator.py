"""
mariantranslator.py: A module responsible for handling translation using MarianMTModel.
"""

from transformers import MarianMTModel, MarianTokenizer


class MarianTranslator:
    """
    A class to handle translation using MarianMTModel.
    """

    def __init__(self, model_name="twieland/VN_ja_to_en"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None

    def load_model(self):
        """
        Load the MarianMT model and tokenizer.
        """
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def translate(self, text):
        """
        Translate the given text using the MarianMT model.

        Args:
            text (str): The text to translate.

        Returns:
            str: The translated text.
        """
        if not self.model:
            self.load_model()
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)
