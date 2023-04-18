"""
This is the main file of the game
"""
import os
import random
import sys
import tkinter as tk
import tkinter.font as tk_font
import json
import requests



def jokes(f):
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

link = r"https://official-joke-api.appspot.com/random_joke"
joke= jokes(link)


def window():
    """
    :return:
    """
    root_el = tk.Tk()
    root_el.title("The girl who got missing")
    # setting window size
    width = 600
    height = 243
    screenwidth = root_el.winfo_screenwidth()
    screenheight = root_el.winfo_screenheight()
    align_str = f'{width:d}x{height:d}+{(screenwidth - width) / 2:d}' \
                f'+{(screenheight - height) / 2:d}'

    root_el.configure(bg="#000000")
    root_el.geometry(align_str)
    root_el.resizable(width=False, height=False)




def setup_button(input_el, callback, font_size):
    """

    :param font_size:
    :param callback:
    :param input_el:
    :return:
    """
    button = tk.Button(root)
    button["activebackground"] = "#474747"
    button["bg"] = "#000000"
    font = tk_font.Font(family='Times', size=font_size)
    button["font"] = font
    button["fg"] = "#ffffff"
    button["justify"] = "center"
    button["text"] = input_el
    button["command"] = callback

    return button


def setup_entry():
    """
    :return:
    """
    entry = tk.Entry(root)
    entry["borderwidth"] = "1px"
    font = tk_font.Font(family='Times', size=10)
    entry["font"] = font
    entry["fg"] = "#000000"
    entry["justify"] = "center"

    return entry


def destroy():  # destroy all widgets
    """

    :return:
    """
    for child in root.winfo_children():
        child.destroy()


def setup_text(input_el, font_size, f_g):
    """
    :param f_g:
    :param font_size:
    :param input_el:
    :return:
    """
    text = tk.Message(root)
    text["anchor"] = "center"
    text["bg"] = "#000000"
    font = tk_font.Font(family='Times', size=font_size)
    text["font"] = font
    text["fg"] = f_g
    text["justify"] = "center"
    text["width"] = 300
    text["text"] = input_el
    return text


def quit_program():
    """
    :return:
    """
    sys.exit()


class Setup:
    """
    This class is used to set up the game and the GUI for the game to work properly and to be able to run the game.
    """

    def __init__(self, root_el, states_el):
        self.entry2 = None
        self.entry1 = None
        self.name = None
        self.states = states_el
        # setting title
        root_el.title("The scary story")
        # setting window size
        width = 1200
        height = 600
        screenwidth = root_el.winfo_screenwidth()
        screenheight = root_el.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                     (screenheight - height) / 2)
        root_el.configure(bg="#000000")
        root_el.geometry(align_str)
        root_el.resizable(width=False, height=False)

        title = tk.Message(root_el)
        title["anchor"] = "center"
        title["bg"] = "#000000"
        font = tk_font.Font(family='Times', size=50, weight="bold", slant="italic", underline=True)
        title["font"] = font
        title["fg"] = "#ffffff"
        title["justify"] = "center"
        title["width"] = 1000
        title["text"] = "The scary story"
        title.place(x=110, y=100, width=1000, height=90)

        start = tk.Button(root_el)
        start["activebackground"] = "#474747"
        start["bg"] = "green"
        font = tk_font.Font(family='Times', size=15)
        start["font"] = font
        start["fg"] = "#ffffff"
        start["justify"] = "center"
        start["text"] = "Klick here to play!"
        start.place(x=500, y=200, width=200, height=100)
        start["command"] = self.start

        quit_el = tk.Button(root_el)
        quit_el["activebackground"] = "#000000"
        quit_el["activeforeground"] = "#ffffff"
        quit_el["bg"] = "#ff0000"
        font = tk_font.Font(family='Times', size=10)
        quit_el["font"] = font
        quit_el["fg"] = "#ffffff"
        quit_el["justify"] = "center"
        quit_el["text"] = "Quit!"
        quit_el.place(x=0, y=550, width=150, height=50)
        quit_el["command"] = quit_program

        jOke = setup_text(f'Joke of the day: \n {joke["setup"]} \n{joke["punchline"]}', font_size=15, f_g="white")
        jOke.place(x=0, y=400, width=1200, height=150)

    def start(self):
        """

        :return:
        """
        self.main()

    def main(self):
        """

        :return:
        """
        destroy()  # destroy all widgets
        alder = setup_text('How old are you?', font_size=20, f_g="white")
        alder.place(x=140, y=50, width=357, height=120)

        namn = setup_text('Whats your name?', font_size=20, f_g="white")
        namn.place(x=650, y=50, width=357, height=120)

        self.entry1 = setup_entry()
        self.entry1.place(x=780, y=140, width=118, height=52)

        self.entry2 = setup_entry()
        self.entry2.place(x=240, y=140, width=118, height=52)

        knapp1 = setup_button('next', self.confirm_main, font_size=20)
        knapp1.place(x=500, y=350, width=118, height=52, )

    def confirm_main(self):
        """

        :return:
        """
        alder = self.entry1.get()
        namn = self.entry2.get()
        destroy()

        state2text = setup_text(f'Hello {alder}, you are {namn} years old, correct?', font_size=30, f_g="white")
        state2text.place(x=400, y=20, width=357, height=300)

        state2knapp = setup_button('Yes', self.states.state3, font_size=20)
        state2knapp.place(x=450, y=350, width=118, height=52)

        state2knapp1 = setup_button('No', self.main, font_size=20)
        state2knapp1.place(x=600, y=350, width=118, height=52)
        with open('temp.txt', 'w', encoding="utf-8") as file:
            file.write(namn)


