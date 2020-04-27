from pytube import YouTube
_url='https://www.youtube.com/watch?v=_V_SnyuBCpY&list=PLIivdWyY5sqKiWvnaA5A8F3UQ0Xu5i49U&index=3'
yt = YouTube(str(_url))
print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[0].)