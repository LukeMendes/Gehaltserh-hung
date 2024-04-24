import tkinter as tk
import time
import random

def on_button_enter(e):
    xpos = random.randint(1,470)
    ypos = random.randint(50,370)
    button.place(x=xpos, y=ypos, width=20, height=20)

def on_button_click2():
    label3 = tk.Label(root, text="Sehr vernünftige Entscheidung!", font=("Arial", 16))
    label3.place(x=100,y=100,width=300,height=20)
    label4 = tk.Label(root, text="Bis zum nächsten Jahr...", font=("Arial", 16))
    label4.place(x=100,y=200,width=300,height=20)
    button.destroy()
    root.after(5000, lambda:root.destroy())

#--------------
# Hauptprogramm
#--------------

root = tk.Tk()
root.title("funID")
root.geometry("500x500")
root.resizable(False, False)

label1 = tk.Label(root, text="Herzlich willkommen in Ihrem virtuellen Personalbüro !", font=("Arial",14))
label1.pack()
label2 = tk.Label(root, text="Sie wollen eine Gehaltserhöhung ???", font=("Arial",14))
label2.pack()

button2 = tk.Button(root, text="Nein", command=on_button_click2)
button2.place(x=150, y=400, width=200, height=80)

horiz = 230
verti = 300
button = tk.Button(root, text="Ja")
button.place(x=horiz, y=verti, width=20, height=20)
button.bind("<Enter>", on_button_enter)

root.mainloop()
