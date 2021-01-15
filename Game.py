from tkinter import *
from Resource import Resource
from Block import Block
from Grid import Grid
from Player import Player
from Battle import * 



image_size = 72
board_size = 10




root = Tk()
canvas = Canvas(root, width=image_size * board_size, height=image_size * board_size)
resource = Resource()

player = Player(0,0,canvas, resource)





# Tell the canvas that we prepared a function that can deal with the key press events

canvas.bind("<KeyPress>", player.movement)


canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()


root.mainloop()
