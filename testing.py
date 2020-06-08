from pytube import YouTube
_url='https://www.youtube.com/watch?v=XLBjvccXX_o'
yt = YouTube(str(_url))
print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download())