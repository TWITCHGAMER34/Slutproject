import tkinter as tk
import tkinter.font as tkFont

class Game:
    def __init__(self, root):
        #setting title
        root.title("The girl who is missing")
        #setting window size
        width=600
        height=243
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.configure(bg = "#000000")
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_405=tk.Message(root)
        GMessage_405["anchor"] = "center"
        GMessage_405["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GMessage_405["font"] = ft
        GMessage_405["fg"] = "#ffffff"
        GMessage_405["justify"] = "center"
        GMessage_405["text"] = "The girl who is missing"
        GMessage_405.place(x=110,y=20,width=357,height=90)

        start=tk.Button(root)
        start["activebackground"] = "#474747"
        start["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        start["font"] = ft
        start["fg"] = "#ffffff"
        start["justify"] = "center"
        start["text"] = "Klick here to play!"
        start.place(x=240,y=140,width=118,height=52)
        start["command"] = self.start

        GButton_701=tk.Button(root)
        GButton_701["activebackground"] = "#000000"
        GButton_701["activeforeground"] = "#ffffff"
        GButton_701["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_701["font"] = ft
        GButton_701["fg"] = "#ffffff"
        GButton_701["justify"] = "center"
        GButton_701["text"] = "Quit!"
        GButton_701.place(x=0,y=200,width=94,height=36)
        GButton_701["command"] = self.GButton_701_command

    def window(self):
        root = tk.Tk()
        root.title("The girl who got missing")
        #setting window size
        width=600
        height=243
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.configure(bg = "#000000")
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

    def Game_0(self):
        self.window()
        root.destroy()



    def start(self):
        self.Game_0()

    def GButton_701_command(self):
        quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()
