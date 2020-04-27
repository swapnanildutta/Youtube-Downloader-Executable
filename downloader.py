from pytube import YouTube
import tkinter as tk
import time
#YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
root=tk.Tk()



def Interface():   

    def downloader():
        _url=e.get()
        if len(_url)>0:
            try:
                yt = YouTube(str(_url))
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
                ourMessage ='Downloaded !!'
                messageVar = tk.Message(root, text = ourMessage) 
                messageVar.config(bg='lightgreen') 
            except:
                ourMessage ='Error! Check link.'
                messageVar = tk.Message(root, text = ourMessage) 
                messageVar.config(bg='red')
        else:
            ourMessage ='No link to download! Please enter link.'
            messageVar = tk.Message(root, text = ourMessage) 
            messageVar.config(bg='yellow')
        messageVar.pack()
        root.deletecommand(messageVar)
        #e.update()
    
    menu = tk.Menu(root)
    root.config(menu=menu) 
    filemenu = tk.Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Exit', command=root.quit) 
    helpmenu = tk.Menu(menu) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About') 

    root.geometry("600x200")
    rect=tk.Label(root,text="Youtube Downloader",bg='red',fg='white')
    rect.pack(ipadx=5,ipady=5,fill='x')

    instruct=tk.Label(root,text='Enter the link below')
    instruct.pack()

    e=tk.Entry(root,width='400',borderwidth='5')
    e.pack(pady=5)


    downb=tk.Button(root,text='Download Video',command=downloader)

    downb.pack(pady=5)

    root.mainloop()

Interface()