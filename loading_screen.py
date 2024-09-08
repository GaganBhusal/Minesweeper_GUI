from tkinter import *

def load_the_screen():

    bg = '#0d3320'
    import time


    root = Tk()
    width = 500
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width/2)
    y_coordinate = (screen_height/2)-(height/2)
    root.geometry(f'{width}x{height}+{500}+{250}')
    c1 = PhotoImage(file='Images/c1.png')
    c2 = PhotoImage(file='Images/c2.png')
    root.overrideredirect(True) #for hiding titlebar

    # def new_window():
    #     root_1 = Tk()
    #     root_1.mainloop()
        # root_1.mainloop()

    Frame(root, width=500, height=300, bg=bg).place(x=0,y=0)
    root.config(bg='#272727')
    label1 = Label(root, text='MINESWEEPER', fg='white', bg=bg,font=('Game of Squids',25))
    label1.place(relx=0.5 ,rely=0.5,anchor=CENTER)

    label2 = Label(root, text='Loading...', fg='white', bg=bg)
    label2.place(x=20, y=270)

    for i in range(1):
        l1 = Label(root, image=c2, border=0, relief=SUNKEN).place(x=220, y=170)
        l2 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=240, y=170)
        l3 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=260, y=170)
        l4 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=280, y=170)
        root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=220, y=170)
        l2 = Label(root, image=c2, border=0, relief=SUNKEN).place(x=240, y=170)
        l3 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=260, y=170)
        l4 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=280, y=170)
        root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=220, y=170)
        l2 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=240, y=170)
        l3 = Label(root, image=c2, border=0, relief=SUNKEN).place(x=260, y=170)
        l4 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=280, y=170)
        root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=220, y=170)
        l2 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=240, y=170)
        l3 = Label(root, image=c1, border=0, relief=SUNKEN).place(x=260, y=170)
        l4 = Label(root, image=c2, border=0, relief=SUNKEN).place(x=280, y=170)
        root.update_idletasks()
        time.sleep(0.5)



    root.destroy()
    # new_window()
    root.mainloop()

