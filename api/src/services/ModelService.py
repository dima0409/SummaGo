import whisper
from moviepy.editor import *


class ModelService:

    def convert_to_mp3(self, video_path: str, audio_path: str):
        clip = VideoFileClip(video_path)
        audio = clip.audio
        audio.write_audiofile(audio_path)
        return True


    def get_text_from_mp3(self, mp3_path: str):
        model = whisper.load_model("small")
        result = model.transcribe(mp3_path)
        return result["text"]