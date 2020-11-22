from tkinter import filedialog
from pytube import YouTube
from PIL import Image
import tkinter as tk
import requests
import io


# Assign the light, dark mode colours and startup mode.
light = '#bcbcbc'
dark = '#23272a'
startupMode = dark
titleFont = ('Verdana', 28) # Used only on the about page for YouTube Downloader
textFont = ('Verdana', 9) # Used everywhere, change font or size to test on your machine.


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
        getDesc.insert('end', yt.description)
        getImg = requests.get(yt.thumbnail_url)
        img = Image.open(io.BytesIO(getImg.content))
        img = img.resize((380, 265))
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
    currBG = menu['bg']
    dispFrame = tk.Frame(rootFrame, bg=currBG, width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')
    downloadBtn.config(text='Download Video', state='normal')
    infoText.set('Enter the link below:')
    getTitle.set('Title:')
    getViews.set('Views:')
    getLength.set('Length:')
    getDesc.delete('1.0', tk.END)
    url.set('')
    urlEntry.focus()


def getVideo():
    global saveAs
    ytTitle = yt.title
    try:
        saveAs = filedialog.asksaveasfilename(initialfile=ytTitle, filetypes=[('mp4', '*.mp4')])
        filename = saveAs.split('/')[-1]
        i = saveAs.index(filename)
        path = saveAs[:i]
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(output_path=path, filename=filename)
    except AttributeError:
        downloadBtn.config(text='Download Cancelled', state='disabled')


def updateImg():
    global thumbImg, dispFrame
    dispFrame.destroy()
    dispFrame = tk.Frame(rootFrame, width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')
    thumbImg = tk.PhotoImage(file='currentDownloaderImg.png')
    thumbArea = tk.Label(dispFrame, image=thumbImg)
    thumbArea.pack(fill='both', expand=True)
    root.update()
    getVideo()


def mainMode(bgMode, txtMode):
    root.config(bg=bgMode)
    rootFrame.config(bg=bgMode)
    descFrame.config(bg=bgMode)
    dispFrame.config(bg=bgMode)
    info.config(bg=bgMode, fg=txtMode)
    clearBtn.config(bg=bgMode, fg=txtMode)
    urlEntry.config(bg=bgMode, fg=txtMode)
    spacerL.config(bg=bgMode, fg=txtMode)
    downloadBtn.config(bg=bgMode, fg=txtMode)
    spacerR.config(bg=bgMode, fg=txtMode)
    title.config(bg=bgMode, fg=txtMode)
    views.config(bg=bgMode, fg=txtMode)
    length.config(bg=bgMode, fg=txtMode)
    menu.config(bg=bgMode, fg=txtMode)
    filemenu.config(bg=bgMode, fg=txtMode)
    helpmenu.config(bg=bgMode, fg=txtMode)
    desc.config(bg=bgMode, fg=txtMode)
    getDesc.config(bg=bgMode, fg=txtMode)


def aboutMode(bgMode, txtMode):
    root.config(bg=bgMode)
    rootFrame.config(bg=bgMode)
    menu.config(bg=bgMode, fg=fgMode)
    title.config(bg=bgMode, fg=txtMode)
    line1.config(bg=bgMode, fg=txtMode)


def about(bgMode, txtMode):
    global rootFrame, menu, filemenu, helpmenu, title, line1
    # Menu Tabs
    menu = tk.Menu(root, bg=bgMode, fg=txtMode, font=textFont)
    root.config(menu=menu) 
    filemenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu, font=textFont)
    filemenu.add_command(label='Downloader', command=lambda: main(bgMode, txtMode))
    filemenu.add_command(label='Exit', command=root.destroy)
    filemenu.add_separator()
    filemenu.add_command(label='Light Mode', command=lambda: about(light, dark))
    filemenu.add_command(label='Dark Mode', command=lambda: about(dark, light))
    helpmenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu, font=textFont) 
    helpmenu.add_command(label='About', command=about)
    # layout
    rootFrame.destroy()
    rootFrame = tk.Frame(root, bg=bgMode)
    rootFrame.pack(fill='both', expand=True)
    title = tk.Label(rootFrame, text='YouTube Downloader', bg=bgMode, fg=txtMode, font=titleFont)
    title.pack(pady=100)
    # If you want to add to this about page, copy the next 2 lines above and paste below and change the line1 to line2 etc.
    line1 = tk.Label(rootFrame, text='created by Swapnanil Dutta', bg=bgMode, fg=txtMode, font=textFont)
    line1.pack()


