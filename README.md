# Huffman-Encoding
Simple implementation of the Huffman Encoding compression system.

# Explanation

The idea behind Huffman Encoding is building a tree with the letters from the input, using 
weights assigned as the number of times the letter appears in the input string. 

The novelty of Huffman's system was the idea of building the tree from bottom up. Previous attempts
were innefficient because they attempted to construct the tree from the top down, and so weren't
able to create an optimal tree. 


There are three main steps to doing Huffman Encoding.  

First, the input is parsed into a list of (letter, weight) pairs, where the weight is the number
of times that each letter appears in the string. We then order this list by weight, from heighest
to lowest. Each of these pairs is a node of our Huffman tree. 

input_string = "hello this is a samplet"

_: 4
l: 3
s: 3
h: 2
e: 2
t: 2
i: 2
a: 2
m: 1
p: 1
o: 1

Second, we build our actual tree. We do this by popping off the last two values in our list, then creating
a new node where the value of the node is the sum of the two values that we've combined, and the left and
right branches hold the letters that we added together.

Step 0: (_, 4), (l, 3), (s, 3), (h, 2), . . . (m, 1), (p, 1), (o, 1)

Now we pop the last two nodes (p and o), combine them, create a new node, stick that node back into the list, and
sort the list again.

Step 1: (_, 4), (l, 3), (s, 3), (h, 2), . . . ( , 2), (m, 1)
                                              /    \
                                          (p, 1), (o, 1)

Now we do the same thing, poping the last two nodes (m and the combined p & o node), combine them, create a new
node, stick that node back in the list, and sort the list. 

Step 3: (_, 4), (l, 3), (s, 3), . . . ( , 3), (h, 2)
									  /    \
								 ( , 2)    (m, 1)
                                 /    \
                             (p, 1), (o, 1)

This process continues until we have a single node in our list, which is now our tree. In this case, this node
looks like this:


