from pytube import YouTube
from sys import argv

link=argv[1]
print(link)
yt=YouTube(link)
print(yt.title)
print(yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("C:\\YTDownload")