"""
This is the main file of the game
"""

import tkinter as tk
import tkinter.font as tkFont

class Game:
    def __init__(self, root):
        #setting title
        root.title("The girl who is missing")
        #setting window size
        width=1200
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.configure(bg = "#000000")
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_405=tk.Message(root)
        GMessage_405["anchor"] = "center"
        GMessage_405["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=50, weight="bold", slant="italic", underline=True)
        GMessage_405["font"] = ft
        GMessage_405["fg"] = "#ffffff"
        GMessage_405["justify"] = "center"
        GMessage_405["width"] = 1000
        GMessage_405["text"] = "The girl who is missing"
        GMessage_405.place(x=110,y=100,width=1000,height=90)

        start=tk.Button(root)
        start["activebackground"] = "#474747"
        start["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        start["font"] = ft
        start["fg"] = "#ffffff"
        start["justify"] = "center"
        start["text"] = "Klick here to play!"
        start.place(x=500,y=200,width=200,height=100)
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
        GButton_701.place(x=0,y=550,width=150,height=50)
        GButton_701["command"] = self.GButton_701_command

    def window(self):
        """

        :return:
        """
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

    def setupText(self, input):
        """

        :param input:
        :return:
        """
        text = tk.Message(root)
        text["anchor"] = "center"
        text["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=28)
        text["font"] = ft
        text["fg"] = "#ffffff"
        text["justify"] = "center"
        text["width"] = 300
        text["text"] = input
        return text

    def setupButton(self, input, command):
        """

        :param input:
        :return:
        """
        button = tk.Button(root)
        button["activebackground"] = "#474747"
        button["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=10)
        button["font"] = ft
        button["fg"] = "#ffffff"
        button["justify"] = "center"
        button["text"] = input
        button["command"] = command

        return button

    def setupEntry(self):
        """

        :param input:
        :return:
        """
        entry = tk.Entry(root)
        entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entry["font"] = ft
        entry["fg"] = "#000000"
        entry["justify"] = "center"

        return entry

    def destroy(self): #destroy all widgets
        """

        :return:
        """
        for child in root.winfo_children():
            child.destroy()



    def main(self):
        self.destroy() #destroy all widgets
        GMessage_405 = self.setupText('How old are you?')
        GMessage_405.place(x=110,y=20,width=357,height=120)

        self.GEntry_0 = self.setupEntry()
        self.GEntry_0.place(x=240,y=140,width=118,height=52)

        GButton_0 = self.setupButton('next', self.state2)
        GButton_0.place(x=240,y=200,width=118,height=52)




    def state2(self):
        input = self.GEntry_0.get()
        self.destroy()

        GMessage_405 = self.setupText(f"Hello bob, you are %s years old" % (input))
        GMessage_405.place(x=110,y=20,width=357,height=120)



    def start(self):
        self.main()

    def GButton_701_command(self):
        quit()



if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()
