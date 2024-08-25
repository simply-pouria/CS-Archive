import tkinter as tk
from GameMap import game_map_window


def initialize(color):
    label.config(text=f"Color chosen: {color}")
    root.destroy()
    game_map_window(color)

# create the window
root = tk.Tk()
root.title("Welcome")
root.geometry("400x200")

# Create widgets
blue_button = tk.Button(root, text="Blue", command=lambda: initialize("blue"), padx=10, pady=5)
red_button = tk.Button(root, text="Red", command=lambda: initialize("red"), padx=10, pady=5)
label = tk.Label(root, text="Choose your color", padx=10, pady=10)

# Pack widgets
label.pack()
blue_button.pack()
red_button.pack()


root.mainloop()
