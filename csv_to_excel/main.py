import pandas as pd
import openpyxl
import numpy as np
import glob
from chardet.universaldetector import UniversalDetector
from tkinter import *
from tkinter.filedialog import askopenfile, askdirectory
app = Tk()

def fileopen():
    global filename
    filename = askopenfile(filetypes =[('Csv Files', '*.csv')]).name
    detector = UniversalDetector()
    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    print(detector.result['encoding'])
    if detector.result['encoding'] == "GB2312":
        encodings = 'GBK'
    else:
        encodings = detector.result['encoding']
        print(encodings)
    df = pd.read_csv(filename, encoding=encodings)
    convertfilename = filename.replace('.csv', ' converted.xlsx')
    df.to_excel(convertfilename, encoding=encodings, index=False)
    Label(app, text='file converted to the same folder selected successfully!').pack()
'''
def targetdir():
    global path
    path = askdirectory()
    label = Label(app, text=path).pack()
'''


openfile_button = Button(text='click here to select file for conversion', width=50, height=15, command = fileopen).pack()
#targetdir_button = Button(text='click here to select where to save the converted file', width=30, command=targetdir).pack()
#finish_button = Button(text='click to convert', width=30, command=convert).pack()

app.mainloop()

