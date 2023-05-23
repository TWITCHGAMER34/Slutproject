"""
This is the main file of the game
"""

# imports:
import os
import random
import sys
import tkinter as tk
import tkinter.font as tk_font
import json
import requests


def jokes(_f):  # get jokes from the api
    """
    This function is used to get the jokes from the api
    and return the data
    :param f:
    :return:
    """
    data = requests.get(_f, timeout=5)  # get the data from the api
    t_t = json.loads(data.text)  # load the data
    return t_t  # return the data


LINK = r"https://official-joke-api.appspot.com/random_joke"  # link to the api
joke = jokes(LINK)  # get the joke


def weather():  # get weather from the api
    """
    This function is used to get the weather from the api
    :return:
    """
    access_key = "49fd86502d789706569dd23f26182bed"  # access key to the api
    query = "Karlstad"  # query to the api
    link = f"http://api.weatherstack.com/current?access_key={access_key}&query={query}"
    # link to the api
    data = requests.get(link, timeout=5)  # get the data from the api
    t_t = json.loads(data.text)  # load the data
    return t_t  # return the data


weather = weather()  # get the weather


def window():
    """
    This method is used to set up the window for the game
    to work properly and to be able to run the game.
    :return:
    """
    root_el = tk.Tk()  # create the window
    root_el.title("The scary story")  # set the title of the window
    # setting window size
    width = 600  # set the width of the window
    height = 243  # set the height of the window
    screenwidth = root_el.winfo_screenwidth()  # get the width of the screen
    screenheight = root_el.winfo_screenheight()  # get the height of the screen
    align_str = f'{width}x{height}+{int((screenwidth - width) / 2)}' \
                f'+{int((screenheight - height) / 2)}'  # set the position of the window

    root_el.configure(bg="#000000")  # set the background color of the window
    root_el.geometry(align_str)  # set the size of the window
    root_el.resizable(width=False, height=False)  # set the window to be resizable or not


def setup_button(input_el, callback, font_size):  # set up the buttons
    """
    This method is used to set up the buttons for the game to work properly.
    :param font_size:
    :param callback:
    :param input_el:
    :return:
    """
    button = tk.Button(root)  # create the button
    button["activebackground"] = "#474747"  # set the background color
    # of the button when it is clicked
    button["bg"] = "#000000"  # set the background color of the button
    font = tk_font.Font(family='Times', size=font_size)  # set the font of the button
    button["font"] = font  # set the font of the button
    button["fg"] = "#ffffff"  # set the color of the text of the button
    button["justify"] = "center"  # set the justification of the text of the button
    button["text"] = input_el  # set the text of the button
    button["command"] = callback  # set the command of the button

    return button  # return the button


def setup_entry():  # set up the entry
    """
    This method is used to set up the entry for the game to work properly.
    :return:
    """
    entry = tk.Entry(root)  # create the entry
    entry["borderwidth"] = "1px"  # set the border width of the entry
    font = tk_font.Font(family='Times', size=10)  # set the font of the entry
    entry["font"] = font  # set the font of the entry
    entry["fg"] = "#000000"  # set the color of the text of the entry
    entry["justify"] = "center"  # set the justification of the text of the entry

    return entry  # return the entry


def destroy():  # destroy all widgets
    """
    This method is used to destroy all the widgets in the window.
    :return:
    """
    for child in root.winfo_children():  # loop through all the widgets in the window
        child.destroy()  # destroy the widget


def setup_text(input_el, font_size, f_g):  # set up the text
    """
    This method is used to set up the text for the game to work properly.
    :param f_g:
    :param font_size:
    :param input_el:
    :return:
    """
    text = tk.Message(root)  # create the text
    text["anchor"] = "center"  # set the anchor of the text
    text["bg"] = "#000000"  # set the background color of the text
    font = tk_font.Font(family='Times', size=font_size)  # set the font of the text
    text["font"] = font  # set the font of the text
    text["fg"] = f_g  # set the color of the text of the text
    text["justify"] = "center"  # set the justification of the text of the text
    text["width"] = 300  # set the width of the text
    text["text"] = input_el  # set the text of the text
    return text  # return the text


def quit_program():  # quit the program
    """
    This method is used to quit the program.
    :return:
    """
    sys.exit()  # quit the program


