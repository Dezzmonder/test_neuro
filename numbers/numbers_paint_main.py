import tkinter as tk
import numpy as np
import numbers_neuro

class Paint:
    def __init__(self):
        self.win = tk.Tk()
        self.cv = tk.Canvas(width=300, height=500)
        self.num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(5):
            self.cv.create_line(i * 100 + 1, 0, i * 100 + 1, 500)
            self.cv.create_line(0, i * 100 + 1, 300, i * 100 + 1)
        self.cv.bind("<Button-1>", self.paint)
        self.cv.bind("<B1-Motion>", self.paint)
        self.cv.bind("<Button-3>", self.clear)
        self.cv.bind("<B3-Motion>", self.clear)
        self.cv.pack()
        self.answer = tk.Text(width=35, height=5)
        self.btncalc = tk.Button(text='Вычислить', command=self.calc)
        self.btncalc.pack()
        self.answer.pack()
        self.neuro = numbers_neuro.network
        self.win.mainloop()

    def paint(self, c):
        x = (c.x // 100)
        y = (c.y // 100)
        self.num[y * 3 + x] = 1
        self.cv.create_rectangle(x * 100, y * 100, x * 100 + 100, y * 100 + 100, fill="black")
        self.cv.update()

    def clear(self, c):
        x = (c.x // 100)
        y = (c.y // 100)
        self.num[y * 3 + x] = 0
        self.cv.create_rectangle(x * 100, y * 100, x * 100 + 100, y * 100 + 100, fill="white")
        self.cv.update()

    def calc(self):
        self.answer.delete(1.0, 100.0)
        str = ''
        temp = self.neuro.forward(np.array(self.num))
        str += f'я думаю, что это:\n{temp.index(max(temp))}\nУверенность: {max(temp)}\n'
        self.answer.insert(1.0, str)
        print(str)


paint = Paint()
