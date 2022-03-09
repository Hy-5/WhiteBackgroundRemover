from array import array
from ast import Pass
from fileinput import filename
from hmac import trans_36, trans_5C
from operator import delitem
from turtle import colormode, left, position, screensize
from unicodedata import name
import webbrowser
import webbrowser
from PIL import Image
#from tkinter import Tk
import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import urllib.parse
from tkinter import messagebox
from tkinter import *

class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

"""class Tab(tkinter.Frame):
    def __init__(self, name:str, nbrofSubTabs:int):
        self.name=name
        self.tabLists=tabList[nbrofSubTabs]
    
    def addSubTab(self, subtabName:str, position:int):
        self.tabLists[position]=subtabName"""

def singleFileModif():
    fileName=askopenfilename()
    outputName=fileName.split(".")
    outputFile=outputName[0] +"_WBRmodified.png"
    with Image.open(fileName) as pic:
        pic=pic.convert("RGBA")
        pixel=pic.load()
    colorFloat=(0,0,0,0)
    for i in range(pic.size[0]):
        for j in range(pic.size[1]):
            if pixel[i,j]>=(210,210,210,210):
                pixel[i,j]=(0,0,0,0)
    pic.save(outputFile)
    print("Done")

def entireFolderModif():
    pass

def callback(url):
    webbrowser.open_new_tab(url)

def tabsDefinition():
    tabList=ttk.Notebook(WBR)

    tab1=ttk.Frame(tabList)
    tab2=ttk.Frame(tabList)
    tabList.add(tab1, text="File")
    tabList.add(tab2, text="About")
    tabList.pack(expand=1, ipadx=500, ipady=500, fill="both")
    ttk.Label(tab2, text="WBR - White Background Remover.\n\nIsmael (Hy-5) Coulibaly\nhttps://github.com/Hy-5").grid(column=0, row=0, padx=0, pady=5)    
    

if __name__=="__main__":
    #Tk().withdraw()
    root=tkinter.Tk()
    root.geometry("600x300")
    WBR=App()
    WBR.master.title("WBR - White Background Remover")
    #WBR.master.maxsize(500,500)
    tabsDefinition()

    WBR.mainloop()



    """fileName=askopenfilename()
    outputName=fileName.split(".")
    outputFile=outputName[0] +"_WBRmodified.png"
    with Image.open(fileName) as pic:
        pic=pic.convert("RGBA")
        pixel=pic.load()
    colorFloat=(0,0,0,0)
    for i in range(pic.size[0]):
        for j in range(pic.size[1]):
            if pixel[i,j]>=(210,210,210,210):
                pixel[i,j]=(0,0,0,0)
    pic.save(outputFile)
    print("Done")"""