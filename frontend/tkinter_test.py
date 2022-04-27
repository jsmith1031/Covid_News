import tkinter
from tkinter import Button
from datetime import datetime
import time

standardTextSize = 30

def Draw():
    
    global text

    frame=tkinter.Frame(window,width=100,height=100,relief='solid',bd=1)
    frame.place(relx= 0.15, rely= 0.90, anchor = 'center')

    get_local_news = Button(window, text="Get Local News", font=("Arial", 14), height = 10, width = 20, command=window.destroy)
    get_local_news.place(relx= 0.42, rely= 0.79, anchor = 'center')

    symptom_checker = Button(window, text="Symptom Checker", font=("Arial", 14), height = 10, width = 20, command=window.destroy)
    symptom_checker.place(relx= 0.65, rely= 0.79, anchor = 'center')

    '''
    exit_button = Button(window, text="Exit", height = 10, width = 20, command=window.destroy)
    exit_button.pack(pady=200)
    '''





window = tkinter.Tk()
window.geometry("1024x600")

Draw()

window.mainloop()