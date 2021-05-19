from pytube import YouTube
from tkinter import Tk, Button, Label, Entry

SAVE_PATH = r"D:/"
link = "https://www.youtube.com/watch?v=xarC5jAiO7w"

class YouTube_downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("+900+300")
        self.url_entry = Entry(self)
        self.url_entry.grid(row=0, column=0)


if __name__ == "__main__":
    youtube_downloader = YouTube_downloader()
    youtube_downloader.mainloop()

# try:
#     yt = YouTube(link)
#     # print(yt.streams.first().download())
#     # print(
#     #     yt.streams.filter(progressive=True, file_extension="mp4")
#     #     .order_by("resolution")
#     #     .desc()
#     #     .first()
#     # )
#     for stream in yt.streams.order_by("resolution").desc():
#         print(stream)

#     # print(yt.streams.order_by("resolution").desc().get_highest_resolution())
# except:
#     print("Connection Error")

# # mp4files = yt.filter('mp4')
# # yt.set_filename("pytube-download-test")
# # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
# # try:
# #     d_video.download(SAVE_PATH)
# # except:
# #     print("Some Error!")

# # print('Task Completed!')
