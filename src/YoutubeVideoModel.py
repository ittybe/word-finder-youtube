"""
Video Model is used by every class in this package,
that need to get information from Youtube service  

This model represents youtube video
"""
import logging
import types
from pytube import YouTube

logger = logging.getLogger(__name__)

class YoutubeVideoModel:
    def __init__(self, video_id :str):
        """
            :params:
                video_id: str, only id no url 
        """
        self.video_id = video_id

        self.yt_obj = YouTube(self.get_url())

    def get_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"

    def get_caption(self, lang_code):
        pass

    def get_caption_user_comparison(self, comparison :types.FunctionType) -> list:
        """[summary]
        going through all available captions on video and make comparison with language

        Args:
            comparison (function):         
                comparison is a function that takes one param "lambda x: <some comparison>", 
                this param is language code of caption
                function has to return true or false value, 
                if it returns true then caption matches your language preference, otherwise it s not

        Returns:
            list: list of captions that maches your request (in string xml format)
        """
        # get all captions
        caps = self.yt_obj.captions.keys()

        result = []
        
        # iterate throught all captions
        for cap in caps:
            
            # compare with comparison func 
            if (comparison(cap.code)):

                # add matched caption into result list
                result.append(cap)
        
        return result

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
    video = YoutubeVideoModel("aoy_WJ3mE50")
    captions_languages = video.get_available_languages_of_captions()

    print(captions_languages)
    input("press any key")
    list_of_caps = video.get_caption_user_comparison(lambda lang_code: True if "en" in lang_code else False)

    print(list_of_caps)
    print(len(list_of_caps))

    

    
        

