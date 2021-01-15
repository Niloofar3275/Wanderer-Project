



class Block:

	def __init__(self, row, column, block_type):

		self.row = row
		self.column = column
		self.block_type = block_type

	def draw(self, canvas, resource, image_size):
		canvas.create_image(self.row * image_size + (image_size/2), self.column * image_size + (image_size/2), image = resource.get_image(self.block_type))