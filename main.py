from pytube import YouTube, exceptions
from tkinter import Checkbutton, Tk, Button, Label, Entry, IntVar


class YouTube_downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("+900+300")
        self.iconbitmap("icon.ico")
        self.url_entry = Entry(self, width=50)
        self.url_entry.grid(row=0, column=0, padx=10, pady=10)
        self.download_button = Button(
            self, text="DOWNLOAD", command=self.download_video
        )
        self.download_button.grid(row=0, column=2, padx=10)
        self.audio_check = IntVar()
        self.audio_only_button = Checkbutton(
            self, text="Audio Only", variable=self.audio_check
        )
        self.audio_only_button.grid(row=0, column=1)
        self.status_label = Label(self, font="Helvetica 12 bold")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=[0, 10])

    def download_video(self):
        url = self.url_entry.get()
        try:
            yt = YouTube(url)

            if self.audio_check.get():
                yt.streams.filter(file_extension="mp4").filter(
                    only_audio=True
                ).order_by("abr").desc().first().download()
            else:
                yt.streams.filter(progressive=True).order_by(
                    "resolution"
                ).desc().first().download()

            self.status_label.config(text=f"Download Complete")

        except exceptions.RegexMatchError:
            self.status_label.config(text="URL Not Found")

        except Exception as e:
            self.status_label.config(text=f"{e}")
            print(e)


if __name__ == "__main__":
    youtube_downloader = YouTube_downloader()
    youtube_downloader.mainloop()
