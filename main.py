from pytube import YouTube
from tkinter import Tk, Button, Label, Entry

SAVE_PATH = r"D:/"
# link = "https://www.youtube.com/watch?v=xarC5jAiO7w"
link = "https://www.youtube.com/watch?v=kR2Fo3B5r2c"

class YouTube_downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("+900+300")
        self.url_entry = Entry(self)
        self.url_entry.grid(row=0, column=0)
        self.download_button = Button(self, text="DOWNLOAD", command=self.download_video)
        self.download_button.grid(row=0, column=1)
        self.status_label = Label(self, text="Status")
        self.status_label.grid(row=1, column=0, columnspan=2)

    def download_video(self):
        print("downloading")
        print(link)
        try:
            yt = YouTube(link)
            print(yt)
            # print(yt.streams.first().download())
            # print(
            #     yt.streams.filter(progressive=True, file_extension="mp4")
            #     .order_by("resolution")
            #     .desc()
            #     .first()
            # )
            print(yt.streams.order_by("resolution").desc())
            # print(yt.streams.order_by("resolution").desc().get_highest_resolution())
        except:
            print("Connection Error")

if __name__ == "__main__":
    youtube_downloader = YouTube_downloader()
    youtube_downloader.mainloop()
