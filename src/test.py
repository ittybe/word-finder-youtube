from YoutubeModel import YoutubeModel

if __name__ == "__main__":
    yt = YoutubeModel()

    caption = yt.get_caption("lIFE7h3m40U", "en")

    print(caption)
    print(type(caption))
