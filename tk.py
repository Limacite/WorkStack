# -*- coding:utf8 -*-
import tkinter as tk
import datetime as dt
import subWindow as sw

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
    sw.saveTask = saveTask
    aW = sw.InputWindow(aTW,dt.datetime.today())
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
    btnList = btnLGen(tskL)
    cmdSet(btnList)
    btnGen(btnList,tskL)  
    
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