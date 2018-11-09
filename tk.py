# -*- coding:utf8 -*-
import tkinter as tk

class InputWindow():
    def packWidget(self):
        self.tFrame.pack()
        self.tEntry.pack()
        self.pFrame.pack()
        self.pEntry.pack()
        self.dFrame.pack()
        self.dEntry.pack()
        self.kFrame.pack()
        self.cFrame.pack()
        self.cText.pack(fill="both")
        self.bottomFrame.pack(fill="both")
        self.okB.pack(side="right")  
        self.canB.pack(side="right")
            
    def __init__(self,pere):
        self.pere = pere
        self.bList = {"t":"","p":"","d":"","k":"","f":"","c":""}
        self.bList["t"] = tk.StringVar()
        self.bList["t"].set("")
        self.bList["p"] = tk.StringVar()
        self.bList["p"].set("")
        self.bList["k"] = tk.IntVar()
        self.bList["k"].set(0)
        self.bList["c"] = tk.StringVar()
        self.bList["c"].set("")
        self.tFrame = tk.LabelFrame(self.pere,text="タイトル",relief="ridge",bd=2)
        self.tEntry = tk.Entry(self.tFrame,textvariable=self.bList["t"])
        self.pFrame = tk.LabelFrame(self.pere,text="優先度",relief="ridge",bd=2)
        self.pEntry = tk.Entry(self.pFrame,textvariable=self.bList["p"])
        self.dFrame = tk.LabelFrame(self.pere,text="日時",relief="ridge",bd=2)
        self.dEntry = tk.Entry(self.dFrame,textvariable=self.bList["d"])
        self.kFrame = tk.LabelFrame(self.pere,text="種類",relief="ridge",bd=2)
        self.kB0 = tk.Radiobutton(self.kFrame,text="仕事",value=0,variable=self.bList["k"])
        self.kB1 = tk.Radiobutton(self.kFrame,text="趣味",value=1,variable=self.bList["k"])
        self.cFrame = tk.LabelFrame(self.pere,text="メモ",relief="ridge",bd=2)
        self.cText = tk.Text(self.cFrame,height="5",width="20")
        self.bottomFrame = tk.Frame(self.pere,bd=0,relief="ridge")
        self.okB = tk.Button(self.bottomFrame,text="適用",command=lambda:saveTask(self.bList,pere))
        self.canB = tk.Button(self.bottomFrame,text="キャンセル",command=lambda:self.pere.destroy())

def saveTask(bL,win):
    tsk = {"title":bL["t"].get(),"priority":bL["p"].get(),"date":0,"kind":bL["k"].get(),"favorit":0,"comment":bL["c"].get()}
    taskList.append(tsk)
    renewTsk(taskList)
    win.destroy()

def addTskWin(event):
    aTW = tk.Toplevel()
    aTW.title("タスクを追加")
    aW = InputWindow(aTW)
    #aw.__init__(aTW)
    aW.packWidget()

def pushed(event):
    event.widget["text"] = "pushed"

def txtGen(tsk):
    return (str(tsk["title"]) + "\n" + "date:" + str(tsk["date"]))

#リストからボタンを作る
def btnLGen(tskL):
    if len(tskL) != 0:
        btn = tk.Button(tskFrame,text=txtGen(tskL[0]))
        return [btn] + btnLGen(tskL[1:])
    else:
        return []

#要素の順番に応じてcommandをセットする
#iは必ず0を入れる
def cmdSet(btnL):
    if len(btnL) != 0:
        btnL[0].bind("<1>",pushed) #左クリックのコマンドをセット  
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
    
#List[0] = car
#List[1:] = cdr
#List[:-1] = 最期の要素を除いたリスト

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
taskBox = {"title":"title","priority":0,"date":181224,"kind":"job","favorit":1,"comment":"comment"}
taskList.append(taskBox)
taskBox = {"title":"ponpon","priority":2,"date":181103,"kind":"hobby","favorit":0,"comment":"cmcmcmc"}
taskList.append(taskBox)
#------------------------

renewTsk(taskList)
#----------------------------



root.mainloop()
#----------------------------