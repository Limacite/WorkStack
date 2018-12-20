# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:10 2018

@author: ic151215
"""

import json
import glob

def saveJson(filename,task):
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