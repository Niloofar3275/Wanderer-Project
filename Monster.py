
from random import *

board_size = 10



walls = [[3,0],[3,1],[3,2],[2,2],[2,2],[1,2],[5,1],[5,2],[5,3],[5,4],
		[6,4],[7,4],[8,4],[7,1],[8,1],[7,2],[8,2],[0,4],[1,4],[2,4],[3,4],[1,5],[1,6],[3,5],[3,6],
		[5,6],[6,7],[6,6],[5,7],[8,6],[8,7],[8,8],[1,8],[2,8],[3,8],[3,9],[5,9],[6,9]]



class Monster():

	def __init__(self,monster_number, monster_x, monster_y, level):


		self.monster_number = monster_number
		self.monster_x = monster_x
		self.monster_y = monster_y
		self.monster_type = "skeleton"
		self.key_bearer = False
		self.alive = True




		# sets monster level
		self.level = level
		level_chance = randint(1,10)
		
		if 5 < level_chance:

			self.level = self.level + 1

		elif level_chance == 5:

			self.level = self.level + 2




		#first monster that is spawned is boss and second one has the key
		if self.monster_number == 0:

			self.monster_type = "boss"
			#key_bearer = False

		elif self.monster_number == 1:
			key_bearer = True



		# sets starting stats if monster is a boss
		if self.monster_type == "boss":

			self.HP = 2 * self.level * randint(1, 6) + randint(1, 6)
			self.DP = self.level/2 * randint(1, 6) + randint(1, 6) / 2
			self.SP = self.level * randint(1, 6) + self.level

		# sets starting stats if monster is an skeleton
		else:
			self.HP = 2 * self.level * randint(1, 6)
			self.DP = self.level/2 * randint(1, 6)
			self.SP = self.level * randint(1, 6)

		#print(f"{self.HP} {self.DP} {self.SP}")




	def dead(self):

		# kills the monster by puting it out of the map

		self.monster_x = 100
		self.monster_y = 100
		self.alive = False







	#moving a single monster
	def move(self):

		if self.alive:


			moved = False
			directions = [0,1,2,3]

			while not moved:
				# random number that selects monster direction
				# 0 = up, 1 = down, 2 = right, 3 = left
				
				direction = choice(directions)
				#print(direction)
				#going up
				if direction == 0:
					self.monster_y = self.monster_y - 1

					#checks so monster is not moved into a wall/other monsters or is out of map
					if [self.monster_x, self.monster_y] in walls or [self.monster_x, self.monster_y] in monsters.positions or self.monster_y == -1:
						self.monster_y = self.monster_y +1
						directions.remove(0)


					else:
						moved = True

				#going down
				elif direction == 1:
					self.monster_y = self.monster_y + 1

					#checks so monster is not moved into a wall/other monster or is out of map
					if [self.monster_x, self.monster_y] in walls or [self.monster_x, self.monster_y] in monsters.positions or self.monster_y == 10:
						self.monster_y = self.monster_y - 1
						directions.remove(1)


					else:
						moved = True

				#going right
				elif direction == 2:
					self.monster_x = self.monster_x + 1

					#checks so monster is not moved into a wall/other monster or is out of map
					if [self.monster_x, self.monster_y] in walls or [self.monster_x, self.monster_y] in monsters.positions or self.monster_x == 10:
						self.monster_x = self.monster_x - 1
						directions.remove(2)


					else:
						moved = True

				#going left
				elif direction == 3:

					self.monster_x = self.monster_x - 1

					#checks so monster is not moved into a wall/other monster or is out of map
					if [self.monster_x, self.monster_y] in walls or [self.monster_x, self.monster_y] in monsters.positions or self.monster_x == -1:
						self.monster_x = self.monster_x + 1
						directions.remove(3)


					else:
						moved = True


				#monster can't be moved
				if len(directions) == 0:

					moved = True


	
		
		monsters.positions[self.monster_number] = [self.monster_x, self.monster_y]

	def draw(self, canvas, resource, image_size):

		canvas.create_image(self.monster_x * image_size + (image_size/2), self.monster_y * image_size + (image_size/2), image = resource.get_image(self.monster_type))

	

class Monsters():

	def __init__(self,level):

		num_of_monsters = randint(3,6)
		#print(num_of_monsters)
		self.monsters = []
		self.positions= []
		self.level = level

		while len(self.positions) < num_of_monsters:
			
			#we start from 3 so monster is not spawned very close to player
			position = [randint(3,board_size-1),randint(3,board_size-1)]


			#checks so monster is not spawned in a wall/monster
			if position not in walls and position not in self.positions:
				self.positions.append(position)


		for i in range(len(self.positions)):
			monster = Monster(i,self.positions[i][0],self.positions[i][1], self.level)
			self.monsters.append(monster)




	def moving(self):
			for i in range(len(self.monsters)):
				self.monsters[i].move()

	def next_level(self, restart = False):


		self.level = self.level + 1
		#for i in range(len(self.monsters)):
		#	self.monsters[i].dead()
		if restart:
			self.level = 1
		self.__init__(self.level)







monsters = Monsters(1)
#print(monsters.positions)
#monsters.moving()
#print(monsters.monsters[1])
#monsters.moving()