class States(Setup):
    """
    Detta är en klass som ärver från Setup klassen och innehåller alla states som finns i spelet. Denna klassen är
    kopplad till Setup klassen och använder sig av dess metoder.
    """

    def __init__(self, root_el):
        super().__init__(root_el, self)

    def zdead(self):
        """

        :return:
        """
        destroy()
        print("You died")
        ztext = setup_text('You died', font_size=40, f_g="red")
        ztext.place(x=400, y=50, width=357, height=120)

        z_knapp = setup_button('next', self.main, font_size=20)
        z_knapp.place(x=520, y=350, width=118, height=52, )

    def state3(self):
        """

        :return:
        """
        destroy()
        state3text = setup_text(
            'You wake up in a dark room, you dont know where you are or how you got here, you see a door in front of '
            'you, to your right and to your left, choose a door.',
            font_size=33, f_g="white")
        state3text.place(x=-250, y=10, width=1100, height=600)

        state3knapp = setup_button('Open the door infront of you', self.state4, font_size=15)
        state3knapp.place(x=500, y=200, width=300, height=50)

        state3knapp1 = setup_button('Open the door to your right', self.state5, font_size=15)
        state3knapp1.place(x=500, y=300, width=300, height=50)

        state3knapp2 = setup_button('Open the door to your left', self.state6, font_size=15)
        state3knapp2.place(x=500, y=100, width=300, height=50)

    def state4(self):
        """

        :return:
        """
        destroy()
        state4text = setup_text(
            'You open the door in-front of you, you see a staircase, you go up the stairs and you see a door, you open '
            'the door and you see a room with a table and a chair, you sit down and you see a piece of paper on the '
            'table, you pick it up and it says "You are in a room, you have to find a way out, you can go up the stairs'
            'or you can go down the stairs, choose wisely"',
            font_size=20, f_g="white")
        state4text.place(x=-250, y=20, width=1000, height=600)

        state4knapp = setup_button('Go up the stairs', self.state7, font_size=20)
        state4knapp.place(x=500, y=150, width=300, height=52)

        state4knapp1 = setup_button('Go down the stairs', self.state8, font_size=20)
        state4knapp1.place(x=500, y=250, width=300, height=52)

    def state5(self):
        """

        :return:
        """
        destroy()
        state5text = setup_text("""You open the door on the right hand side of you, and step into a dimly lit room.
        The air is heavy with the stench of rot and decay, and the walls are lined with shelves containing jars filled 
        with strange, twisted specimens. As you make your way further into the room, you notice movement out of the 
        corner of your eye. You turn to see a grotesque figure slowly emerging from the shadows. Its skin is mottled 
        and decaying, its eyes sunken and life less. It lurches towards you, emitting a low, guttural growl. 
        Your heart races as you realize that you are face to face with a zombie. You try to back away, but your foot 
        catches on a loose floorboard and you stumble backwards, falling to the ground.""", font_size=15, f_g="white")
        state5text.place(x=50, y=20, width=500, height=600)

        state5text2 = setup_text("""
             The zombie closes in on you, its fingers clawing at the air. You scramble backwards, desperately searching 
             for a way out. As you look around, you notice that the jars on the shelves are shaking and rattling, and 
             something inside them is moving. 
             With a sickening realization, you realize that the jars contain other undead creatures, waiting to be 
             unleashed upon the living. As the zombie draws nearer, you know that your only chance for survival is to 
             fight your way out of the room before the other creatures are released. 
             Your heart pounding, you scramble to your feet and race towards the door. The zombie is hot on your heels, 
             its breath rancid and putrid. You slam the door shut, but it is no match for the zombie's strength. 
             The creature slams into the door, sending splinters flying.
             You turn to run, but you realize that you are trapped. The zombie has blocked your only exit. 
             As the creature reaches out to grab you, you close your eyes and brace for impact, praying that someone, 
             anyone, will come to your rescue.""", font_size=13, f_g="white")
        state5text2.place(x=450, y=0, width=400, height=600)

        state5knapp = setup_button('Fight the zombie', self.fzombie, font_size=20)
        state5knapp.place(x=850, y=250, width=300, height=52)

    def state6(self):
        """

        :return:
        """
        destroy()
        state6text = setup_text("""You open the door on the left hand side of you, and step into a dimly lit room.
            The air is heavy with the stench of rot and decay, and the walls are lined with shelves containing jars 
            filled with strange, twisted specimens. As you make your way further into the room, you notice movement 
            out of the corner of your eye. You turn to see a grotesque figure slowly emerging from the shadows. 
            Its skin is mottled and decaying, its eyes sunken and lifeless. It lurches towards you, emitting a low, 
            guttural growl. Your heart is racing as you realize that you are face to face with a zombie. You try to 
            back away, but your foot catches on a loose floorboard and you stumble backwards, falling to the ground. 
            The zombie closes in on you, its fingers clawing at the air. You scramble backwards, desperately searching 
            for a way out. As you look around, you notice that the jars on the shelves are shaking and rattling, and 
            something inside them is moving. With a sickening realization, you realize that the jars contain other 
            undead creatures, waiting to be unleashed upon the living. As the zombie draws nearer, you know that your 
            only chance for survival is to fight your way out of the room.""", font_size=10, f_g="white")
        state6text.place(x=50, y=20, width=500, height=600)

        state6knapp = setup_button('Fight the zombie', self.fzombie, font_size=20)
        state6knapp.place(x=850, y=350, width=300, height=52)

        state6knapp2 = setup_button('Run...', self.zdead, font_size=20)
        state6knapp2.place(x=850, y=250, width=300, height=52)

    def fzombie(self):
        """

        :return:
        """
        fzombieval = random.randint(1, 2)
        if fzombieval == 1:
            self.zstate2()
        else:
            self.zdead()

    def zstate2(self):
        """

        :return:
        """
        destroy()
        zstate2text = setup_text("""
            You successfully killed the zombie, you see a staircase, you go up the stairs and you see a door, you open
            the door and you see a room with a table and a chair, you sit down and you see a piece of paper on the
            table, you pick it up and it says "You are in a room, you have to find a way out, you can go up the stairs
            or you can go down the stairs, choose wisely"
            """, font_size=20, f_g="white")
        zstate2text.place(x=-250, y=20, width=1000, height=600)

        zstate2knapp = setup_button('Go up the stairs', self.state7, font_size=20)
        zstate2knapp.place(x=500, y=150, width=300, height=52)

        zstate2knapp1 = setup_button('Go down the stairs', self.state8, font_size=20)
        zstate2knapp1.place(x=500, y=250, width=300, height=52)

    def state7(self):
        """

        :return:
        """
        destroy()
        state7text = setup_text("""
            You chose to go up the stairs, you are going up and going up, until you reach the top, you see a door, 
            you open the door and you hear something strange from behind, what do you do?""", font_size=20,
                                f_g="white")
        state7text.place(x=-250, y=20, width=1000, height=600)

        state7knapp = setup_button('Go back down the stairs', self.state8, font_size=20)
        state7knapp.place(x=500, y=150, width=300, height=52)

        state7knapp1 = setup_button('Stay, and wait', self.win, font_size=20)
        state7knapp1.place(x=500, y=250, width=300, height=52)

    def state8(self):
        """

        :return:
        """
        destroy()

        # Open temp.txt and read the first line
        with open("temp.txt", "r", encoding="utf-8") as file:
            name = file.readline()

        state8text = setup_text(f"""
            You chose to go down the stairs, you are going down and going down, until you reach the bottom, you see a 
            door, you open the door, you see a room with a table and a chair, you sit down and you hear someone calling 
            your name, "{name}! what are you doing here?", you look up an
            d you see your best friend, you get up and you 
            hug him, you say "I'm so glad you're here, I was so scared, I thought I was going to die", you both start 
            crying, you say "This place is so scary, I don't know how I'm going to get out of here", your friend says 
            "Don't worry, I'll help you get out of here", you say "Thank you so much, I don't know what I would do 
            without you", you both start crying again, you say "I'm so glad you're here, I was so scared, I thought 
            I was going to die", you both start crying.""", font_size=15, f_g="white")
        state8text.place(x=-250, y=20, width=1000, height=600)

        state8knapp = setup_button('Listen to your friend', self.state6, font_size=20)
        state8knapp.place(x=500, y=150, width=300, height=52)

        state8knapp1 = setup_button('Ignore your friend', self.zdead, font_size=20)
        state8knapp1.place(x=500, y=250, width=300, height=52)


    def win(self):
        statewin = setup_text("""You hear the rotor blades of a helicopter approaching, you look out the window and
        you see a helicopter, you run to the door and you open it, the helicopter lands and you get in, you say
        "Thank you so much for saving me, I don't know what I would do without you", the pilot says "Don't worry,
        I'm here to save you", you say "Thank you so much!""", font_size=15, f_g="white")
        statewin.place(x=-180, y=20, width=700, height=600)

        statewin1 = setup_button('Play again', self.state3, font_size=20)
        statewin1.place(x=500, y=150, width=300, height=52)

        statewin2 = setup_button('Quit', sys.exit, font_size=20)
        statewin2.place(x=500, y=250, width=300, height=52)


if __name__ == "__main__":
    root = tk.Tk()
    states = States(root)
    app = Setup(root, states)
    root.mainloop()

# Delete the temp.txt file
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
