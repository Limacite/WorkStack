# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 23:16:21 2018

@author: ic151215
"""
import tkinter as tk

def saveTask(self):
    pass

class InputWindow():
    kL = ("仕事","趣味")

    def packWidget(self):
        self.tFrame.pack()
        self.tEntry.pack()
        self.pFrame.pack()
        self.pEntry.pack()
        self.dFrame.pack()
        self.dEntry.pack()
        self.kFrame.pack()
        self.kB0.pack()
        self.kB1.pack()
        self.cFrame.pack()
        self.cText.pack(fill="both")
        self.bottomFrame.pack(fill="both")
        self.okB.pack(side="right")  
        self.canB.pack(side="right")
            
    def __init__(self,pere,toDay,tsk={}):
        self.pere = pere
        if tsk == {}:
            self.bList = {}
            self.bList["title"] = tk.StringVar()
            self.bList["priority"] = tk.StringVar()
            self.bList["date"] = tk.StringVar()
            self.bList["date"].set(toDay.strftime("%Y-%m-%d"))
            self.bList["kind"] = tk.StringVar()
            self.bList["kind"].set("仕事")
            self.bList["comment"] = tk.StringVar()
        else:
            self.bList = tsk
            self.bList["title"] = tk.StringVar()
            self.bList["title"].set(tsk["title"])
            self.bList["priority"] = tk.StringVar()
            self.bList["priority"].set(tsk["priority"])
            self.bList["date"] = tk.StringVar()
            self.date = toDay.strftime("%Y-%m-%d")
            self.bList["date"].set(self.date)
            self.bList["kind"] = tk.StringVar()
            self.bList["kind"].set(tsk["kind"])
            self.bList["comment"] = tk.StringVar()
            self.bList["comment"].set(tsk["comment"])
        
        self.tFrame = tk.LabelFrame(self.pere,text="タイトル",relief="ridge",bd=2)
        self.tEntry = tk.Entry(self.tFrame,textvariable=self.bList["title"])
        self.pFrame = tk.LabelFrame(self.pere,text="優先度",relief="ridge",bd=2)
        self.pEntry = tk.Entry(self.pFrame,textvariable=self.bList["priority"])
        self.dFrame = tk.LabelFrame(self.pere,text="日時",relief="ridge",bd=2)
        self.dEntry = tk.Entry(self.dFrame,textvariable=self.bList["date"])
        self.kFrame = tk.LabelFrame(self.pere,text="種類",relief="ridge",bd=2)
        self.kB0 = tk.Radiobutton(self.kFrame,text="仕事",value=InputWindow.kL[0],variable=self.bList["kind"])
        self.kB1 = tk.Radiobutton(self.kFrame,text="趣味",value=InputWindow.kL[1],variable=self.bList["kind"])
        self.cFrame = tk.LabelFrame(self.pere,text="メモ",relief="ridge",bd=2)
        self.cText = tk.Text(self.cFrame,height="5",width="20")
        self.bottomFrame = tk.Frame(self.pere,bd=0,relief="ridge")
        self.okB = tk.Button(self.bottomFrame,text="適用",command=lambda:saveTask(self.bList,pere))
        self.canB = tk.Button(self.bottomFrame,text="キャンセル",command=lambda:self.pere.destroy())