class Setup:  # set up the game
    """
    This class is used to set up the game and the GUI for the
    game to work properly and to be able to run the game.
    """

    def __init__(self, root_el, states_el):  # initialize the class
        self.entry2 = None  # set the entry to none
        self.entry1 = None  # set the entry to none
        self.name = None  # set the name to none
        self.states = states_el  #set the states to the input
        # setting title
        root_el.title("The scary story")  # set the title of the window
        # setting window size
        width = 1200  # set the width of the window
        height = 600  # set the height of the window
        screenwidth = root_el.winfo_screenwidth()  # get the width of the screen
        screenheight = root_el.winfo_screenheight()  # get the height of the screen
        align_str = f'{width}x{height}+{int((screenwidth - width) / 2)}+' \
                    f'{int((screenheight - height) / 2)}'
        root_el.configure(bg="#000000")  # set the background color of the window
        root_el.geometry(align_str)  # set the size of the window
        root_el.resizable(width=False, height=False)  # set the window to be resizable or not

        title = tk.Message(root_el)  # create the title
        title["anchor"] = "center"  # set the anchor of the title
        title["bg"] = "#000000"  # set the background color of the title
        font = tk_font.Font(family='Times', size=50, weight="bold", slant="italic",
                            underline=True)  # set the font of the title
        title["font"] = font  # set the font of the title
        title["fg"] = "#ffffff"  # set the color of the text of the title
        title["justify"] = "center"  # set the justification of the text of the title
        title["width"] = 1000  # set the width of the title
        title["text"] = "The scary story"  # set the text of the title
        title.place(x=110, y=100, width=1000, height=90)  # set the position of the title

        start = tk.Button(root_el)  # create the start button
        start["activebackground"] = "#474747"  # set the background color of
        # the start button when it is clicked
        start["bg"] = "green"  # set the background color of the start button
        font = tk_font.Font(family='Times', size=15)  # set the font of the start button
        start["font"] = font  # set the font of the start button
        start["fg"] = "#ffffff"  # set the color of the text of the start button
        start["justify"] = "center"  # set the justification of the text of the start button
        start["text"] = "Click here to play!"  # set the text of the start button
        start.place(x=500, y=200, width=200, height=100)  # set the position of the start button
        start["command"] = self.start  # set the command of the start button

        quit_el = tk.Button(root_el)  # create the quit button
        quit_el["activebackground"] = "#000000"  # set the background
        # color of the quit button when it is clicked
        quit_el["activeforeground"] = "#ffffff"  # set the color of the
        # text of the quit button when it is clicked
        quit_el["bg"] = "#ff0000"  # set the background color of the quit button
        font = tk_font.Font(family='Times', size=10)  # set the font of the quit button
        quit_el["font"] = font  # set the font of the quit button
        quit_el["fg"] = "#ffffff"  # set the color of the text of the quit button
        quit_el["justify"] = "center"  # set the justification of the text of the quit button
        quit_el["text"] = "Quit!"  # set the text of the quit button
        quit_el.place(x=0, y=550, width=150, height=50)  # set the position of the quit button
        quit_el["command"] = quit_program  # set the command of the quit button

        joke_print = setup_text(f'Joke of the day: \n {joke["setup"]} '
                                f'\n{joke["punchline"]}', font_size=15,
                                f_g="white")  # set the joke of the day
        joke_print.place(x=0, y=400, width=1200, height=150)  # set the position
        # of the joke of the da
        weather_print = setup_text(f'Weather: \n {weather["current"]["weather_descriptions"][0]}'
                                   f'\n {weather["current"]["temperature"]} degrees', font_size=15,
                                   f_g="white")  # set the weather
        weather_print.place(x=0, y=300, width=1200, height=100)  # set the position

    def start(self):
        """
        This method is used to start the game.
        :return:
        """
        self.main()  # run the main method

    def main(self):
        """
        This method is used to set up the main GUI.
        :return:
        """
        destroy()  # destroy all widgets
        alder = setup_text('Whats your name?', font_size=20, f_g="white")  # set the text of the age
        alder.place(x=140, y=50, width=357, height=120)  # set the position of the text of the age

        namn = setup_text('How old are you?', font_size=20, f_g="white")  # set the text of the name
        namn.place(x=650, y=50, width=357, height=120)  # set the position of the text of the name

        self.entry1 = setup_entry()  # set the entry of the age
        self.entry1.place(x=780, y=140, width=118, height=52)  # set the
        # position of the entry of the age

        self.entry2 = setup_entry()  # set the entry of the name
        self.entry2.place(x=240, y=140, width=118, height=52)  # set the position
        # of the entry of the name

        knapp1 = setup_button('next', self.confirm_main, font_size=20)  # set the next button
        knapp1.place(x=500, y=350, width=118, height=52, )  # set the position of the next button

    def confirm_main(self):  # set the confirm main method
        """
        This method is used to confirm the main GUI.
        :return:
        """
        alder = self.entry1.get()  # get the age
        namn = self.entry2.get()  # get the name
        destroy()  # destroy all widgets

        state2text = setup_text(f'Hello {namn}, you are {alder} years old, correct?', font_size=30,
                                f_g="white")  # set the text of the confirm main
        state2text.place(x=400, y=20, width=357, height=300)  # set the
        # position of the text of the confirm main

        state2knapp = setup_button('Yes', self.states.state3, font_size=20)  # set the yes button
        state2knapp.place(x=450, y=350, width=118, height=52)  # set the position of the yes button

        state2knapp1 = setup_button('No', self.main, font_size=20)  # set the no button
        state2knapp1.place(x=600, y=350, width=118, height=52)  # set the position of the no button
        with open('temp.txt', 'w', encoding="utf-8") as file:  # open the temp file
            file.write(namn)  # write the name in the temp file


class States(Setup):  # create the states class
    """
    Detta är en klass som ärver från Setup klassen och
    innehåller alla states som finns i spelet. Denna klassen är
    kopplad till Setup klassen och använder sig av dess metoder.
    """

    def __init__(self, root_el):  # set the init method
        """
        This method is used to set up the states.
        :param root_el:
        """
        super().__init__(root_el, self)  # set the super method

    def zdead(self):  # set the zdead method, this method is used when the player dies in the game.
        """
        This method is used to set up the GUI when the player dies.
        :return:
        """
        destroy()  # destroy all widgets
        print("You died")  # print that the player died
        ztext = setup_text('You died', font_size=40, f_g="red")  # set the text of the death
        ztext.place(x=400, y=50, width=357, height=120)  # set the position of the text of the death

        z_knapp = setup_button('next', self.main, font_size=20)  # set the next button
        z_knapp.place(x=520, y=350, width=118, height=52, )  # set the position of the next button

    def state3(self):  # set the state3 method, this
        # method is used when the player is in the first room.
        """
        This method is used to set up the GUI when the player is in the first room.
        :return:
        """
        destroy()  # destroy all widgets
        state3text = setup_text(
            'You wake up in a dark room, you dont know where you are or '
            'how you got here, you see a door in front of '
            'you, to your right and to your left, choose a door.',
            font_size=33, f_g="white")  # set the text of the first room
        state3text.place(x=-250, y=10, width=1100, height=600)  # set the position
        # of the text of the first room

        state3knapp = setup_button('Open the door infront of you', self.state4,
                                   font_size=15)  # set the door infront of you button
        state3knapp.place(x=500, y=200, width=300, height=50)  # set the position of
        # the door infront of you button

        state3knapp1 = setup_button('Open the door to your right', self.state5,
                                    font_size=15)  # set the door to your right button
        state3knapp1.place(x=500, y=300, width=300, height=50)  # set the position
        # of the door to your right button

        state3knapp2 = setup_button('Open the door to your left', self.state6,
                                    font_size=15)  # set the door to your left button
        state3knapp2.place(x=500, y=100, width=300, height=50)  # set the
        # position of the door to your left button

    def state4(self):  # set the state4 method, this method
        # is used when the player is in the second room.
        """
        This method is used to set up the GUI when the player is in the second room.
        :return:
        """
        destroy()  # destroy all widgets
        state4text = setup_text(
            'You open the door in-front of you, you see a staircase, '
            'you go up the stairs and you see a door, you open '
            'the door and you see a room with a table and a chair, '
            'you sit down and you see a piece of paper on the '
            'table, you pick it up and it says "You are in a room, '
            'you have to find a way out, you can go up the stairs'
            'or you can go down the stairs, choose wisely"',
            font_size=20, f_g="white")  # set the text of the second room
        state4text.place(x=-250, y=20, width=1000, height=600)  # set the
        # position of the text of the second room

        state4knapp = setup_button('Go up the stairs', self.state7, font_size=20)  # set the go
        # up the stairs button
        state4knapp.place(x=500, y=150, width=300, height=52)  # set the position
        # of the go up the stairs button

        state4knapp1 = setup_button('Go down the stairs', self.state8,
                                    font_size=20)  # set the go down the stairs button
        state4knapp1.place(x=500, y=250, width=300, height=52)  # set the position
        # of the go down the stairs button

    def state5(self):  # set the state5 method,
        # this method is used when the player is in the third room.
        """
        This method is used to set up the GUI when the player is in the third room.
        :return:
        """
        destroy()  # destroy all widgets
        state5text = setup_text("""You open the door on the right hand side of you,
        and step into a dimly lit room. The air is heavy with the stench of rot and decay,
        and the walls are lined with shelves containing jars filled with strange, twisted specimens.
        As you make your way further into the room, you notice movement out of the
        corner of your eye. You turn to see a grotesque figure slowly emerging from the shadows. Its skin is mottled
        and decaying, its eyes sunken and life less. It lurches towards you, emitting a low, guttural growl.
        Your heart races as you realize that you are face to face with a zombie. You try to back away, but your foot
        catches on a loose floorboard and you stumble backwards, falling to the ground.""",
                                font_size=15, f_g="white")
        state5text.place(x=50, y=20, width=500, height=600)  # set the text of the third room

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
             anyone, will come to your rescue.""", font_size=13, f_g="white")  # set
        # the text of the third room
        state5text2.place(x=450, y=0, width=400, height=600)
        # set the position of the text of the third room
        state5knapp = setup_button('Fight the zombie', self.fzombie, font_size=20)  # set the
        # fight the zombie button
        state5knapp.place(x=850, y=250, width=300, height=52)  # set the position
        # of the fight the zombie button

    def state6(self):  # set the state6 method, this method
        # is used when the player is in the fourth room.
        """
        This method is used to set up the GUI when the player is in the fourth room.
        :return:
        """
        destroy()  # destroy all widgets
        state6text = setup_text("""You open the door on the left hand side of you,
            and step into a dimly lit room.
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
            only chance for survival is to fight your way out of the room.""",
                                font_size=10, f_g="white")
        state6text.place(x=50, y=20, width=500, height=600)  # set the text of the fourth room

        state6knapp = setup_button('Fight the zombie', self.fzombie, font_size=20)
        # set the fight the zombie button
        state6knapp.place(x=850, y=350, width=300, height=52)  # set the position of the
        # fight the zombie button

        state6knapp2 = setup_button('Run...', self.zdead, font_size=20)  # set the run button
        state6knapp2.place(x=850, y=250, width=300, height=52)  # set the position of the run button

    def fzombie(self):  # set the fzombie method, this method is
        # used when the player is fighting the zombie.
        """
        This method is used to set up the GUI when the player is fighting the zombie.
        :return:
        """
        fzombieval = random.randint(1, 2)  # set the fzombieval variable
        # to a random number between 1 and 2
        if fzombieval == 1:  # if the fzombieval variable is equal
            # to 1, then the player wins the fight
            self.zstate2()  # call the zstate2 method
        else:  # if the fzombieval variable is not equal to 1, then the player loses the fight
            self.zdead()  # call the zdead method

    def zstate2(self):  # set the zstate2 method, this method is used when
        # the player wins the fight against the zombie.
        """
        This method is used to set up the GUI when the player wins the fight against the zombie.
        :return:
        """
        destroy()  # destroy all widgets
        zstate2text = setup_text("""
            You successfully killed the zombie, you see a staircase, you go up the stairs and you see a door, you open
            the door and you see a room with a table and a chair, you sit down and you see a piece of paper on the
            table, you pick it up and it says "You are in a room, you have to find a way out, you can go up the stairs
            or you can go down the stairs, choose wisely"
            """, font_size=20, f_g="white")  # set the text of the fifth room
        zstate2text.place(x=-250, y=20, width=1000, height=600)  # set the position
        # of the text of the fifth room

        zstate2knapp = setup_button('Go up the stairs', self.state7, font_size=20)  # set the
        # go up the stairs button
        zstate2knapp.place(x=500, y=150, width=300, height=52)  # set the position of
        # the go up the stairs button

        zstate2knapp1 = setup_button('Go down the stairs', self.state8,
                                     font_size=20)  # set the go down the stairs button
        zstate2knapp1.place(x=500, y=250, width=300, height=52)  # set the position of
        # the go down the stairs button

    def state7(self):  # set the state7 method, this method is
        # used when the player is in the fifth room.
        """
        This method is used to set up the GUI when the player is in the fifth room.
        :return:
        """
        destroy()  # destroy all widgets
        state7text = setup_text("""
            You chose to go up the stairs, you are going up and going up, until you reach the top, you see a door, 
            you open the door and you hear something strange from behind, what 
            do you do?""", font_size=20,
                                f_g="white")  # set the text of the sixth room
        state7text.place(x=-250, y=20, width=1000, height=600)  # set the position
        # of the text of the sixth room

        state7knapp = setup_button('Go back down the stairs', self.state8,
                                   font_size=20)  # set the go back down the stairs button
        state7knapp.place(x=500, y=150, width=300, height=52)  # set the position
        # of the go back down the stairs button

        state7knapp1 = setup_button('Stay, and wait', self.win, font_size=20)  # set the
        # stay and wait button
        state7knapp1.place(x=500, y=250, width=300, height=52)  # set the position
        # of the stay and wait button

    def state8(self):  # set the state8 method, this method is used when
        # the player is in the sixth room.
        """
        This method is used to set up the GUI when the player is in the sixth room.
        :return:
        """
        destroy()  # destroy all widgets

        # Open temp.txt and read the first line
        with open("temp.txt", "r", encoding="utf-8") as file:  # open the temp.txt file
            name = file.readline()  # read the first line of the temp.txt file

        state8text = setup_text(f"""
            You chose to go down the stairs, you are going down and going down, until you reach the bottom, you see a 
            door, you open the door, you see a room with a table and a chair, you sit down and you hear someone calling 
            your name, "{name}! what are you doing here?", you look up an
            d you see your best friend, you get up and you 
            hug him, you say "I'm so glad you're here, I was so scared, I thought I was going to die", you both start 
            crying, you say "This place is so scary, I don't know how I'm going to get out of here", your friend says 
            "Don't worry, I'll help you get out of here", you say "Thank you so much, I don't know what I would do 
            without you", you both start crying again, you say "I'm so glad you're here, I was so scared, I thought 
            I was going to die", you both start crying.""", font_size=12, f_g="white")
        state8text.place(x=-250, y=20, width=1000, height=600)  # set the position
        # of the text of the sixth room

        state8knapp = setup_button('Listen to your friend', self.state6, font_size=20)  # set
        # the listen
        # to your friend button
        state8knapp.place(x=500, y=150, width=300, height=52)  # set the position of the
        # listen to your friend button

        state8knapp1 = setup_button('Ignore your friend', self.zdead, font_size=20)  # set the
        # ignore your friend button
        state8knapp1.place(x=500, y=250, width=300, height=52)  # set the position of
        # the ignore your friend button

    def win(self):  # set the win method, this method is used when the player wins the game.
        """
        This method is used to set up the GUI when the player wins the game.
        :return:
        """
        statewin = setup_text("""You hear the rotor blades of a helicopter approaching,
        you look out the window and you see a helicopter, you run to the door and you 
        open it, the helicopter lands and you get in, you say "Thank you so much for
        saving me, I don't know what I would do without you", the pilot says "Don't worry,
        I'm here to save you", you say "Thank you so much!""", font_size=15, f_g="white")
        # set the text of the win screen
        statewin.place(x=-180, y=20, width=700, height=600)  # set the position of the text
        # of the win screen

        statewin1 = setup_button('Play again', self.state3, font_size=20)
        statewin1.place(x=500, y=150, width=300, height=52)  # set the position of the play
        # again button

        statewin2 = setup_button('Quit', sys.exit, font_size=20)  # set the quit button
        statewin2.place(x=500, y=250, width=300, height=52)  # set the position of the quit button


if __name__ == "__main__":  # set the main method
    root = tk.Tk()  # set the root
    states = States(root)  # set the states
    app = Setup(root, states)  # set the app
    root.mainloop()  # start the mainloop

# Delete the temp.txt file
if os.path.exists("temp.txt"):  # check if the temp.txt file exists
    os.remove("temp.txt")  # delete the temp.txt file
