# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:10 2018

@author: ic151215
"""

import json
import glob

def saveJson(filename,task):
    filename = "./jsonFiles/" + str(filename)
    with open(filename,"w") as file:
        json.dump(task,file)
        
def inportJson():
    taskList = list()
    jsonList = glob.glob("./jsonFiles/*")
    for filename in jsonList:
        x = open(filename)
        taskList.append(json.load(x))
        x.close()
    
    return taskList


def main():
    taskList = inportJson()
    print(taskList)
    print("title:")
    title = input()
    print("priority:")
    priority = input()
    print("date:")
    date = input()
    print("kind:")
    kind = input()
    print("favorit:")
    fav = input()
    print("comment:")
    com = input()
    task = {"title":title,"priority":priority,"date":date,"kind":kind,"favorit":fav,"comment":com}
    saveJson("test.json",task)
    print("complete")
    
main()
    
    