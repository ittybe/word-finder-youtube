"""
Video Model is used by every class in this package,
that need to get information from Youtube service  

This model represents youtube video
"""

from pytube import YouTube

class YoutubeVideoModel:
    def __init__(self, video_id :str):
        """
            args:
                video_id: str, only id no url 
        """
        self.video_id = video_id

        self.yt_obj = YouTube(self.get_url())

    def get_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"

    def get_caption(self, lang_code):
        pass

    def get_available_languages_of_captions(self) -> list:
        """
        get available captions languages in format like this
        [{
            'lcode' : '<some_lang_code>'
            'lname' : '<some_lang_name>'
        }, 
        ..., ..., ...]

        :rtype: list
        """
        
        # get all captions
        caps = self.yt_obj.captions.keys()

        # read all cap one by one
        result = []
        for cap in caps:
            # get lang code and language s name
            lang_code = cap.code
            lang_name = cap.name

            # write lang code and lang name into list as dict
            result.append(
                {
                    'lcode' : lang_code,
                    'lname' : lang_name
                }
            )

        return result


    
if __name__ == "__main__":
    video = YoutubeVideoModel("RGuJga2Gl_k")
    captions_languages = video.get_available_languages_of_captions()
    print(captions_languages)


    

    
        

