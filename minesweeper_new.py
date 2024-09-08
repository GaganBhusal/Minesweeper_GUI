from tkinter import *
from tkinter import messagebox
import sys
import random
import time
import loading_screen

(sys.setrecursionlimit(1100))


class Minesweeper:
    non_mines = []
    all_mines = []
    all_objects = []
    all_buttons = []
    opened_buttons = []
    no_of_mines = 25
    total_flags = no_of_mines
    reset_game = False
    location = None
    geometry_height = None
    geometry_width = None
    first_click = False

    def __init__(self, x, y):
        self.current = False
        self.is_checked_once = False
        self.flag_set = False
        self.total = 0
        self.frame_flag = PhotoImage(file='Images/frame_flag.png')
        self.flag = PhotoImage(file='Images/flag.png')
        self.bomb = PhotoImage(file='Images/bomb.png')
        self.box = PhotoImage(file='Images/box.png')
        self.hover_box = PhotoImage(file='Images/hover.png')
        self.O0 = PhotoImage(file='Images/0.png')
        self.O1 = PhotoImage(file='Images/1.png')
        self.O2 = PhotoImage(file='Images/2.png')
        self.O3 = PhotoImage(file='Images/3.png')
        self.O4 = PhotoImage(file='Images/4.png')
        self.O5 = PhotoImage(file='Images/5.png')
        self.O6 = PhotoImage(file='Images/6.png')
        self.O7 = PhotoImage(file='Images/7.png')
        self.O8 = PhotoImage(file='Images/8.png')
        self.counter = 0
        self.is_button_opened = False
        self.current_button = None
        self.is_mine = False
        self.x = x
        self.y = y
        Minesweeper.all_objects.append(self)

    @staticmethod
    def save_no_of_row_and_column(row, column):
        Minesweeper.row = row
        Minesweeper.column = column

    @staticmethod
    def list_of_all_mine_counts_in_game():
        for items in Minesweeper.all_objects:
            a = items.count_total_number_of_mines()
            if items.is_mine:
                a = -2
            items.configure_button_to_show_mines_count(a=a)

    @staticmethod
    def check_win():
        # a = None
        for items in Minesweeper.non_mines:
            if items.is_button_opened:
                Minesweeper.non_mines.remove(items)
        print("The " + str(len(Minesweeper.non_mines)))
        if len(Minesweeper.non_mines) == 0:
            messagebox.showinfo(title='Game Completed', message='Congratulations , You won the game')
            if messagebox.askyesno(title='Play again', message="DO you want to play again?"):
                Minesweeper.choosed_to_change_difficulty(50)
            else:
                messagebox.showinfo(title='Thanks', message='Thanks for playing the game')
                exit()

    def show__________________(self, event):
        if not self.is_button_opened and not self.flag_set:
            self.current_button.configure(image=self.hover_box)

    def show1_________________(self, event):
        if not self.is_button_opened and not self.flag_set:
            self.current_button.configure(image=self.box)

    def creating_boxes(self, location):
        a = Button(location, highlightthickness=0, image=self.box, highlightcolor='red', height=35, width=35,
                   bg='#746D69')
        a.grid(row=self.x, column=self.y)
        a.bind('<Button-1>', self.left_click)
        a.bind('<Button-3>', self.right_click)
        a.bind('<Enter>', self.show__________________)
        a.bind('<Leave>', self.show1_________________)
        Minesweeper.all_buttons.append(a)
        self.current_button = a

    @staticmethod
    def creating_mines(no_of_mines=25):

        print(no_of_mines)
        print(Minesweeper.all_objects)
        print(no_of_mines)
        Minesweeper.all_mines = random.sample(Minesweeper.all_objects, no_of_mines)
        for items in Minesweeper.all_mines:
            items.is_mine = True
        for item in Minesweeper.all_objects:
            if not item.is_mine:
                Minesweeper.non_mines.append(item)

    def show_empty_boxes(self):

        for items in self.checking_boxes_around_current_one():

            items.count_missing_flags()
            items.configure_button_to_show_mines_count(a=items.count_total_number_of_mines())

            for i in items.checking_boxes_around_current_one():
                if i.count_total_number_of_mines() == 0 and not i.is_checked_once and not i.is_mine:
                    i.configure_button_to_show_mines_count(a=i.count_total_number_of_mines())
                    print(f"{i} is opened")

                    i.count_missing_flags()

                    i.is_checked_once = True
                    i.is_button_opened = True

                    i.left_click(event="")
            items.is_button_opened = True

    def left_click(self, event):

        print(f'{self.total_flags} total flags left')
        print('Mine Clicked')
        if self.is_mine:

            self.count_missing_flags()

            self.configure_button_to_show_mines_count(a=-1)
            self.is_checked_once = True
            self.is_button_opened = True

            time.sleep(0.3)
            for item in Minesweeper.all_mines:
                item.is_button_opened = True
                item.is_checked_once = True

                item.configure_button_to_show_mines_count(a=-1)
            time.sleep(0.5)
            self.current_button.configure(image=self.box)

            messagebox.showinfo(title='End!', message="Oops you clicked a mine")
            if messagebox.askyesno(title='Play again', message="DO you want to play again?"):
                Minesweeper.choosed_to_change_difficulty(30)
            else:
                messagebox.showinfo(title='Thanks', message='Thanks for playing the game')
                exit()


        else:

            self.count_missing_flags()
            print(f'{self.total} total')
            self.total += 1
            if self.count_total_number_of_mines() == 0:
                self.show_empty_boxes()
        self.show_number_of_mines_around()
        Minesweeper.opened_buttons.append(self)

        Minesweeper.check_win()

    def right_click(self, event):

        if not self.is_button_opened and not self.flag_set and Minesweeper.total_flags > 0:

            self.flag_set = True
            self.current_button.config(image=self.flag, text="", compound=BOTTOM)
            Minesweeper.total_flags -= 1
            print(f'{self.total_flags} total flags')
            self.show_remaining_flags()
        elif not self.is_button_opened and self.flag_set:
            self.flag_set = False
            Minesweeper.total_flags += 1
            self.current_button.config(image=self.box, text="", compound=BOTTOM)
            self.show_remaining_flags()
        print(f'{self.total_flags} total flags last')

    def configure_button_to_show_mines_count(self, a):
        if a != 0:
            print(f'{a} no of mines')
        if self.is_mine:
            self.current_button.config(image=self.bomb, text="", compound=BOTTOM)
        elif a == 0:
            self.current_button.config(image=self.O0, text="", compound=BOTTOM)
        elif a == 1:
            self.current_button.config(image=self.O1, text="", compound=BOTTOM)
        elif a == 2:
            self.current_button.config(image=self.O2, text="", compound=BOTTOM)
        elif a == 3:
            self.current_button.config(image=self.O3, text="", compound=BOTTOM)
        elif a == 4:
            self.current_button.config(image=self.O4, text="", compound=BOTTOM)
        elif a == 5:
            self.current_button.config(image=self.O5, text="", compound=BOTTOM)
        elif a == 6:
            self.current_button.config(image=self.O6, text="", compound=BOTTOM)
        elif a == 7:
            self.current_button.config(image=self.O7, text="", compound=BOTTOM)
        elif a == 8:
            self.current_button.config(image=self.O8, text="", compound=BOTTOM)

    def show_number_of_mines_around(self):
        self.is_button_opened = True
        if not self.is_mine:
            self.configure_button_to_show_mines_count(a=self.count_total_number_of_mines())

    def checking_boxes_around_current_one(self):
        all_cells = [
            self.return_boxes_around(self.x - 1, self.y - 1),
            self.return_boxes_around(self.x, self.y - 1),
            self.return_boxes_around(self.x + 1, self.y - 1),
            self.return_boxes_around(self.x - 1, self.y),
            self.return_boxes_around(self.x + 1, self.y),
            self.return_boxes_around(self.x - 1, self.y + 1),
            self.return_boxes_around(self.x, self.y + 1),
            self.return_boxes_around(self.x + 1, self.y + 1)

        ]
        all_cells = [items for items in all_cells if items is not None]
        return all_cells

    def count_total_number_of_mines(self):
        self.counter = 0
        list_of_boxes = self.checking_boxes_around_current_one()
        for items in list_of_boxes:
            if items.is_mine == True:
                self.counter += 1
        return self.counter

    def return_boxes_around(self, x, y):
        for items in Minesweeper.all_objects:
            if items.x == x and items.y == y:
                return items

    def count_missing_flags(self):

        if self.flag_set:
            self.flag_set = False
            Minesweeper.total_flags += 1
            self.show_remaining_flags()

    def location__(self, top_location, geometry_height, geometry_width):
        Minesweeper.location = top_location
        Minesweeper.geometry_height = geometry_height
        Minesweeper.geometry_width = geometry_width

    def show_remaining_flags(self):
        c = Label(Minesweeper.location, image=self.frame_flag)
        c.place(x=750, y=30)
        d = Label(Minesweeper.location, width=2, text=f"{Minesweeper.total_flags}", font=('Comic Sans MS', 30),
                  bg='#8f7632')
        d.place(x=820, y=30)

    def reset_buttons(self):
        print(Minesweeper.all_buttons)
        self.current_button.configure(image=self.box)


    @staticmethod
    def choosed_to_change_difficulty(num):
        for all_items in Minesweeper.all_objects:
            Minesweeper.total_flags = num
            all_items.reset_buttons()
            all_items.is_mine = False
            all_items.is_checked_once = False
            all_items.flag_set = False
            all_items.is_button_opened = False

        print(num)
        Minesweeper.reset_game = True
        Minesweeper.creating_mines(num)

    def difficulty_level(self, location, geometry_height, geometry_width):
        f1 = Frame(location, height=geometry_height, width=geometry_width, bg='#12c4c0')
        f1.place(x=0, y=0)

        def create_buttons(text, x, y):
            if text == 'Easy':
                no_of_mines = 30
            elif text == 'Medium':
                no_of_mines = 50
            elif text == 'Hard':
                no_of_mines = 85

            def on_entera(e):
                myButton1['background'] = '#0f9d9a'
                myButton1['foreground'] = '#262626'

            def on_leavea(e):
                myButton1['background'] = '#12c4c0'
                myButton1['foreground'] = '#262626'

            myButton1 = Button(f1, text=text,
                               font=('Comic Sans Ms', 20),
                               width=15,
                               height=2,
                               fg='#262626',
                               border=0,
                               bg='#12c4c0',
                               activeforeground='#262626',
                               activebackground='#0f9d9a',
                               command=lambda: delete(no_of_mines))

            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x, y=y)

        create_buttons('Easy', 100, 0)
        create_buttons('Medium', 400, 0)
        create_buttons('Hard', 700, 0)

        def delete(no_of_mines):
            f1.destroy()
            Minesweeper.total_flags = no_of_mines
            self.show_remaining_flags()
            Minesweeper.choosed_to_change_difficulty(no_of_mines)

        def delete_():
            f1.destroy()

        global close_image
        close_image = PhotoImage(file='close.png')
        Button(f1, image=close_image, command=delete_, bg='#fa434b', border=0, activebackground='#fa434b').place(x=10,
                                                                                                                 y=10)

    def __repr__(self):
        return f"Minesweeper ({self.x},{self.y})"