def main(bgMode, txtMode):
    global rootFrame, info, infoText, clearBtn, urlEntry, spacerL, downloadBtn, spacerR, filemenu, helpmenu
    global getDesc, url, title, getTitle, views, getViews, length, getLength, desc, menu, descFrame, dispFrame
    # Menu Tabs
    menu = tk.Menu(root, bg=bgMode, fg=txtMode, font=textFont)
    root.config(menu=menu)
    filemenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu, font=textFont)
    filemenu.add_command(label='Downloader', command=lambda: main(bgMode, txtMode))
    filemenu.add_command(label='Exit', command=root.destroy)
    filemenu.add_separator()
    filemenu.add_command(label='Light Mode', command=lambda: mainMode(light, dark))
    filemenu.add_command(label='Dark Mode', command=lambda: mainMode(dark, light))
    helpmenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu, font=textFont) 
    helpmenu.add_command(label='About', command=lambda: about(bgMode, txtMode))
    # Layout
    rootFrame.destroy()
    rootFrame = tk.Frame(root, bg=bgMode)
    rootFrame.pack(fill='both', expand=True)
    infoText = tk.StringVar(value='Enter the link below:')
    info = tk.Label(rootFrame, textvariable=infoText, bg=bgMode, fg=txtMode, font=textFont)
    info.grid(row=0, column=0, padx=12, pady=10, sticky='w')
    clearBtn = tk.Button(rootFrame, text='Clear Data', width=14, bg=bgMode, fg=txtMode, font=textFont, command=clearData)
    clearBtn.grid(row=0, column=7, columnspan=2, padx=8)
    url = tk.StringVar()
    urlEntry = tk.Entry(rootFrame, textvariable=url, width='55', borderwidth='5', bg=bgMode, fg=txtMode, font=textFont)
    urlEntry.grid(row=1, column=0, columnspan=5, padx=15)
    root.bind('<Return>', downloader)
    spacerL = tk.Label(rootFrame, width=4, bg=bgMode, fg=txtMode, font=textFont)
    spacerL.grid(row=1, column=6)
    downloadBtn = tk.Button(rootFrame, text='Download Video', width=14, bg=bgMode, fg=txtMode, font=textFont, command=downloader)
    downloadBtn.grid(row=1, column=7, columnspan=2, padx=8)
    spacerR = tk.Label(rootFrame, width=4, bg=bgMode, fg=txtMode, font=textFont)
    spacerR.grid(row=1, column=9)
    getTitle = tk.StringVar(value='Title:')
    title = tk.Label(rootFrame, textvariable=getTitle, bg=bgMode, fg=txtMode, font=textFont)
    title.grid(row=2, column=0, columnspan=10, padx=12, pady=5, sticky='w')
    getViews = tk.StringVar(value='Views:')
    views = tk.Label(rootFrame, textvariable=getViews, bg=bgMode, fg=txtMode, font=textFont)
    views.grid(row=3, column=0, columnspan=2, padx=12, pady=5, sticky='w')
    getLength = tk.StringVar(value='Length:')
    length = tk.Label(rootFrame, textvariable=getLength, bg=bgMode, fg=txtMode, font=textFont)
    length.grid(row=4, column=0, columnspan=2, padx=12, pady=5, sticky='w')
    desc = tk.Label(rootFrame, text='Description:', bg=bgMode, fg=txtMode, font=textFont)
    desc.grid(row=5, column=0, padx=12, pady=5, sticky='w')
    descFrame = tk.Frame(rootFrame, bg=bgMode)
    descFrame.grid(row=6, rowspan=6, column=0, columnspan=2, padx=12, sticky='w')
    descScroll = tk.Scrollbar(descFrame)
    descScroll.pack(side='right', fill='both', expand=True)
    getDesc = tk.Text(descFrame, width=35, height=10, wrap='word', bg=bgMode, fg=txtMode, font=textFont)
    getDesc.pack()
    getDesc.config(yscrollcommand=descScroll.set)
    descScroll.config(command=getDesc.yview)
    dispFrame = tk.Frame(rootFrame, bg=bgMode, width=380, height=255)
    dispFrame.grid(row=3, rowspan=12, column=0, columnspan=10, sticky='e')


# Setup root window
root = tk.Tk()
# Uncomment this next line if you want to remove the title bar. Then to close app use file menu to exit.
##root.attributes('-type', 'splash')
root.title('YouTube Downloader')
root.geometry("740x400")
rootFrame = tk.Frame(root)
rootFrame.pack(fill='both', expand=True)

if startupMode == dark: # Depending on the startup mode this will set to light or dark mode.
    main(dark, light)
else:
    main(light, dark)
    
root.mainloop()
