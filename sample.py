import HuffmanCompression

inp = "sample"
huff = HuffmanCompression.HuffmanFactory(inp)
print(huff.compressed_string)
huff.compare_lengths()

