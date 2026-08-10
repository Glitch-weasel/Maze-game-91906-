from tkinter import *

root = Tk()
root.geometry("740x740")

placeholder = "light blue"
textholder = ("Arial", 30)

def show_frame(frame):
    frame.tkraise()


class Image_Scroller_Stuff():
    images = [
        "Image 1", "Image 2", "Image 3", "Image 4", "Image 5",
        "Image 6", "Image 7", "Image 8", "Image 9", "Image 10",
        "Image 11", "Image 12", "Image 13", "Image 14", "Image 15",
        "Image 16", "Image 17", "Image 18", "Image 19", "Image 20",
        "Image 21", "Image 22", "Image 23", "Image 24", "Image 25",
        "Image 26", "Image 27", "Image 28", "Image 29", "Image 30"]
    
    current = 0          # Which image is currently selected
    direction = 0        # -1 = left, 1 = right, 0 = stopped
    delay = 800          # Time between image changes (milliseconds)

   

    def image_scroller(images, direction):
        return



class Frames():
    def Main_Menu_Frame():
        Main_Menu = Frame(root,
            bg= placeholder,
            borderwidth= 3)
        Main_Menu.place(x=0, y=0, relwidth=1, relheight=1)

        MM_Title = Label(Main_Menu, text= "Placeholder text (title)", font= textholder)
        MM_Title.place(x= 370, y= 100, anchor= "center")

        MM_NG = Button(Main_Menu, text= "New Game", font= textholder)
        MM_NG.place(x= 370, y= 250, anchor= "center")

        MM_LS = Button(Main_Menu, text= "Level Select", font= textholder, command=lambda: show_frame(level_select))
        MM_LS.place(x= 370, y= 360, anchor= "center")

        MM_Achivements = Button(Main_Menu, text= "Achivements", font= textholder, command=lambda: show_frame(achivements))
        MM_Achivements.place(x= 370, y= 480, anchor= "center")

        MM_Options = Button(Main_Menu, text= "Options", font= textholder)
        MM_Options.place(x= 370, y= 600, anchor= "center")

        MM_Exit = Button(Main_Menu, text= "Exit", font= ("Arial", 25), command= root.destroy)
        MM_Exit.place(x= 650, y= 680, anchor= "center")
        return Main_Menu

    def Level_Select_Frame():

        Level_Select = Frame(root,
            bg= placeholder,
            borderwidth= 3)
        Level_Select.place(x=0, y=0, relwidth=1, relheight=1)

        LS_LI = Label(Level_Select, text=Image_Scroller_Stuff.images[Image_Scroller_Stuff.current], font=("Arial", 30))
        LS_LI.place(x= 370, y= 100, anchor= "center")

        LS_LD = Label(Level_Select, text= "Placeholder", font= ("Arial", 15))
        LS_LD.place(x= 370, y= 300, anchor= "center")

        LS_PL = Button(Level_Select, text= "Play Level", font= textholder)
        LS_PL.place(x= 150, y= 500, anchor= "center")

        LS_IC = Button(Level_Select, text= "Import Custom Level", font= textholder)
        LS_IC.place(x= 500, y= 500, anchor= "center")

        LS_B = Button(Level_Select, text= "Back", font= textholder, command=lambda: show_frame(main_menu))
        LS_B.place(x= 370, y= 650, anchor= "center")

        return Level_Select
    
    def Achivements_Frame():

        Achivements = Frame(root,
            bg= placeholder,
            borderwidth= 3)
        Achivements.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        A_ICO = Label(Achivements, text= "placeholder", font= ("arial", 15))
        A_ICO.place(x= 120, y= 100, anchor= "center")

        A_DESC = Label(Achivements, text= "Placeholder", font= textholder)
        A_DESC.place(x= 370, y= 100, anchor= "center")

        A_LIST = Label(Achivements, text= "placeholder", font= textholder)
        A_LIST.place(x= 250, y= 300, anchor= "center")

        A_SLDR = Label(Achivements, text= "placeholder", font= textholder)
        A_SLDR.place(x= 500, y= 300, anchor= "center")

        A_BCK = Button(Achivements, text= "Back", font= textholder, command=lambda: show_frame(main_menu))
        A_BCK.place(x= 370, y= 500, anchor= "center")

        return Achivements





main_menu = Frames.Main_Menu_Frame()
level_select = Frames.Level_Select_Frame()
achivements = Frames.Achivements_Frame()

show_frame(main_menu)
root.mainloop()