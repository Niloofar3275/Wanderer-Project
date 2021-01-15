
from Block import Block
from Monster import *
from Battle import *




class Grid:

	# sets monster initial position
	

	def __init__(self, size, player, player_direction = "main_charactor", monsters_move = False):

		

		self.pause = False

		self.grid = []
		
		#position of walls
		self.walls = [[3,0],[3,1],[3,2],[2,2],[2,2],[1,2],[5,1],[5,2],[5,3],[5,4],
		[6,4],[7,4],[8,4],[7,1],[8,1],[7,2],[8,2],[0,4],[1,4],[2,4],[3,4],[1,5],[1,6],[3,5],[3,6],
		[5,6],[6,7],[6,6],[5,7],[8,6],[8,7],[8,8],[1,8],[2,8],[3,8],[3,9],[5,9],[6,9]]

		


		# moves the monster every 2 turn
		if monsters_move:

			monsters.moving()
			#print(monsters.positions)
		
		#builds the map block by block


		for i in range(0, size):
				
			row = []
			for j in range(0, size):

				#checks if player is in the block
				if player.X== i and player.Y== j:

					if [i,j] in monsters.positions:


						#self.pause = True
						battle(player, monsters.monsters[monsters.positions.index([i,j])], monsters, monsters_move)


								
					occupied_player = True

				#checks if monster is in the block
				elif [i,j] in monsters.positions:

					occupied_monster = True

					#finds which monster is in the block
					monster = monsters.positions.index([i,j])

				else:
					occupied_player = False
					occupied_monster = False


						

				#checks if the block is a Wall
				if [i,j] in self.walls:

					block_type = "Wall"

				else:

					block_type = "Floor"

				if occupied_player:

					row.append(player)

				elif occupied_monster:

					row.append(monsters.monsters[monster])
						

				else:

					block = Block(i, j, block_type)
					row.append(block)




			if not self.pause:
				self.grid.append(row)
				



	def draw(self, canvas, resource, image_size):
		if not self.pause:
			for i in range(0, len(self.grid)):

				for j in range(0, len(self.grid)):

					# calls draw funtion of the object
					self.grid[i][j].draw(canvas, resource, image_size)


