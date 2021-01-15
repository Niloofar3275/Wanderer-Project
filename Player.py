from random import *
from Grid import Grid
from Resource import Resource
import time


# position of walls
walls = [[3,0],[3,1],[3,2],[2,2],[2,2],[1,2],[5,1],[5,2],[5,3],[5,4],
		[6,4],[7,4],[8,4],[7,1],[8,1],[7,2],[8,2],[0,4],[1,4],[2,4],[3,4],[1,5],[1,6],[3,5],[3,6],
		[5,6],[6,7],[6,6],[5,7],[8,6],[8,7],[8,8],[1,8],[2,8],[3,8],[3,9],[5,9],[6,9]]


image_size = 72
board_size = 10

class Player(object):

	def __init__(self,X,Y, canvas , resource):

		self.canvas = canvas
		self.resource = resource
		self.attack = False

		self.fighting = False

		self.X = X
		self.Y = Y
		self.direction = "main_charactor"
		self.turn = 0

		self.HP = 20 + 3 * randint(1, 6)
		self.max_HP = self.HP
		self.DP = 2 * randint(1, 6)
		self.SP = 5 + randint(1, 6)



		if self.turn == 0:

			grid = Grid(board_size, self)
			grid.draw(self.canvas, self.resource, image_size)
			self.show_stat()



	def show_stat(self):

		
		self.canvas.create_text(image_size*(board_size - 1.9), image_size*(board_size -1/2), font=("Helvetica", 19), text= f"HP:{round(self.HP, 1)} SP:{self.SP} DP:{self.DP}")

		if self.fighting:
			self.canvas.create_text(image_size * 3, image_size*(board_size -1/2), font=("Helvetica", 19),\
			 text= f"{self.monster_stat.monster_type.title()} level {self.monster_stat.level} HP:{self.monster_stat.HP} SP:{self.monster_stat.SP} DP:{self.monster_stat.DP}", fill = "red")


	def get_monster_stat(self, monster):

		self.monster_stat = monster



	#levels up hero when killing a monster
	def level_up(self):

		self.max_HP = self.max_HP + randint(1, 6)
		self.DP = self.DP + randint(1, 6)
		self.SP = self.SP + randint(1, 6)




	def movement(self, e):

		# hero doesn't move when in fighing mode
		if not self.fighting:
		    # moving up
		    if e.keycode == 38:

		    	#moves the player

		        self.Y = self.Y - 1
		        self.direction = "main_charactor_up"

		        # assigns new number of turn
		        self.turn = self.turn + 1


		        # Checks if player is in the map and is not colliding a wall.
		        if self.Y == -1 or [self.X,self.Y] in walls:
		        	self.Y =self.Y + 1
		       

		    # moving down
		    elif e.keycode == 40:

		        self.Y = self.Y + 1
		        self.direction = "main_charactor"

		        # assigns new number of turn
		        self.turn = self.turn + 1

		        
		        if self.Y == 10 or [self.X,self.Y] in walls:
		        	self.Y =self.Y - 1


		    # moving left
		    elif e.keycode == 37:

		    	#moves the player
		    	self.X = self.X- 1
		    	self.direction = "main_charactor_left"

		    	# assigns new number of turn
		    	self.turn = self.turn + 1

		    	# Checks if player is in the map and is not colliding a wall.
		    	if self.X == -1 or [self.X,self.Y] in walls:
		        	self.X =self.X + 1


		    # moving right
		    elif e.keycode == 39:

		    	self.X = self.X + 1
		    	self.direction = "main_charactor_right"

		    	# assigns new number of turn
		    	self.turn = self.turn + 1



		    	if self.X == 10 or [self.X,self.Y] in walls:

		        	self.X =self.X - 1

		# not going in attack mode while not fighting
		else:

	   		 #attacking
			if e.keycode == 32:
			
			
				self.attack = True




		# condition is satisfied every 2 turns so monsters move  	
		if self.turn % 2 == 0:

			monsters_move = True



		else:

			monsters_move = False

	    

		grid = Grid(board_size, self, self.direction)

		

		if monsters_move and not self.fighting:

			grid = Grid(board_size, self, self.direction, monsters_move)
			grid.draw(self.canvas, self.resource, image_size)
			self.show_stat()



		else:
			grid.draw(self.canvas, self.resource, image_size)
			self.show_stat()




		

	def dead(self):



		self.__init__(0, 0, self.canvas, self.resource)
		print("you lost restarting the game")

		

	def next_level(self):


		self.X = 0
		self.Y = 0
		self.direction = "main_charactor"
		self.turn = 0

		chance = randint(1,10)

		# 50% chance to restore 10% of HP
		if chance < 6:
			self.HP = self.HP + (self.max_HP/10)

		# 10% chance to restore all HP
		elif chance == 6:
			self.HP = self.max_HP
		# 40% chance to restore third of HP
		else:
			self.HP = self.HP + (self.max_HP/3)



		grid = Grid(board_size, self)
		grid.draw(self.canvas, self.resource, image_size)
		print("going to next level")






		

	def draw(self, canvas, resource, image_size):
		
		canvas.create_image(self.X * image_size + (image_size/2), self.Y * image_size + (image_size/2), image = resource.get_image(self.direction))







