class HuffmanFactory:
	raw_string = ""
	huffman_tree = None
	compression_dictionary = {}
	compressed_string = ""


	class HuffmanNode:
		right = None
		left = None
		value = 0
		letter = ""
		
		def __init__(self, value, letter = "", left = None, right = None):
			self.value = value
			self.letter = letter
			self.left = left
			self.right = right
		
		def is_leaf(self):
			return (self.left == None and self.right == None)
		
		def __gt__(self, other):
			return self.value > other.value
		
		def __ge__(self, other):
			return self.value >= other.value
			
		def __lt__(self, other):
			return self.value < other.value
			
		def __le__(self, other):
			return self.value <= other.value
		
		def __eq__(self, other):
			return self.letter == other
		
		def __repr__(self):
			return "[" + self.letter + ", " + str(self.value) + "]"


	def __init__(self, inp):
		self.raw_string = inp

		node_list = HuffmanFactory.generate_node_list(self.raw_string)
		self.huffman_tree = HuffmanFactory.generate_tree(node_list)
		self.compression_dictionary = HuffmanFactory.generate_dict(self.huffman_tree)
		self.compressed_string = HuffmanFactory.compress_string(self.raw_string, self.compression_dictionary)

	def generate_node_list(inp, nodes = []):
		for i in inp:
			if i not in nodes:
				nodes.append(HuffmanFactory.HuffmanNode(1, i))
			else:
				for k in nodes:
					if k.letter == i:
						k.value = k.value + 1
						break
		nodes = sorted(nodes)[::-1]
		return nodes

	def generate_tree(nodes):
		nodes = sorted(nodes)[::-1] 
		while len(nodes) > 1:
			node1 = nodes.pop()
			node2 = nodes.pop()
			new_node = HuffmanFactory.HuffmanNode(node1.value + node2.value, "", node1, node2)
			nodes.append(new_node)
			nodes = sorted(nodes)[::-1]
		return nodes[0]

	def generate_dict(tree, dic = {}):
		def helper(tree, path):
			nonlocal dic
			if tree.is_leaf():
				dic[tree.letter] = path
			else:
				helper(tree.left, path + "0")
				helper(tree.right, path + "1")
		helper(tree, "")
		return dic
	def compress_string(inp, dic):
		s = ""
		for i in inp:
			s += dic[i]
		return s

	def compare_lengths(self):
		len_difference = (len(self.raw_string) * 8) - len(self.compressed_string)
		percent_difference = (len_difference / (len(self.raw_string) * 8)) * 100
		print("Original String Length (bits): " + str(len(self.raw_string) * 8) + " bits.")
		print("Compressed String Length (bits): " + str(len(self.compressed_string)) + " bits.")
		print("Compression decreases space required by ~" + str(percent_difference) + "%.")
