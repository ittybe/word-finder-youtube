"""
Model is used by every class in this package,
that need to get information from Youtube service  
"""
from pytube import YouTube


class YoutubeModel:
    def __init__(self):
        pass
    
    def get_available_captions(self, video_id)

    def get_caption(self, video_id :str, lang_code :str): 
        video_url = 'https://youtube.com/watch?v=' + video_id
        yt = YouTube(video_url)
        caption = yt.captions.get_by_language_code(lang_code)
        return caption.generate_srt_captions()

    def get_recommend_videos(self, video_id :str):
        pass