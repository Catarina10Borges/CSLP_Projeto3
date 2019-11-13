"""
Data Compression
class BitStream
"""

# import numpy as np
import os
from bitstring import ConstBitStream


class BitStream:
    array = []
    """
    @:param file_name it's the file name that we want to read
    @:param bitcount counts how many bits 
    @:param counter counts 
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.stream = ConstBitStream(filename=file_name)

    def __str__(self):
        return None

    # The resulting file should be binary
    # the minimum amount of data that you can access in a file is one byte (8 bits)
    def readbit(self):
        return self.stream.read(1).tobytes()

    def writebit(self, bit):
        f = open('output.txt', 'wb+')
        f.write(bit)

    def readbits(self, nbits):
        bits = self.stream.read(nbits).tobytes()
        return bits

    def writebits(self, bits, n):
        f = open('output.txt', 'wb+')
        f.write(bits)


bitstream = BitStream('test.txt')
bitstream.readbit()
bitstream.readbit()
bitstream.readbit()
print(bitstream.readbits(5))
print(bitstream.readbits(8))
bitstream.writebit(bitstream.readbits(16))