loading_screen.load_the_screen()


def run():
    if Minesweeper.reset_game:
        Minesweeper.reset_game = False
        run()
    root = Tk()
    root.config(bg='#70942e')
    root.title('Minesweeper(GB)')
    root.resizable(0, 0)
    screen_width = int(root.winfo_screenwidth() // 1.7)
    screen_height = int(root.winfo_screenheight() // 1.7)

    geometry_width = int(screen_width * 1.13)
    geometry_height = int(screen_height * 1.37)
    root.geometry(f"{geometry_width}x{geometry_height}")
    print(screen_width // 35)
    print(screen_height // 35)

    top_frame = Frame(root, height=geometry_height, width=geometry_width, bg='#8f7632')
    Label(top_frame, text='MINESWEEPER', font=('Aerial', 100), bg='green').place(relx=0.5, rely=0.5, anchor=CENTER)
    top_frame.config(bg='#8f7632')
    top_frame.place(x=0, y=0)

    bottom_frame = Frame(root, height=800, width=800)
    bottom_frame.config(bg='#787878', pady=20, padx=20)
    bottom_frame.place(x=0, y=100)

    Minesweeper.save_no_of_row_and_column(screen_width // 35, screen_height // 35)
    for i in range(screen_height // 35):
        for j in range(screen_width // 35):
            mines = Minesweeper(i, j)
            if i == 0 and j == 0:
                mines.location__(top_location=top_frame, geometry_height=geometry_height,
                                 geometry_width=geometry_width)
                mines.show_remaining_flags()
                Button(top_frame, text='Difficulty', font=('Comic Sans Ms', 25), bg='#8f7632',
                       command=lambda: mines.difficulty_level(top_frame, geometry_height, geometry_width)).place(x=10,
                                                                                                                 y=10)

            mines.creating_boxes(bottom_frame)

    Minesweeper.creating_mines()
    root.mainloop()


run()
