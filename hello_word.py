
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Hello World")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

title = tk.Label(
    root,
    text="HELLO WORLD!",
    font=("Arial", 28, "bold"),
    fg="#89B4FA",
    bg="#1E1E2E"
)
title.pack(pady=40)

subtitle = tk.Label(
    root,
    text="Welcome to Python Programming 🚀",
    font=("Arial", 11),
    fg="white",
    bg="#1E1E2E"
)
subtitle.pack(pady=5)

def say_hello():
    messagebox.showinfo(
        "Python Says",
        "Hello World! Keep Coding 🔥"
    )

button = tk.Button(
    root,
    text="CLICK ME",
    font=("Arial", 12, "bold"),
    bg="#89B4FA",
    fg="#1E1E2E",
    activebackground="#A6E3A1",
    bd=0,
    padx=25,
    pady=12,
    command=say_hello
)
button.pack(pady=30)

root.mainloop()
