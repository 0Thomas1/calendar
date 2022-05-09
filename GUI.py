from main import *
from tkinter import *
from tkinter import ttk



root = Tk()
root.geometry('450x300')
root.resizable(True, True)
root.title('Prime Number App')
root.attributes('-topmost', 1)
root.iconbitmap('icon.ico')

ftop = ttk.Frame(root)
fmid = ttk.Frame(root)
fbot = ttk.Frame(root)

ftop.grid(column=0,row =0, sticky="nsew")
fmid.grid(column=0,row =1, sticky="nsew")
fbot.grid(column=0,row =2,sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=2)
root.columnconfigure(0,weight=1)

fmid['borderwidth'] = 2
fmid['relief'] = 'sunken'



def confirm():
    #replace prev prog. with new one
    for widgets in fmid.winfo_children():
        widgets.destroy()

    test_lbl = ttk.Label(fmid)
    test_lbl.grid(column=0, row=0)
    #test_lbl['text'] = f'You selected: {clicked.get()}'
    check_prime_GUI()

def check_prime_GUI():
    #put widgets and algo in the mid frame
    out_lbl = Label(fmid)

    lbl = Label(fmid, text='Number: ')
    lbl.grid(column=0, row=0)

    inputbox=Entry(fmid,textvariable= 0)
    inputbox.grid(column=1, row=0)

    global checking_num
    checking_num = int(inputbox.get())

    chk_btn = ttk.Button(
        fmid,
        text='Check',
        command=check_prime_out(out_lbl))
    chk_btn.grid(column=2, row=0)
    out_lbl.grid()

def check_prime_out(lbl):
    if check_prime(int(checking_num)) is True:
        lbl['text'] = f'{checking_num} is a prime number'
    else:
        lbl['text'] = f'{checking_num} is not a prime number'


    

# label with a specific font
label = Label(ftop, text='Which function to use')
label.grid(column=0, row=0, sticky='W', columnspan= 2)

# program selection
programs = [
    "Check prime",
    "Find prime in a range",
    "Find twin primes",
    "Prime factor" ]

clicked = StringVar()
clicked.set(programs[0])
drop = OptionMenu(ftop, clicked, *programs)
drop.grid(column=0, row=1)

# confirm button
confirm_button = ttk.Button(
    ftop,
    text='Confirm',
    command=confirm)
confirm_button.grid(column=1, row=1)
    
#exit button
exit_button = ttk.Button(
    fbot,
    text='Exit',
    command=lambda: root.quit())

exit_button.place(relx=0.8, rely=0.7)


root.mainloop()
