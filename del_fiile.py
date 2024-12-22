import tkinter as tk
import sys


window = tk.Tk()
window.title('Калькулятор')
window.geometry("300x250")

label_1 = tk.Label(window, text='1', width=150)
label_1.pack()

window.mainloop()

for path in sys.path:
    print(path)

help('modules')
