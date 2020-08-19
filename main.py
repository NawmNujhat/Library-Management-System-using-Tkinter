from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *

mypass="Na8*m"
mydatabase="library"

con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()

root = Tk()
root.title("CSEDU Library")
root.minsize(width=400,height=400)
root.geometry("1000x1000")
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("lib.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(root)
e.pack(fill=BOTH, expand=YES)
headingFrame1=Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel=Label(headingFrame1,text="Welcome to CSEDU Library",bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
btn1=Button(root,text="Add Book Details",bg='black',fg='white',command=addBook)
btn1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
btn2=Button(root,text="Delete Book",bg='black',fg='white')
btn2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)
btn3=Button(root,text="View Books",bg='black',fg='white')
btn3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
btn4=Button(root,text="Issue Book to Student",bg='black',fg='white')
btn4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)
btn5=Button(root,text="Return Books",bg='black',fg='white')
btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)


root.mainloop()