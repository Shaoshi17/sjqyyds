import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('警告名字叫“sjqyyds”的黑客正在攻击你的电脑！')
    window.geometry("380x80" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='警告！警告！Windows正在被攻击',
             bg='red',
             font=('楷体', 16),
             width=60, height=4
             ).pack()
    window.mainloop()



threads = []
for i in range(200): #数字可以修改
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()
