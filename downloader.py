from pytube import YouTube
from PIL import Image
import tkinter as tk
import requests
import io


def downloader():
    global yt
    if len(url.get()) > 0:
        downloadBtn.config(text='Please wait...', bg='yellow', state='disabled')
        root.update()
        yt = YouTube(url.get())
        getTitle.set('Title: {}'.format(yt.title))
        getViews.set('Views: {}'.format(yt.views))
        mins, secs = divmod(yt.length, 60)
        hrs, mins = divmod(mins, 60)
        getLength.set('Length: {}:{}:{}'.format(str(hrs).zfill(2), str(mins).zfill(2), str(secs).zfill(2)))
        getImg = requests.get(yt.thumbnail_url)
        img = Image.open(io.BytesIO(getImg.content))
        img = img.resize((380, 255))
        img.save('currentDownloaderImg.png')
        root.after(1000, updateImg)
    else:
        infoText.set('No link to download! Please enter link.')
        downloadBtn.config(state='disabled')
        root.update()
        root.after(3000, infoText.set('Enter the link below:'))
        downloadBtn.config(state='normal')


def clearData():
    dispFrame.destroy()
    downloadBtn.config(text='Download Video', bg='lightgreen', state='normal')
    infoText.set('Enter the link below:')
    getTitle.set('Title:')
    getViews.set('Views:')
    getLength.set('Length:')
    url.set('')
    urlEntry.focus()


def getVideo():
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    root.after(3000, clearData)


def updateImg():
    global thumbImg, dispFrame
    dispFrame = tk.Frame(root, bg='black', width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=1, columnspan=4)
    thumbImg = tk.PhotoImage(file='currentDownloaderImg.png')
    thumbArea = tk.Label(dispFrame, image=thumbImg)
    thumbArea.pack(fill='both', expand=True)
    root.update()
    getVideo()


# Setup root window
root = tk.Tk()
root.title('YouTube Downloader')
root.geometry("650x400")

# Menu Tabs
menu = tk.Menu(root)
root.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Exit', command=root.destroy) 
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

# Layout
infoText = tk.StringVar(value='Enter the link below:')
info = tk.Label(root, textvariable=infoText)
info.grid(row=0, column=0, padx=12, pady=10, sticky='w')
url = tk.StringVar()
urlEntry = tk.Entry(root, textvariable=url, width='55', borderwidth='5')
urlEntry.grid(row=1, column=0, columnspan=2, padx=15)
urlEntry.focus()
downloadBtn = tk.Button(root, text='Download Video', width=14, bg='lightgreen', command=downloader)
downloadBtn.grid(row=1, column=3, padx=8)
getTitle = tk.StringVar(value='Title:')
title = tk.Label(root, textvariable=getTitle)
title.grid(row=2, column=0, columnspan=4, padx=12, pady=10, sticky='w')
getViews = tk.StringVar(value='Views:')
views = tk.Label(root, textvariable=getViews)
views.grid(row=3, column=0, padx=12, sticky='w')
getLength = tk.StringVar(value='Length:')
length = tk.Label(root, textvariable=getLength)
length.grid(row=4, column=0, padx=12, pady=10, sticky='w')
for i in range(5, 15):
    spacer1 = tk.Label(root, text='')
    spacer1.grid(row=i, column=0)


root.mainloop()
