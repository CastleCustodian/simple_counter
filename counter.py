from tkinter import *
from tkinter import ttk


def increment(*ex):
    count_at.set(int(count_at.get()) + 1)

def reset(*ex):
    count_at.set(0)


root =  Tk()
root.title('Simple Counter')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

count_at =StringVar()
display_count_at = ttk.Label(mainframe, textvariable=count_at)
display_count_at.grid(column=2, row=1, sticky=(E))

ttk.Button(mainframe, text='Reset', command=reset).grid(column=1, row=2, sticky=(W, S))
ttk.Button(mainframe, text='Count', command=increment).grid(column=2, row=2, sticky=(E,S))


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

reset()

root.bind("<Return>", reset)
root.bind("<space>", increment)

root.mainloop()