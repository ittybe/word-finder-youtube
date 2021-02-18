from YoutubeModel import YoutubeModel

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=lIFE7h3m40U'
    yt = YouTube(video_url)

    yt.captions
    # yt = YoutubeModel()

    # caption = yt.get_caption("lIFE7h3m40U", "en")

    # print(caption)
    # print(type(caption))
