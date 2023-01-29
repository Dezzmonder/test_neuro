import tkinter as tk
import json


def paint(c):
    x = (c.x//100)
    y = (c.y//100)
    if not (x,y) in num:
        num.append((x,y))
    cv.create_rectangle(x*100, y*100, x*100 + 100, y*100 + 100, fill="black")
    cv.update()


def clear(c):
    x = (c.x//100)
    y = (c.y//100)
    if (x,y) in num:
        num.remove((x,y))
    cv.create_rectangle(x*100, y*100, x*100 + 100, y*100 + 100, fill="white")
    cv.update()


def save(c):
    with open("num.json", 'w') as write:
        data = {'matrix': num}
        json.dump(data, write)



win = tk.Tk()
cv = tk.Canvas(width=500, height=500)
for i in range(5):
    cv.create_line(i*100, 0, i*100, 500)
    cv.create_line(0, i*100, 500, i*100)
num = []
win.bind('<Key>', save)
cv.bind('<Button-1>', paint)
cv.bind('<Button-3>', clear)
cv.pack()
win.mainloop()
