# -*- coding:utf8 -*-
import tkinter as tk

def saveTask(bL,win):
    tsk = {"title":bL["t"].get(),"priority":0,"date":0,"kind":0,"favorit":0,"comment":"comment"}
    taskList.append(tsk)
    renewTsk(taskList)
    win.destroy()

def addTskWin(event):
    aTW = tk.Toplevel(root)
    aTW.title("タスクを追加")
    bList = {"t":"","p":"","d":"","k":"","f":"","c":""}
    
    bList["t"] = tk.StringVar()
    bList["t"].set("")
    pBuffer = tk.StringVar()
    pBuffer.set("")
    bList["k"] = tk.IntVar()
    bList["k"].set(0)
    bList["c"] = tk.StringVar()
    bList["c"].set("")
    kL = ("仕事","趣味")
    
    tFrame = tk.LabelFrame(aTW,text="タイトル",relief="ridge",bd=2)
    tFrame.pack()
    tk.Entry(tFrame,textvariable=bList["t"]).pack()
    pFrame = tk.LabelFrame(aTW,text="優先度",relief="ridge",bd=2)
    pFrame.pack()
    tk.Entry(pFrame,textvariable=bList["p"]).pack()
    dFrame = tk.LabelFrame(aTW,text="日時",relief="ridge",bd=2)
    dFrame.pack()
    tk.Entry(dFrame,textvariable=bList["d"]).pack()
    kFrame = tk.LabelFrame(aTW,text="種類",relief="ridge",bd=2)
    kFrame.pack()
    tk.Radiobutton(kFrame,text="仕事",value=0,variable=bList["k"]).pack(side="left")
    tk.Radiobutton(kFrame,text="趣味",value=1,variable=bList["k"]).pack(side="left")
    cFrame = tk.LabelFrame(aTW,text="メモ",relief="ridge",bd=2)
    cFrame.pack()
    tk.Text(cFrame,height="5",width="20").pack(fill="both")
    #tk.Entry(cFrame,textvariable=bList["c"]).pack(fill="both")
    
    bottomFrame = tk.Frame(aTW,bd=0,relief="ridge")
    bottomFrame.pack(fill="both")
    
    #taskBox = {"title":bList["t"].get("1.0","end"),"priority":0,"date":0,"kind":0,"favorit":0,"comment":"comment"}
    
    okB = tk.Button(bottomFrame,text="適用",command=lambda:saveTask(bList,aTW))
    canB = tk.Button(bottomFrame,text="キャンセル",command=lambda:aTW.destroy())
    
    okB.pack(side="right")  
    canB.pack(side="right")

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