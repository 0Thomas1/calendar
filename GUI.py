from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Prime Number App')
root.attributes('-topmost', 1)
root.iconbitmap('/icon.ico')

# label with a specific font
label = Label(root, text='which function to use')

label.pack()

exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit())

exit_button.pack(
    ipadx=1,
    ipady=1,
    expand=True
)

root.mainloop()
