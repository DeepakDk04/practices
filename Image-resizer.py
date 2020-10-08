#!/usr/bin/env python3        #--final code
from multiprocessing import Pool  #Processing Images symentaniously [Took less time]
import os
from PIL import Image 

dr = "/opt/icons/"  #Target folder Location
if not os.path.exists(dr):
    os.mkdir(dr)  # Create Target Folder 

tasks = [i for i in os.walk(".")]  # Picking all other files on a current working Directory
tasks = tasks[0][2] # Re assign Task variable For only picking required files Not All Files

def run(task): # creating RUN metthod for pool
    try:
        if  task.endswith(".jpeg"):
            return None #If file is already A .JPEG , We dont neet to process
        if '.' in task:
            return None #Filter the files names with no Extension
        im = Image.open(task) # Hold image data in im Object
        im = im.rotate(270).resize((128,128)).convert("RGB") # Modify according to Requirment
        im.save(dr + task, "jpeg") # Save the Modified Im object as a Image File In a target Location
    except OSError as e:
        print("There was an error")
        print(task, e)

p = Pool(len(tasks)) # Create a pool of no of Files to process
p.map(run, tasks) # excecuting process by maping RUN method with argsa in a Pool

# Output : 
#Nothing To print , If No erorrs, else print Error Messages
#Create modified image files in a  Target Directory
