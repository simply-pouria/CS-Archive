import tkinter as tk
from tkinter import messagebox
from random import randint

from youtube_dl.extractor import canvas


#  a class to make handling the players more convenient
class Player:
    initial_coordination = {'red': 2, 'blue': 22}

    def __init__(self, color: str, cv: tk.Canvas):
        self.traveled = 0
        self.coordination = Player.initial_coordination[color]
        self.color = color
        self.canvas = cv
        # putting the player on its initial position
        self.r = 15
        center = white_circles_positions_dict[Player.initial_coordination[color]]
        self.circle = cv.create_oval(center[0] - self.r, center[1] - self.r, center[0] + self.r, center[1] + self.r,
                                     fill=self.color)

    def move_forward(self, distance: int):
        print(distance, 'distance')
        self.traveled += distance
        self.coordination += distance
        try:
            if self.traveled <= 40:

                cr = white_circles_positions_dict[self.coordination]  # coordinate center
                new_coord = (cr[0] - 15, cr[1] - 15, cr[0] + 15, cr[1] + 15)  # x0 y0 x1 y1
                self.canvas.coords(self.circle, new_coord)

            else:

                if self.color == 'red':
                    cr = red_circle_positions_dict[self.coordination]  # coordinate center
                    new_coord = (cr[0] - 15, cr[1] - 15, cr[0] + 15, cr[1] + 15)  # x0 y0 x1 y1
                    self.canvas.coords(self.circle, new_coord)

                elif self.color == 'blue':
                    cr = blue_circle_positions_dict[self.coordination]  # coordinate center
                    new_coord = (cr[0] - 15, cr[1] - 15, cr[0] + 15, cr[1] + 15)  # x0 y0 x1 y1
                    self.canvas.coords(self.circle, new_coord)
        except KeyError:
            pass

    def move_backward(self, distance: int):
        self.traveled -= distance
        self.coordination -= distance

    def update_gui(self):
        pass


# a dictionary used to track the locations of position coordinates on canvas
positions = {}

# These dictionaries are used to label each circle with a specific color
white_circles_dicts = {}
red_circles_dicts = {}
blue_circles_dicts = {}

# coordinations
white_circle_coordinations = [(350, 180), (350, 210), (320, 210), (290, 210), (260, 210), (230, 210), (230, 240),
                              (230, 270), (230, 300), (230, 330), (200, 330), (170, 330), (170, 300),
                              (170, 270), (170, 240), (170, 210), (140, 210), (110, 210), (80, 210),
                              (50, 210), (50, 180), (50, 150), (80, 150), (110, 150), (140, 150),
                              (170, 150), (170, 120), (170, 90), (170, 60), (170, 30), (200, 30),
                              (230, 30), (230, 60), (230, 90), (230, 120), (230, 150), (260, 150),
                              (290, 150), (320, 150), (350, 150)]

red_circle_coordinations = [
    (320, 180), (290, 180), (260, 180), (230, 180)
]

blue_circle_coordinations = [
    (80, 180), (110, 180), (140, 180), (170, 180)
]

# creating dictionaries that correspond coordinations to each position

white_circles_positions_dict = {list(range(1, 41))[i]: white_circle_coordinations[i] for i in
                                range(len(list(range(1, 41))))}

red_circle_positions_dict = {list(range(41, 45))[i]: red_circle_coordinations[i] for i in
                             range(len(list(range(41, 45))))}

blue_circle_positions_dict = {list(range(41, 45))[i]: blue_circle_coordinations[i] for i in
                              range(len(list(range(41, 45))))}


# created as a function to ease switching windows
def game_map_window(color: str):
    root = tk.Tk()
    main_cv = tk.Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0,
                        bg="grey")
    dice = tk.Button(root, width=10, height=10, text="dice",
                     command=lambda: game_loop(player_1=player_1, player_2=player_2), fg="green", bg="gray")
    dice_result = tk.Label(root, text="Dice")
    main_cv.grid(row=0, column=0)
    dice.grid(row=0, column=1, sticky=tk.SE)
    dice_result.grid(row=0, column=1, sticky=tk.NE)

    # initializing game logic
    player_1 = Player(color, cv=main_cv)

    if color == "blue":
        player_2 = Player("blue", cv=main_cv)
    if color == "red":
        player_2 = Player("red", cv=main_cv)

    # a class to ease working with circle positions in the game map
    class PositionCircle:
        def __init__(self, x: float, y: float, r: float, color: str):
            self.x = x
            self.y = y
            self.r = r
            self.color = color
            self.circle = None
            self.draw_circle()

        def draw_circle(self):
            center = [self.x, self.y]
            self.circle = main_cv.create_oval(center[0] - self.r, center[1] - self.r, center[0] + self.r,
                                              center[1] + self.r,
                                              fill=self.color)

        def change_color(self, new_color):
            pass

    # creating the game map
    for position in white_circle_coordinations:
        x = position[0]
        y = position[1]
        r = 10
        color = 'white'
        circle_position = PositionCircle(x=x, y=y, r=r, color=color)
        white_circles_dicts[white_circle_coordinations.index(position) + 1] = circle_position

    for position in red_circle_coordinations:
        x = position[0]
        y = position[1]
        r = 10
        color = 'red'
        circle_position = PositionCircle(x=x, y=y, r=r, color=color)
        red_circles_dicts[red_circle_coordinations.index(position) + 1] = circle_position

    for position in blue_circle_coordinations:
        x = position[0]
        y = position[1]
        r = 10
        color = 'blue'
        circle_position = PositionCircle(x=x, y=y, r=r, color=color)
        blue_circles_dicts[blue_circle_coordinations.index(position) + 1] = circle_position

    def game_loop(player_1: Player, player_2: Player):

        print('p1', player_1.coordination)
        print('p2', player_2.coordination)

        # runs the turn of the player while also checking if they have won
        if turn(player_1):
            root.destroy()
            messagebox.showinfo(f"Player {player_1.color} wins!", f"Player {player_1.color} wins")
            return player_1

        if player_1.coordination == player_2.coordination:
            # player 1 kills player 2
            messagebox.showinfo("someone dies!", f"Player {player_1.color} just killed {player_2.color}")
            player_2.move_backward(player_2.traveled)

        # runs the turn of the player while also checking if they have won
        if turn(player_2):
            root.destroy()
            messagebox.showinfo(f"Player {player_2.color} wins!", f"Player {player_2.color} wins")
            return player_2

        if player_1.coordination == player_2.coordination:
            # player 2 kills player 1
            messagebox.showinfo("someone dies!", f"Player {player_2.color} just killed {player_1.color}")
            player_1.move_backward(player_1.traveled)

    def turn(player: Player):

        dice = randint(1, 6)
        dice_result.config(text=f"player {player.color}'s Dice: {dice}")

        if player.traveled + dice > 44:
            pass
            # should not move because the dice is more than the maximum places on the board

        elif player.traveled + dice == 44:
            return player

        else:
            player.move_forward(distance=dice)

        # rolls the dice again automatically if the player's previous dice was 6
        if dice == 6:
            turn(player)

    root.title("Mensch ärgere Dich nicht")
    root.mainloop()
