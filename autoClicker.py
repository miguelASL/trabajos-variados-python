import tkinter as tk
from tkinter import ttk
import ctypes
import time

class AutoClicker:
    def __init__(self):
        self.mouse = ctypes.windll.user32
        self.state = False
        self.X = 0
        self.root = tk.Tk()
        self.root.title("AutoClicker")
        self.root.resizable(width=False, height=False)

        self.amount = tk.StringVar()
        self.speed = tk.StringVar()

        self.amount.set(0)
        self.speed.set(100)
        mainframe = ttk.Frame(self.root)
        mainframe.grid(padx= 5, pady= 5)

        ttk.Label(mainframe, text="Cantidad de clicks:").grid(column=1, row=1, sticky=tk.W)
        ttk.Entry(mainframe, width=7, textvariable=self.amount).grid(column=1, row=2, sticky=tk.W)
        ttk.Entry(mainframe, width=7, textvariable=self.speed).grid(column=1, row=3, sticky=tk.W)
        ttk.Button(mainframe, text="Start", command=self.StateTrue).grid(column=1, row=5, sticky=tk.W)
        ttk.Button(mainframe, text="Stop", command=self.StateFalse).grid(column=1, row=6, sticky=tk.W)
        mainframe.bind("<F1>", lambda e: self.StateTrue())
        mainframe.bind("<F2>", lambda e: self.StateFalse())

    def StateFalse(self):
        if self.state:
            self.state = False
            self.X = 0
            print("OFF")

    def StateTrue(self):
        if not self.state:
            self.X = 0
            self.state = True
            print("ON")

    def run(self):
        while True:
            if self.state:
                Amount = int(self.amount.get())
                Speed = int(self.speed.get())
                print(self.state)
                if Amount == 0:
                    time.sleep(Speed / 1000)
                    self.mouse.mouse_event(2, 0, 0, 0, 0) # Left Down
                    self.mouse.mouse_event(4, 0, 0, 0, 0) # Left Up

                elif self.X < Amount:
                    time.sleep(Speed / 1000)
                    self.mouse.mouse_event(2, 0, 0, 0, 0) # Left Down
                    self.mouse.mouse_event(4, 0, 0, 0, 0) # Left Up
                    self.X += 1
                    print("Clicked {} times".format(self.X))
                    if self.X == Amount:
                        self.state = False
                        self.X = 0
                        print("OFF")

if __name__ == "__main__":
    AutoClicker().run()