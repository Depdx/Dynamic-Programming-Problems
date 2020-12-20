import unittest
import Node
import Graph
import BoxNode


class TestBoxStacking(unittest.TestCase):
	def setUp(self):
		self.boxes = [(4, 5, 3), (2, 3, 2), (3, 6, 2), (1, 5, 4), (2, 4, 1), (1, 2, 2)]
		self.correct_stack = [(4, 5, 3), (2, 3, 2), (1, 2, 2)]
		self.correct_height = 7
	def test_Node(self):
		try:
			a = Node(name="A")
			b = Node(name="B")
			a.add_node(node=b)
			self.assertListEqual(a.connected_node, [b])
		except:
			self.fail()


	def test_BoxNode(self):
		try:
			a = BoxNode(name="A", box=self.boxes[0])
			b = BoxNode(name="B", box=self.boxes[1])
			a.add_node(node=b)
			self.assertListEqual(a.connected_node, [b])
		except:
			self.fail()

	def test_Graph(self):
		try:
			g = Graph(name="G")
		except:
			self.fail()


if __name__ == "__main__":
	unittest.main()
