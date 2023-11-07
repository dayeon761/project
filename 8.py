from tkinter import *
import sqlite3

con = sqlite3.connect('Jokkk.db')




def F():
    text.delete(0.0, END)
    cur = con.cursor()
    cur.execute('SELECT Joke FROM Jokes ORDER BY RANDOM() LIMIT 1')
    for row in cur:
        text.insert(END, row)
    cur.close()

window = Tk()
window.title("Кликер")
window.geometry('400x250')

text = Text(window, height=4)  
text.grid() 

button = Button(window, text="Жми!", command=F)
button.grid(column=0, row=1)

con.commit()

con.close()

window.mainloop()