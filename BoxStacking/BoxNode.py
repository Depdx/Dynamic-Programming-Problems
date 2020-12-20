import Node


class BoxNode(Node):
	"""
	:param box : 3D tuple with dimensions, exemple (1,2,3) is a box of witdh 1, lenght 2 and height 3
	"""

	def __init__(self, box: tuple = (0, 0, 0), **kwargs):
		self.box = box
		super().__init__(**kwargs)
