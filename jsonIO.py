# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:10 2018
"""

import json
import glob
import uuid

def saveJson(task):
    filename = "./jsonFiles/" + str(uuid.uuid4()) + ".json"
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
    