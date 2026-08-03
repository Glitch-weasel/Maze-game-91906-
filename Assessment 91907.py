from tkinter import *

root = Tk()
root.geometry("640x480")

placeholder = "light blue"
textholder = ("Arial", 30)

Main_Menu = Frame(root,
    bg=placeholder,
    borderwidth=3)
Main_Menu.pack(padx=20, pady=20)

MM_Title = Label(Main_Menu, text= "Placeholder text (title)", font= textholder)
MM_Title.grid(row= 0, column= 1)

MM_NG = Button(Main_Menu, text= "New Game", font= textholder)
MM_NG.grid(row= 1, column= 1)

MM_LS = Button(Main_Menu, text= "Level Select")
MM_LS.grid(row= 2, column= 1)

MM_Achivements = Button(Main_Menu, text= "Achivements")
MM_Achivements.grid(row= 3, column= 1)

MM_Options = Button(Main_Menu, text= "Options")
MM_Options.grid(row= 4, column=1)




root.mainloop()