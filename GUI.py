#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

from tkinter import *
from tkinter import filedialog
from Konachan_gui import *
from PIL import ImageTk
import time




def download_clicked():
    filePath = filedir()
    explict = Explicitval.get()
    tag = tagEntered.get()
    sPage = startPageNo.get()
    nPages = noPages.get()
    startDownload(explict,tag,sPage,nPages,filePath)


def filedir():
    path = str(filedialog.askdirectory())
    pathoffile.set(path)
    return path



def startDownload(exp,tag,sPage,nPages,path):
    konachan = konachanDownload()
    konachan.explicit(exp,sPage,nPages,tag,path)
    downloadFile(konachan)


def downloadFile(konachan):
    fileName = konachan.filename
    downloadfile.set(fileName)
    time.sleep(0.5)


def findpages():
    explict = Explicitval.get()
    tag = tagEntered.get()
    tpages =konachanDownload.noOfImages(explict,tag)
    noPages.set(int(tpages))


root = Tk()
root.geometry("600x450")
root.resizable(0,0)
root.title("Image Downloader")

topFrame= Frame(root,width=600,height=110)
topFrame.pack(side=TOP,fill='both')
topFrame.configure(background='black')

bottomFrame = Frame(root,width=600,height=250,background='black')
bottomFrame.pack(fill='both',expand=True)

Explicitval = StringVar()
Explicitval.set(False)
tagEntered =StringVar()
startPageNo =IntVar()
startPageNo.set(1)
noPages = IntVar()
noPages.set(1)
downloadfile = StringVar()
pathoffile = StringVar()

imgPath = "/Users/rohithraj/PycharmProjects/images/konachanLogo.jpg"
imagefile = ImageTk.PhotoImage(file=imgPath)

konachanlogo = Label(topFrame, image=imagefile,background='black',borderwidth=0)
konachanlogo.pack(anchor=CENTER)

rbutton1 = Radiobutton(bottomFrame, text = "Explicit", variable=Explicitval, value=True, background='red')
rbutton1['foreground'] = '#ff0000'
rbutton1.place(x=170,y=20)
rbutton2 = Radiobutton(bottomFrame, text = "Safe", variable=Explicitval, value=False, background='green')
rbutton2['foreground'] = '#ff0000'
rbutton2.place(x=350,y=20)

tagLabel = Label(bottomFrame,text="Tag: ",foreground='#f7f693',background='black')
tagLabel.place(x=130,y=70)

tagInput = Entry(bottomFrame, textvariable=tagEntered,borderwidth=0,width=30)
tagInput.place(x=180,y=70)

startPageLabel = Label(bottomFrame,text="Start Page No: ",foreground='#f7f693',background='black')
startPageLabel.place(x=67,y=110)

startPageNoEntry = Entry(bottomFrame,textvariable=startPageNo,borderwidth=0,width=30)
startPageNoEntry.place(x=180,y=110)

pagesLabel = Label(bottomFrame, text="No of Pages: ",foreground='#f7f693',background='black')
pagesLabel.place(x=77,y=150)

pages = Entry(bottomFrame,textvariable=noPages,borderwidth=0,width=30)
pages.place(x=180,y=150)
Button(bottomFrame, text="ALL",background='black',borderwidth=0, width=10, foreground="blue", command=findpages).place(x=430, y=148)

pathLabel = Label(bottomFrame,text="Path: ",foreground="#f7f693", background='black')
pathLabel.place(x=123, y=190)

path = Entry(bottomFrame, textvariable=pathoffile,width=30, borderwidth=0)
path.place(x=180, y=190)

downloadLabel = Label(bottomFrame, text="Downloading: ",foreground='#f7f693',background='black')
downloadLabel.place(x=71,y=230)

downloadLabelfile = Label(bottomFrame,textvariable=downloadfile, foreground='green',width=30,height=1)
downloadLabelfile.place(x=180,y=230)

downloadButton = Button(bottomFrame,text="Download",background='black',borderwidth=0,foreground='black', width=40, command=download_clicked)
downloadButton.place(x=130,y=270)


root.mainloop()
