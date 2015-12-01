class HuffmanFactory:
	"""Class used to create a Huffman tree and compress the input text based on that huffman tree. 

	>>> import HuffmanCompression
	>>> sample_input = "sample"
	>>> huff = HuffmanCompression.HuffmanFactory(sample_input)
	>>> print(huff.compressed_string)
	1001010100111110                            # bit representation (as string)
	>>> huff.compression_dictionary
	{'a': '101', 'p': '00', 'e': '110', 's': '100', 'm': '01', 'l': '111'}
	>>> huff.compare_lengths()
	Original String Length (bits): 48 bits.
	Compressed String Length (bits): 16 bits.
	Compression decreases space required by ~66.67%.
	"""
	raw_string = ""
	huffman_tree = None
	compression_dictionary = {}
	compressed_string = ""

	class HuffmanNode:
		"""Class used to represent each node in a Huffman tree.
		Will always have two branches.
		"""
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
			"""Return if the node has any branches or not. """
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

		def depth(self):
			if is_leaf(self):
				return 0
			else:
				return 1 + max(depth(self.left), depth(self.right))
		
		def __repr__(self):
			print()




	def __init__(self, inp):
		self.raw_string = inp

		node_list = HuffmanFactory.generate_node_list(self.raw_string)
		self.huffman_tree = HuffmanFactory.generate_tree(node_list)
		self.compression_dictionary = HuffmanFactory.generate_dict(self.huffman_tree)
		self.compressed_string = HuffmanFactory.compress_string(self.raw_string, self.compression_dictionary)

	def generate_node_list(inp, nodes = []):
		"""Create list of HuffmanNodes. If the HuffmanNode for a letter doesn't exist
		in the list, add it. If it does, increment its value by 1. """
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
		"""Merge nodes together, building from bottom to top, to create a Huffman tree. 

		Given pairs [e, 7], [t, 2], and [l, 1], creates a tree that looks like this:

			    ( )
		       /   \
		     ( )   (e) 
            /   \
          (t)   (l)

        Letters that appear more frequently will appear closer to the top of the tree,
        and so have a shorter representation. 
		"""
		nodes = sorted(nodes)[::-1] 
		while len(nodes) > 1:
			node1 = nodes.pop()
			node2 = nodes.pop()
			new_node = HuffmanFactory.HuffmanNode(node1.value + node2.value, "", node1, node2)
			nodes.append(new_node)
			nodes = sorted(nodes)[::-1]
		return nodes[0]

	def generate_dict(tree, dic = {}):
		"""Create dictionary based on the Huffman tree. Left branch is represented by a 0,
		and right branch is represented by a 1.

		        ( )
		       /   \
		     ( )   (e) 
            /   \
          (t)   (l)

        In this case, e is represented by "1", t is represented by "00", and l is represented by "01". 
        """
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
		"""Create compressed string based on the dictionary created in earlier steps. 

		>>> dict = {'a': '101', 'p': '00', 'e': '110', 's': '100', 'm': '01', 'l': '111'}
		>>> compressed = compress_string("sample", dict)
		>>> print(compressed)
		1001010100111110
		"""

		s = ""
		for i in inp:
			s += dic[i]
		return s

	def compare_lengths(self):
		"""Compare amount of memory required to store the string pre-compression
		and post-compression, printing out the individual bit requirements and then the
		percent difference. """

		len_difference = (len(self.raw_string) * 8) - len(self.compressed_string)
		percent_difference = (len_difference / (len(self.raw_string) * 8)) * 100
		print("Original String Length (bits): " + str(len(self.raw_string) * 8) + " bits.")
		print("Compressed String Length (bits): " + str(len(self.compressed_string)) + " bits.")
		print("Compression decreases space required by ~" + "{0:.2f}".format(percent_difference) + "%.")
