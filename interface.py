import tkinter as tk
from tkinter import ttk, messagebox, Frame, RIDGE, Label

root = tk.Tk()
root.title('Language Translation Tool')
root.geometry('990x770')

frame = Frame(root, width=990, height=770, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame.place(x=0, y=0)

Label(root, text='Language Translation Tool', font=("Helvitica 20 bold"), fg="black", background='#F7DC6F').pack(pady=10)

root.mainloop()
