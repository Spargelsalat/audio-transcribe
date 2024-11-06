"""
srt_formatter.py: A module responsible for formatting and creating SRT subtitle files.
"""


class SRTFormatter:
    """
    A class to handle the creation of SRT (Subtitle) files.
    """

    def create_srt(self, segments, output_path, translator=None):
        """
        Create an SRT file from segments.
        """
        with open(output_path, "w", encoding="utf-8") as srt_file:
            for i, segment in enumerate(segments):
                # Write index
                srt_file.write(f"{i+1}\n")

                # Write timestamps
                start = self.format_timestamp(segment["start"])
                end = self.format_timestamp(segment["end"])
                srt_file.write(f"{start} --> {end}\n")

                # Write untranslated text
                untranslated_text = segment["text"].strip()
                srt_file.write(f"{untranslated_text}\n")

                # Write translated text
                if translator:
                    translated_text = translator.translate(untranslated_text)
                    srt_file.write(f"{translated_text}\n")

                srt_file.write("\n")

    def format_timestamp(self, seconds):
        """
        Convert a time in seconds to SRT timestamp format.
        """
        milliseconds = int((seconds % 1) * 1000)
        total_seconds = int(seconds)  # Get the total seconds
        minutes = total_seconds // 60  # Get the total minutes
        hours = minutes // 60  # Get the total hours
        seconds = total_seconds % 60  # Remaining seconds
        minutes = minutes % 60  # Remaining minutes
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
