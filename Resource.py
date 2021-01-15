from tkinter import * 

# this class loads the images that we need
class Resource:

	def __init__(self):
		self.images = {}
		self.images["Floor"] = self.load_image("./images/Floor.gif")
		self.images["Wall"] = self.load_image("./images/Wall.gif")
		self.images["main_charactor"] = self.load_image("./images/main_charactor.gif")
		self.images["main_charactor_right"] = self.load_image("./images/main_charactor_right.gif")
		self.images["main_charactor_left"] = self.load_image("./images/main_charactor_left.gif")
		self.images["main_charactor_up"] = self.load_image("./images/main_charactor_up.gif")
		self.images["boss"] = self.load_image("./images/boss.gif")
		self.images["skeleton"] = self.load_image("./images/skeleton.gif")



	def load_image(self, path):

		img = PhotoImage(file=path)
		return img

	def get_image(self, key):
		return self.images[key]

