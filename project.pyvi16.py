from tkinter import *
import time
import webbrowser
import random
import tkinter.messagebox as tm
window =Tk()
tm.showinfo ("Welcome", "Welcome to python antivirus would you like to perform a scan?")
window.title("Antivirus")
#Virus
def virus():
    tm.showwarning("Scanning", "Scanning, please wait this can take several minutes")
    print ("Please wait...")
    time.sleep(10)
    tm.showwarning("Antivirus", "Virus detected: pyvi16 putting into quarantine...")
    print ("Please wait...")
    time.sleep(2)
    tm.showerror("Failed", "Failed to put in quarantine")
    
Button(window, text = "Scan now", command = virus, bg="Red", height=5, width=30) .grid (row=1, column =0, sticky=W)
window.mainloop()
