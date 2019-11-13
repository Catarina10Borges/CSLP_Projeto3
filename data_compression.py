"""
Data Compression
class BitStream
"""

import numpy as np


class BitStream:
    array = []
"""
@:param file_name it's the file name that we want to read
@:param bitcount counts how many bits 
@:param counter counts 
"""
    def __init__(self, file_name):
        self.filename = file_name
        self.bitcount = 0
        self.counter = 0

    def __str__(self):
        return None

    # The resulting file should be binary
    # the minimum amount of data that you can access in a file is one byte (8 bits)
    def readbit(self):
        file = self.filename
        bit = self.bit
        byte = self.byte

        f = open(file, 'rb')
        for x in f
            f.read(x) # reads character bem character
            x += 1

         f.close()
        # byte = f.read(1)  # reads one byte
        # bit  = byte & 0b00000001  # ler apenas 1 bit


    def writebit(self, bit):
        if self.bitcount == 8:
            return None
        if bit > 0:
            self.counter |= 1 << 7 - self.bitcount
        self.bitcount += 1

    def readbits(self, file, nbits):

        return None

    def writebits(self, bits, n):
        while n > 0:
            self.writeBit(bits & 1 << n - 1)
            self.n -= 1



