"""
Data Compression
class BitStream
"""

# import numpy as np
import os
from bitstring import ConstBitStream
import math


class BitStream:
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
        f = open('output.bin', 'wb+')
        f.write(bit)

    def readbits(self, nbits):
        bits = self.stream.read(nbits).tobytes()
        return bits

    def writebits(self, bits):
        f = open('output.txt', 'wb+')
        for i in bits:
            f.write(int(i,2).to_bytes(len(i), byteorder='big'))

    def golomb_code(self, x, m):
        c = int(math.ceil(math.log(m, 2)))
        remin = x % m
        quo = int(math.floor(x / m))
        # print "quo is",quo
        # print "reminder",remin
        # print "c",c
        div = int(math.pow(2, c) - m)
        # print "div",div
        first = ""
        for i in range(quo):
            first = first + "1"
        # print first

        if (remin < div):
            b = c - 1
            a = "{0:0" + str(b) + "b}"
            # print "1",a.format(remin)
            bi = a.format(remin)
        else:
            b = c
            a = "{0:0" + str(b) + "b}"
            # print "2",a.format(remin+div)
            bi = a.format(remin + div)

        final = first + "0" + str(bi)
        # print "final",final
        return final


bitstream = BitStream('test.bin')

m = 4
golocode = []
for s in range(0,int(len(bitstream.stream)/8) - 1):
    byte = bitstream.stream.read(8).tobytes()
    int_fromb = int(byte.decode("utf-8"))
    golocode += [bitstream.golomb_code(int_fromb, m)]

print(golocode)
bitstream.writebits(golocode)

bitstream2 = BitStream('output.txt')
print(bitstream2.readbits(64))