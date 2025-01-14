"""
Data Compression Project 3 in python
Catarina Bores, 73865
Francisco Aires, 76490
"""
"""
Data Compression contains class BitStream and all the functions to read and write bits from a file.
Contains the Golomb coding and decoding
"""

import os
from bitstring import ConstBitStream
import math
from bitstring import BitArray


class BitStream:

    def __init__(self, output, type):
        """
        Init method or constructor
        @:param self The object pointer
        @:param file_name it's the file that we want to read
        @:param byte it's the stream
        """
        self.file_name = output
        # self.stream = ConstBitStream(filename=file_name)
        self.f = open(output, type)
        self.byte = ''

    def __str__(self):
        return None

    # The resulting file should be binary
    # the minimum amount of data that you can access in a file is one byte (8 bits)
    def readbit(self):
        """
        """
        return self.f.read(1)

    def readbits(self, byte):
        """
        @:param nbits
        """
        bits = '{0:08b}'.format(int(byte))
        return bits

    def writebit(self, bit='1'):
        """
        @:param bit
        """

        self.byte += bit
        if len(self.byte) >= 8:
            self.f.write(int(self.byte[:8], 2).to_bytes(1, byteorder='big'))
            self.byte = self.byte[8:]

    def writebits(self, bits):
        """
        @:param bits
        """

        self.byte += bits
        while len(self.byte) >= 8:
            self.f.write(int(self.byte[:8], 2).to_bytes(1, byteorder='big'))
            self.byte = self.byte[8:]


def golomb_code(x, m):
    """
    @:param x the value we want to transform in the golomb code
    @:param m is the parameter of the Golomb code
    Calculates quocient (quo) and remainder (remin)
    """
    c = int(math.ceil(math.log(m, 2)))
    remin = x % m
    div = int(math.pow(2, c) - m)
    quo = int(math.floor(x / m))

    first = ""
    for i in range(quo):
        first += "1"
    if remin < div:
        b = c - 1
        a = "{0:0" + str(b) + "b}"
        bi = a.format(remin)

    else:
        b = c
        a = "{0:0" + str(b) + "b}"
        bi = a.format(remin + div)

    final = first + "0" + str(bi)

    return final


def golomb_decode(x, m, frame_size):
    """
    @:param x is the value to decode
    @:param m is the parameter of the Golomb code
    Does the decoding of the golomb_code
    """
    k = math.ceil(math.log(m, 2))
    div = int(math.pow(2, k) - m)
    s = 0  # number of consecutive ones
    counter = 0
    number_counter = 0
    frames = []
    frame = []
    i = 0
    while i < len(x):
        if x[i] == '1':
            s += 1  # number of consecutive ones
            i+=1
        else:
            n = x[i+1 : i + k]
            n = int(n,2)
            if (n < div):
                s = s * m + n
            else:
                n = n * 2 + int(x[i+k])
                s = s * m + n - div
            frame += [s]
            number_counter+=1
            s = 0
            i += k + 1
            if number_counter == frame_size:
                counter += 1
                frames += [frame]
                number_counter = 0
                frame = []

    return frames

"""
Testing Golomb Code

m = 4
golocode = ''

numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 100, 200, 255, 99, 70, 90]

for s in numbers:
    golocode += golomb_code(s, m)
print(golocode)

decoded = golomb_decode(golocode, m, 1)
print(decoded)

Testing is over
"""