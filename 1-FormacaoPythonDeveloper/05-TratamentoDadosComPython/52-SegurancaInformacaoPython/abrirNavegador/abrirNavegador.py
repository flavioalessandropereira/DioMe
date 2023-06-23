import webbrowser
from tkinter import *

roote = Tk( )

roote.title('Abrir Browser')
roote.geometry('300x200')

def google():
    webbrowser.open('google.com')


mygoogle =  Button(roote, text = 'Abrir o Google', command=google).pack(padx=20)

roote.mainloop()