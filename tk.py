# -*- coding:utf8 -*-
import tkinter as tk
import datetime as dt

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
            #self.bList = {"title":"title","priority":"","date":"","kind":"仕事","favorit":0,"comment":""}
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

def saveTask(bL,win):
    tsk = {"title":bL["title"].get(),
           "priority":bL["priority"].get(),
           "date":bL["date"].get(),
           "kind":bL["kind"],
           "favorit":0,
           "comment":bL["comment"].get()}
    taskList.append(tsk)
    renewTsk(taskList)
    win.destroy()

def addTskWin(event):
    aTW = tk.Toplevel()
    aTW.title("タスクを追加")
    aW = InputWindow(aTW,dt.datetime.today())
    aW.packWidget()

def pushed(event):
    event.widget["text"] = "pushed"

def btnLGen(tskL):
    if len(tskL) != 0:
        btnText = str(tskL[0]["title"]) + "\n" + "date:" + str(tskL[0]["date"])
        btn = tk.Button(tskFrame,text=btnText)
        return [btn] + btnLGen(tskL[1:])
    else:
        return []

def cmdSet(btnL):
    if len(btnL) != 0:
        btnL[0].bind("<1>",pushed)
        cmdSet(btnL[1:])

def btnGen(btnL,tskL):
    if len(btnL) != 0:
        btnL[0].pack(fill="both")
        if tskL[0]["favorit"] == 1:
            lbl = tk.Label(btnL[0],text="★")
        else:
            lbl = tk.Label(btnL[0],text="☆")
        lbl.pack(side="right")
        btnGen(btnL[1:],tskL[1:])

def frameClear(frm):
    widL = frm.pack_slaves()
    for l in widL:
        l.destroy()

def renewTsk(tskL):
    frameClear(tskFrame)
    btnList = btnLGen(taskList)
    cmdSet(btnList)
    btnGen(btnList,taskList)    
    
taskList = []
buTskL = []

#-------メインウィンドウ----------
root = tk.Tk()
root.title(u"WorkStack")
root.geometry("300x400")

#--------上部----------------
spFrame = tk.Frame(root,bd=0,relief="ridge")
spFrame.pack(fill="x")
sortBtn = tk.Button(spFrame,text="sort |▼")
sortBtn.pack(side="left")
filtBtn = tk.Button(spFrame,text="filter |▼")
filtBtn.pack(side="left")
addBtn = tk.Button(spFrame,text="+")
addBtn.bind("<1>",addTskWin)
addBtn.pack(side="right")
#----------------------------

#---------タスクリスト-----------
tskFrame = tk.Frame(root,bd=2,relief="ridge")
tskFrame.pack(fill="both")
#-------テスト用-----------
taskBox = {"title":"title","priority":0,"date":181224,"kind":"仕事","favorit":1,"comment":"comment"}
taskList.append(taskBox)
taskBox = {"title":"ponpon","priority":2,"date":181103,"kind":"趣味","favorit":0,"comment":"cmcmcmc"}
taskList.append(taskBox)
#------------------------

renewTsk(taskList)
#----------------------------



root.mainloop()
#----------------------------