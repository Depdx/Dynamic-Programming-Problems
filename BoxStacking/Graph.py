class Graph:
	"""
	Graph with nodes
	:param name
	"""
	def __init__(self,name):
		self.__name= name
		self.nodes=[]

	@property
	def name(self):
		return self.__name