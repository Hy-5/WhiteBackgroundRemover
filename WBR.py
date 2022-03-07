from fileinput import filename
from hmac import trans_36, trans_5C
from operator import delitem
from turtle import colormode
from unicodedata import name
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename




if __name__=="__main__":
    Tk().withdraw()
    fileName=askopenfilename()
    outputName=fileName.split(".")
    outputFile=outputName[0] +".png"
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