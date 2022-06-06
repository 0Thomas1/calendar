from main import *
from tkinter import *
from tkinter import ttk

def confirm():
    #replace prev prog. with new one
    c1 = clicked.get()
    if c1 == programs[0]:
        check_prime_GUI()
    elif c1 == programs[1]:
        find_prime_GUI()
    elif c1 == programs[2]:
        find_twin_prime_GUI()
    elif c1 == programs[3]:
        find_prime_factor_GUI()

    
    
    """for i in range(len(programs)):
        if clicked.get() is programs[i]:
            pass
    """

def check_prime_GUI():
    # put widgets and algo in the mid frame
    fmid['text'] = 'Prime number check'
    for widgets in fmid.winfo_children():
        widgets.destroy()
        
    out_lbl = Label(fmid)
    out_lbl['text']=''
    # num lbl
    lbl = Label(fmid, text='Number: ')
    lbl.grid(column=0, row=0)

    # Entry widget
    inputbox=Entry(fmid)
    inputbox.grid(column=1, row=0, padx=2, pady=2)
    inputbox.focus()

    # check button
    chk_btn = ttk.Button(
        fmid,
        text='Check',
        command=lambda: check_prime_out(inputbox.get(), out_lbl))
    chk_btn.grid(column=2, row=0)

    #clear button
    clr_btn = ttk.Button(
        fmid,
        text='Clear',
        command=check_prime_GUI)
    clr_btn.grid(column=2,row=1)
    out_lbl.grid(column=0, row=1, columnspan=2, sticky='W')

def check_prime_out(num, lbl):
    if check_prime(int(num)) is True:
        lbl['text'] = f'{num} is a prime number'
    else:
        lbl['text'] = f'{num} is not a prime number'

def find_prime_GUI():
    #GUI for find prime
    fmid['text'] = 'Find prime numbers'
    for widgets in fmid.winfo_children():
        widgets.destroy()

    # col 0 labels 
    lower_lbl = Label(fmid, text='Lower range: ')
    lower_lbl.grid(column=0, row=0)

    higher_lbl = Label(fmid, text='Higher range: ')
    higher_lbl.grid(column=0, row=1)

    # col 1 entries
    lower_e = Entry(fmid)
    lower_e.grid(column=1, row=0)

    higher_e = Entry(fmid)
    higher_e.grid(column=1, row=1)

     #output
    out_lbl = Label(fmid, text= 'Prime Numbers: ')
    out_lbl.grid( column=0, row=2)

    out_e = Text(fmid,height=8, width=55)
    out_e.grid(column=0, row=3, columnspan=3)

    # col 2 btns
    # check button
    find_btn = ttk.Button(
        fmid,
        text='Find',
        command=lambda: find_prime_out(lower_e.get(), higher_e.get(),out_e))
    find_btn.grid(column=2, row=0)

    #clear button
    clr_btn = ttk.Button(
        fmid,
        text='Clear',
        command=find_prime_GUI)
    clr_btn.grid(column=2,row=1)
    
   
def find_prime_out(lwr, hgr, output):
    out = find_prime(int(lwr), int(hgr))
    for number in out:
        if number is out[-1]:
            output.insert('1.end', str(number))
        else:
            output.insert('1.end', str(number) + ', ')
    output['state'] = 'disable' 

def find_twin_prime_GUI():
    #GUI for find prime
    fmid['text'] = 'Find twin prime numbers'
    for widgets in fmid.winfo_children():
        widgets.destroy()

    # col 0 labels 
    lower_lbl = Label(fmid, text='Lower range: ')
    lower_lbl.grid(column=0, row=0)

    higher_lbl = Label(fmid, text='Higher range: ')
    higher_lbl.grid(column=0, row=1)

    # col 1 entries
    lower_e = Entry(fmid)
    lower_e.grid(column=1, row=0)

    higher_e = Entry(fmid)
    higher_e.grid(column=1, row=1)

     #output
    out_lbl = Label(fmid, text= 'Prime Numbers: ')
    out_lbl.grid( column=0, row=2)

    out_e = Text(fmid,height=8, width=55)
    out_e.grid(column=0, row=3, columnspan=3)
    out_e['state'] = 'disable'

    # col 2 btns
    # check button
    find_btn = ttk.Button(
        fmid,
        text='Find',
        command=lambda: find_twin_prime_out(lower_e.get(), higher_e.get(),out_e))
    find_btn.grid(column=2, row=0)

    #clear button
    clr_btn = ttk.Button(
        fmid,
        text='Clear',
        command=find_twin_prime_GUI)
    clr_btn.grid(column=2,row=1)

def find_twin_prime_out(lwr, hgr, output):
    output['state'] = 'normal'
    output.delete('1.0', END)
    out = find_prime(int(lwr), int(hgr))
    for number in out:
        if number is out[-1]:
            output.insert('1.end', str(number))
        else:
            output.insert('1.end', str(number) + ', ')

    output['state'] = 'disable' 

def find_prime_factor_GUI():
    # put widgets and algo in the mid frame
    fmid['text'] = 'Find prime factor'
    for widgets in fmid.winfo_children():
        widgets.destroy()
        
    # num lbl
    lbl = Label(fmid, text='Number: ')
    lbl.grid(column=0, row=0)

    # Entry widget
    inputbox=Entry(fmid)
    inputbox.grid(column=1, row=0, padx=2, pady=2)
    inputbox.focus()

    # check button
    chk_btn = ttk.Button(
        fmid,
        text='Check',
        command=lambda: find_prime_factor_out(inputbox.get(), out_e))
    chk_btn.grid(column=2, row=0)

    #clear button
    clr_btn = ttk.Button(
        fmid,
        text='Clear',
        command=find_prime_factor_GUI)
    clr_btn.grid(column=2,row=1)

      #output
    out_lbl = Label(fmid, text= 'Prime Numbers: ')
    out_lbl.grid( column=0, row=2)

    out_e = Text(fmid,height=8, width=55)
    out_e.grid(column=0, row=3, columnspan=3)
    out_e['state'] = 'disable'

def find_prime_factor_out(num,output):
    output['state'] = 'normal'
    output.delete('1.0', END)
    out = prime_factor(int(num))
    if len(out) == 0:
        output.insert('1.end', 'This Number Does not have 2 prime factors.')
        return
    for number in out:
        if number is out[-1]:
            output.insert('1.end', str(number))
        else:
            output.insert('1.end', str(number) + ', ')
    output['state'] = 'disable' 
    


# window
root = Tk()
root.geometry('450x300')
root.resizable(False, False)
root.title('Prime Number App')
root.attributes('-topmost', 1)
root.iconbitmap('icon.ico')

#  the frames
ftop = ttk.Frame(root)
fmid = ttk.LabelFrame(root)
fbot = ttk.Frame(root)

ftop.grid(column=0,row =0, sticky="nsew")
fmid.grid(column=0,row =1, sticky="nsew")
fbot.grid(column=0,row =2,sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=2)
root.columnconfigure(0,weight=1)

fmid['borderwidth'] = 2
#fmid['relief'] = 'sunken'
    


    

# label with a specific font
label = Label(ftop, text='Which function to use')
label.grid(column=0, row=0, sticky='W', columnspan= 2)

# program selection (Drop down box)
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
    
# exit button
exit_button = ttk.Button(
    fbot,
    text='Exit',
    command=lambda: root.quit())
ph1 = Label(fbot).grid(column=0, row=0)
ph2 = Label(fbot).grid(column=0, row=1)
exit_button.grid(column=3,row=3)


root.mainloop()
