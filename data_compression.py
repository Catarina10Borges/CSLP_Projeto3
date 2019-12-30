"""
@:mainpage Data Compression Project 3
@:author name Catarina Bores, 73865
@:author  Francisco Aires, 76490
"""
"""
Data Compression contains class BitStream and all the functions to read and write bits from a file.
Contains, also, the Golomb code
"""

import os
from bitstring import ConstBitStream
import math

class BitStream:

    def __init__(self, output, rw):
        """
        Init method or constructor
        @:param self The object pointer
        @:param file_name it's the file that we want to read
        @:param stream it's the 8 bit stream
        """
        self.file_name = output
        #self.stream = ConstBitStream(filename=file_name)
        self.f = open(output, rw)
        self.byte = ''

    def __str__(self):
        return None

    # The resulting file should be binary
    # the minimum amount of data that you can access in a file is one byte (8 bits)
    def readbit(self):
        """
        Reads bit by bit, an then transforms it to byte streams
        """
        return self.f.read(1)

    def readbits(self, nbits):
        """
        Reads all the bits, an then transforms it to byte streams
        @:param nbits
        """
        bits = self.f.read(nbits)
        return bits

    def writebit(self, bit='1'):
        """
        Writes the binary file with all the bits read
        @:param bit
        """

        self.byte += bit
        if len(self.byte) >= 8:
            self.f.write(int(self.byte[:8], 2).to_bytes(1, byteorder='big'))
            self.byte = self.byte[8:]

    def writebits(self, bits):
        """
        Writes all the bits read in the file
        @:param bits
        """

        self.byte += bits
        if len(self.byte) >= 8:
            self.f.write(int(self.byte[:8], 2).to_bytes(1, byteorder='big'))
            self.byte = self.byte[8:]

def golomb_code(x, m):
    """
    @:param x
    @:param m
    Calculates quocient (quo) and remainder (remin)
    """
    c = int(math.ceil(math.log(m, 2)))
    remin = x % m
    quo = int(math.floor(x / m))
    div = int(math.pow(2, c) - m)
    first = ""
    for i in range(quo):
        first += "1"
    if (remin < div):
        b = c - 1
        a = "{0:0" + str(b) + "b}"
        #print("1",a.format(remin))
        bi = a.format(remin)
    else:
        b = c
        a = "{0:0" + str(b) + "b}"
        #print("2",a.format(remin+div))
        bi = a.format(remin + div)

    final = first + "0" + str(bi)
    #print("final",final)
    return final

def golomb_decode(s, m):
    """
    @:param x
    @:param m
    Calculates quocient (quo) and remainder (remin)
    """
    k = math.ceil(math.log(m, 2))
    print('k',k)
    c = 0
    x = ''
    for i in s:
        if i == '1':
            c += 1
        else:
            break
    #print('c',c)
    for i in s[c+1:c+k+1]:
        x += i

    print('x', x)
    x = int(x,2)
    print('x', x)
    #print('x', x)
    c = c*m+x
    return c



"""
Testing the BitStream Class
"""

bitstream = BitStream('test.bin','wb')

m = 2
golocode = []
"""
for s in range(0,int(len(bitstream.stream)/8)):
    byte = bitstream.stream.read(8).tobytes()
    int_fromb = int(byte.decode("utf-8"))
    print("Golomb coding result for", s, "with parameter m equals", m, "is", bitstream.golomb_code(int_fromb, m))
    golocode += [bitstream.golomb_code(int_fromb, m)]
"""
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100,200,255]
for s in numbers:
    golocode += [golomb_code(s,m)]
print(golocode)

decoded = []
for s in golocode:
    decoded += [golomb_decode(s,m)]
print(decoded)

#bitstream.writebits(golocode, 'output.bin')

bitstream2 = BitStream('output2.bin','wb')
bitstream2.writebit()
bitstream2.writebits('0000000')
bitstream2.writebits('10101010')
bitstream2.f.close()
bitstream2.f = ConstBitStream(filename='output2.bin')



