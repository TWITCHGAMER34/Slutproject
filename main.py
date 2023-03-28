"""
This is the main file of the game
"""
import random
import tkinter as tk
import tkinter.font as tkFont
import random


class Game:
    def __init__(self, root):
        # setting title
        root.title("The girl who is missing")
        # setting window size
        width = 1200
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.configure(bg="#000000")
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_405 = tk.Message(root)
        GMessage_405["anchor"] = "center"
        GMessage_405["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=50, weight="bold", slant="italic", underline=True)
        GMessage_405["font"] = ft
        GMessage_405["fg"] = "#ffffff"
        GMessage_405["justify"] = "center"
        GMessage_405["width"] = 1000
        GMessage_405["text"] = "The girl who is missing"
        GMessage_405.place(x=110, y=100, width=1000, height=90)

        start = tk.Button(root)
        start["activebackground"] = "#474747"
        start["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=10)
        start["font"] = ft
        start["fg"] = "#ffffff"
        start["justify"] = "center"
        start["text"] = "Klick here to play!"
        start.place(x=500, y=200, width=200, height=100)
        start["command"] = self.start

        quit = tk.Button(root)
        quit["activebackground"] = "#000000"
        quit["activeforeground"] = "#ffffff"
        quit["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times', size=10)
        quit["font"] = ft
        quit["fg"] = "#ffffff"
        quit["justify"] = "center"
        quit["text"] = "Quit!"
        quit.place(x=0, y=550, width=150, height=50)
        quit["command"] = self.quit

    def window(self):
        """

        :return:
        """
        root = tk.Tk()
        root.title("The girl who got missing")
        # setting window size
        width = 600
        height = 243
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.configure(bg="#000000")
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

    def setupText(self, input, fontsize, fg):
        """

        :param input:
        :return:
        """
        text = tk.Message(root)
        text["anchor"] = "center"
        text["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=fontsize)
        text["font"] = ft
        text["fg"] = fg
        text["justify"] = "center"
        text["width"] = 300
        text["text"] = input
        return text

    def setupButton(self, input, command, fontsize):
        """

        :param input:
        :return:
        """
        button = tk.Button(root)
        button["activebackground"] = "#474747"
        button["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=fontsize)
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

    def destroy(self):  # destroy all widgets
        """

        :return:
        """
        for child in root.winfo_children():
            child.destroy()

    def zdead(self):
        self.destroy()
        GMessage_405 = self.setupText('You died', fontsize=40, fg="red")
        GMessage_405.place(x=400, y=50, width=357, height=120)

        GButton_0 = self.setupButton('next', self.main, fontsize=20)
        GButton_0.place(x=520, y=350, width=118, height=52, )

    def main(self):
        self.destroy()  # destroy all widgets
        GMessage_405 = self.setupText('How old are you?', fontsize=20, fg="white")
        GMessage_405.place(x=140, y=50, width=357, height=120)

        Gmessage_406 = self.setupText('Whats your name?', fontsize=20, fg="white")
        Gmessage_406.place(x=650, y=50, width=357, height=120)

        self.GEntry_1 = self.setupEntry()
        self.GEntry_1.place(x=780, y=140, width=118, height=52)

        self.GEntry_0 = self.setupEntry()
        self.GEntry_0.place(x=240, y=140, width=118, height=52)

        GButton_0 = self.setupButton('next', self.state2, fontsize=20)
        GButton_0.place(x=500, y=350, width=118, height=52, )

    def state2(self):
        input = self.GEntry_0.get()
        input2 = self.GEntry_1.get()
        self.destroy()

        GMessage_405 = self.setupText(f'Hello %s, you are %s years old, correct?' % (input2, input), fontsize=30, fg="white")
        GMessage_405.place(x=400, y=20, width=357, height=300)

        GButton_0 = self.setupButton('Yes', self.state3, fontsize=20)
        GButton_0.place(x=450, y=350, width=118, height=52)

        GButton_1 = self.setupButton('No', self.main, fontsize=20)
        GButton_1.place(x=600, y=350, width=118, height=52)

    def state3(self):
        self.destroy()
        GMessage_405 = self.setupText(
            'You wake up in a dark room, you dont know where you are or how you got here, you see a door in front of '
            'you, to your right and to your left, choose a door.',
            fontsize=33, fg="white")
        GMessage_405.place(x=-250, y=10, width=1100, height=600)

        GButton_0 = self.setupButton('Open the door infront of you', self.state4, fontsize=15)
        GButton_0.place(x=500, y=200, width=300, height=50)

        GButton_1 = self.setupButton('Open the door to your right', self.state5, fontsize=15)
        GButton_1.place(x=500, y=300, width=300, height=50)

        GButton_2 = self.setupButton('Open the door to your left', self.state6, fontsize=15)
        GButton_2.place(x=500, y=100, width=300, height=50)

    def state4(self):
        self.destroy()
        GMessage_405 = self.setupText(
            'You open the door in-front of you, you see a staircase, you go up the stairs and you see a door, you open '
            'the door and you see a room with a table and a chair, you sit down and you see a piece of paper on the '
            'table, you pick it up and it says "You are in a room, you have to find a way out, you can go up the stairs'
            'or you can go down the stairs, choose wisely"',
            fontsize=20, fg="white")
        GMessage_405.place(x=-250, y=20, width=1000, height=600)

        GButton_0 = self.setupButton('Go up the stairs', self.state7, fontsize=20)
        GButton_0.place(x=500, y=150, width=300, height=52)

        GButton_1 = self.setupButton('Go down the stairs', self.state8, fontsize=20)
        GButton_1.place(x=500, y=250, width=300, height=52)

    def state5(self):
        self.destroy()
        GMessage_405 = self.setupText("""You open the door on the right hand side of you,
         and step into a dimly lit room. The air is heavy with the stench of rot and decay, and the walls are lined with
         shelves containing jars filled with strange, twisted specimens.
         As you make your way further into the room, you notice movement out of the corner of your eye. You turn to see 
         a grotesque figure slowly emerging from the shadows. Its skin is mottled and decaying, its eyes sunken and life
         less. It lurches towards you, emitting a low, guttural growl. 
         Your heart races as you realize that you are face to face with a zombie. You try to back away, but your foot 
         catches on a loose floorboard and you stumble backwards, falling to the ground.
         """,
         fontsize=15, fg="white")
        GMessage_405.place(x=50, y=20, width=500, height=600)
        GMessage_406 = self.setupText("""
         The zombie closes in on you, its fingers clawing at the air. You scramble backwards, desperately searching for 
         a way out. As you look around, you notice that the jars on the shelves are shaking and rattling, and something 
         inside them is moving. 
         With a sickening realization, you realize that the jars contain other undead creatures, waiting to be unleashed 
         upon the living. As the zombie draws nearer, you know that your only chance for survival is to fight your way 
         out of the room before the other creatures are released. 
         Your heart pounding, you scramble to your feet and race towards the door. The zombie is hot on your heels, its 
         breath rancid and putrid. You slam the door shut, but it is no match for the zombie's strength. The creature 
         slams into the door, sending splinters flying.
         You turn to run, but you realize that you are trapped. The zombie has blocked your only exit. As the creature 
         reaches out to grab you, you close your eyes and brace for impact, praying that someone, anyone, will come to 
         your rescue.""", fontsize=13, fg="white")
        GMessage_406.place(x=450, y=0, width=400, height=600)

        GButton_0 = self.setupButton('Fight the zombie', self.fzombie, fontsize=20)
        GButton_0.place(x=850, y=250, width=300, height=52)

    def state6(self):
        pass

    def fzombie(self):
        k = random.randint(1, 2)
        if k == 1:
            self.state7()
        else:
            self.zdead()


    def state7(self):
        pass

    def state8(self):
        pass

    def state9(self):
        pass

    def start(self):
        self.main()

    def quit(self):
        quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()
