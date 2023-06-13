## Importing Libraries
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from datetime import date
import pandas as pd

## SETTING UP THE GUI


## creating the class for the checkbox
class CheckButton_Wrapper:
    def __init__(self,text,parent,grid_row,grid_col,function):
        self.text = text
        self.var = IntVar()
        self.row = grid_row
        self.col = grid_col
        self.parent = parent
        self.function = function
        self.checkbutton = Checkbutton(master = self.parent,text=self.text,anchor="w",variable=self.var,command=lambda:self.function(self))
        self.checkbutton.grid(row=self.row,column=self.col,sticky="ew")
        self.addlist = checkboxes.append(self)
    
    def uncheck(self):
        self.var.set(0)
        
##----------------------------- MAIN WINDOW
root = Tk()
root.geometry("850x700")
root.resizable(False,False)

##----------------------------- HEADER

lbl_head = ttk.Label(root,text="Book Tracker",anchor="w",font=("Arial Black",20,"bold"),background="skyblue")
lbl_head.pack(fill=BOTH,padx=5,pady=0)

lbl_subhead = ttk.Label(root,text="Made with Python and Tkinter",anchor="w",font=("Noto Mono",8))
lbl_subhead.pack(fill=BOTH,padx=5,pady=0)

lbl_date = ttk.Label(root,text=date.today().strftime("%d %B %Y"),anchor="w",font=("Noto",7,"italic"))
lbl_date.pack(fill=BOTH,padx=5,pady=0)

##----------------------------- ADDING NEW BOOKS: INPUT SECTION

lfrm_addbooks = LabelFrame(root,text="Add Books",relief=GROOVE,borderwidth=5,font=("Noto",12),padx=20,pady=10)

lbl_addtitle = ttk.Label(lfrm_addbooks,text="Title",anchor="w",width=30)
lbl_addtitle.grid(row=0,column=0,sticky="w")

ent_addtitle = ttk.Entry(lfrm_addbooks,width=60)
ent_addtitle.grid(row=0,column=1,sticky="w")

lbl_addauthor = ttk.Label(lfrm_addbooks,text="Author(s)",anchor="w",width=30)
lbl_addauthor.grid(row=1,column=0,sticky="w")

ent_addauthor = ttk.Entry(lfrm_addbooks,width=60)
ent_addauthor.grid(row=1,column=1,sticky="w")

##----------------------------- ADDING NEW BOOKS: CATEGORIES

## declaring variables
global categories
categories = []
global checkboxes
checkboxes = []
var = IntVar()
book_categories = ["Non-fiction","Fiction","Reference","Novel","Journal","Others"]
genrelist = ["Political","Fantasy","Horror","Science Fiction","Dystopian","Mystery","Thriller","Historical","Romance","Graphic Novel","Young Adult","Children's","Biography","Art and Humanities","Self-help","Travel","Crime","Comedy","Textbook"]
genrelist.sort()
global genres
genres = []

## setting up function for storing categories in a list.
def addcategory(checkbutton):
    value = checkbutton.var.get()
    if value == 1:
        categories.append(checkbutton.text)
        print(categories)
    else:
        categories.remove(checkbutton.text)
        print(categories)


## setting up the frames
lfrm_category = LabelFrame(lfrm_addbooks,text="Choose the book's category.")
lfrm_category.columnconfigure((0,1,2),weight=1,uniform="equal")

for i,category in enumerate(book_categories):
    row = i // 3
    col = i % 3
    chk_category = CheckButton_Wrapper(text=category,parent=lfrm_category,grid_row=row,grid_col=col,function=addcategory)

lfrm_category.grid(row=2,column=0,columnspan=3,sticky="ew")

##----------------------------- ADDING NEW BOOKS: GENRES

def addgenre(checkbutton):
    value = checkbutton.var.get()
    if value == 1:
        genres.append(checkbutton.text)
        print(genres)
    else:
        genres.remove(checkbutton.text)
        print(genres)

lfrm_genre = LabelFrame(lfrm_addbooks,text="Choose the book's genre.")
lfrm_genre.columnconfigure((0,1,2,3,4,5),weight=1,uniform="equal")

for i, genre in enumerate(genrelist):
    row = i // 6
    col = i % 6
    chk_genre = CheckButton_Wrapper(parent=lfrm_genre,text=genre,grid_row=row,grid_col=col,function=addgenre)

lfrm_genre.grid(row=3,column=0,columnspan=3,sticky="ew")

##----------------------------- ADDING NEW BOOKS: BUTTON

def addNewBook():
    title = ent_addtitle.get()
    author = ent_addauthor.get()

    ## Check for data validation

    if (title == "") or (author == ""):
        messagebox.showwarning("Invalid input","One of the required fields is empty.")
        return

    date_today = date.today().strftime("%d %B %Y")
    tbl_books.insert("", "end", values=(title, author, date_today, categories, genres))
    messagebox.showinfo("New book added","The new book recorded has been added.")
    ## clearing the values
    ent_addtitle.delete(0,END)
    ent_addauthor.delete(0,END)
    genres.clear()
    categories.clear()
    for checkbox in checkboxes:
        checkbox.uncheck()

btn_addbook = ttk.Button(lfrm_addbooks,text="Add Book",padding=5,command=addNewBook)
btn_addbook.grid(row=4,column=0,sticky="w",padx=(0,12),pady=12)

##----------------------------- ADDING NEW BOOKS: TABLES

tbl_books = ttk.Treeview(lfrm_addbooks)

tbl_books["columns"] = ("Title","Author","Date Added","Category","Genres")

for col in tbl_books["columns"]:
    tbl_books.column(col,width=6)
    tbl_books.heading(col,text=col)
tbl_books.column("#0",width=0,stretch=NO)

tbl_books.grid(row=5,column=0,columnspan=3,sticky="ew")

lfrm_addbooks.pack(pady=30)

root.mainloop()