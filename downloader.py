from pytube import YouTube
from PIL import Image
import tkinter as tk
import requests
import io


# Assign the light, dark mode colours and startup mode.
light = '#bcbcbc'
dark = '#23272a'
startupMode = dark


def downloader(event=None):
    global yt, downloadBtn
    if len(url.get()) > 0:
        downloadBtn.config(text='Please wait...', state='disabled')
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
    global dispFrame
    dispFrame.destroy()
    currBG = root['bg']
    dispFrame = tk.Frame(root, bg=currBG, width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')
    downloadBtn.config(text='Download Video', state='normal')
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
    dispFrame.destroy()
    dispFrame = tk.Frame(root, width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')
    thumbImg = tk.PhotoImage(file='currentDownloaderImg.png')
    thumbArea = tk.Label(dispFrame, image=thumbImg)
    thumbArea.pack(fill='both', expand=True)
    root.update()
    getVideo()


def changeMode(bgMode, txtMode):
    global info, urlEntry, spacerL, downloadBtn, spacerR, title, views, length, menu, dispFrame
    global spacer1, spacer2, spacer3, spacer4, spacer5, spacer6
    root.config(bg=bgMode)
    info.config(bg=bgMode, fg=txtMode)
    urlEntry.config(bg=bgMode, fg=txtMode)
    spacerL.config(bg=bgMode, fg=txtMode)
    downloadBtn.config(bg=bgMode, fg=txtMode)
    spacerR.config(bg=bgMode, fg=txtMode)
    title.config(bg=bgMode, fg=txtMode)
    views.config(bg=bgMode, fg=txtMode)
    length.config(bg=bgMode, fg=txtMode)
    menu.config(bg=bgMode, fg=txtMode)
    spacer1.config(bg=bgMode, fg=txtMode)
    spacer2.config(bg=bgMode, fg=txtMode)
    spacer3.config(bg=bgMode, fg=txtMode)
    spacer4.config(bg=bgMode, fg=txtMode)
    spacer5.config(bg=bgMode, fg=txtMode)
    spacer6.config(bg=bgMode, fg=txtMode)
    dispFrame.config(bg=bgMode)


# Setup root window
root = tk.Tk()
# Uncomment this next line if you want to remove the title bar. Then to close app use file menu to exit.
##root.attributes('-type', 'splash')
root.title('YouTube Downloader')
root.geometry("740x400")

# Menu Tabs
menu = tk.Menu(root)
root.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Exit', command=root.destroy)
filemenu.add_separator()
filemenu.add_command(label='Light Mode', command=lambda: changeMode(light, dark))
filemenu.add_command(label='Dark Mode', command=lambda: changeMode(dark, light))
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')

# Layout
infoText = tk.StringVar(value='Enter the link below:')
info = tk.Label(root, textvariable=infoText)
info.grid(row=0, column=0, padx=12, pady=10, sticky='w')
url = tk.StringVar()
urlEntry = tk.Entry(root, textvariable=url, width='55', borderwidth='5')
urlEntry.grid(row=1, column=0, columnspan=5, padx=15)
root.bind('<Return>', downloader)
spacerL = tk.Label(root, width=4)
spacerL.grid(row=1, column=6)
downloadBtn = tk.Button(root, text='Download Video', width=14, command=downloader)
downloadBtn.grid(row=1, column=7, columnspan=2, padx=8)
spacerR = tk.Label(root, width=4)
spacerR.grid(row=1, column=9)
getTitle = tk.StringVar(value='Title:')
title = tk.Label(root, textvariable=getTitle)
title.grid(row=2, column=0, columnspan=10, padx=12, pady=10, sticky='w')
getViews = tk.StringVar(value='Views:')
views = tk.Label(root, textvariable=getViews)
views.grid(row=3, columnspan=2, padx=12, sticky='w')
getLength = tk.StringVar(value='Length:')
length = tk.Label(root, textvariable=getLength)
length.grid(row=4, columnspan=2, padx=12, pady=10, sticky='w')
spacer1 = tk.Label(root, text='')
spacer1.grid(row=5, column=0)
spacer2 = tk.Label(root, text='')
spacer2.grid(row=6, column=0)
spacer3 = tk.Label(root, text='')
spacer3.grid(row=7, column=0)
spacer4 = tk.Label(root, text='')
spacer4.grid(row=8, column=0)
spacer5 = tk.Label(root, text='')
spacer5.grid(row=9, column=0)
spacer6 = tk.Label(root, text='')
spacer6.grid(row=10, column=0)
dispFrame = tk.Frame(root, bg='white', width=380, height=255)
dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')

if startupMode == dark: # Depending on the startup mode this will set to light or dark mode.
    changeMode(bgMode=dark, txtMode=light)
else:
    changeMode(bgMode=light, txtMode=dark)
    
root.mainloop()
