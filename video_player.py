import cv2
import numpy as np

from Frame import Frame
from Video import Video
from data_compression import BitStream
from collections import Counter
import matplotlib.pyplot as plt

videoReader = BitStream('akiyo_cif.y4m')
f = open('akiyo_cif.y4m', 'rb')
bits = videoReader.readbits(43)
first_line = bits.decode().split(' ')
print(first_line)
w = int(first_line[1][1:])
h = int(first_line[2][1:])
frame_ratio = first_line[3][1:].split(':')
frame_rate = int(round(int(frame_ratio[0])/int(frame_ratio[1])))
print(frame_rate)
videoReader.readbit()
i = 0
l = 0
f = 0
frame = b''
frame_size = int(w*h*3/2)
print(frame_size)
bytes = videoReader.readbits(6)

def read_frame(frame):
    y = frame[:2*int(frame_size/3)]
    u = frame[2*int(frame_size/3):int(5*frame_size/6)]
    v = frame[int(5*frame_size/6):]
    y_array = np.frombuffer(y, dtype=np.uint8,count=w*h)
    u_array = np.frombuffer(u, dtype=np.uint8)
    v_array = np.frombuffer(v, dtype=np.uint8)
    y_matrix = np.reshape(y_array,(h,w))
    u_matrix = np.reshape(u_array,(h//2,w//2))
    v_matrix = np.reshape(v_array,(h//2,w//2))
    frame_object = Frame(y_matrix, u_matrix, v_matrix)
    return frame_object


def YUV2RGB(yuv):
    m = np.array([[1.0, 1.0, 1.0],
                  [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                  [1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]])

    rgb = np.dot(yuv, m)
    rgb[:, :, 2] -= 179.45477266423404
    rgb[:, :, 1] += 135.45870971679688
    rgb[:, :, 0] -= 226.8183044444304
    return np.uint8(rgb)


cap = cv2.VideoCapture('akiyo_cif.y4m')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")


frames = []
while True:
    if bytes == b'':
        break
    elif bytes == b'FRAME\n':
        f += 1
        frame = videoReader.readbits(int(frame_size))
        frame = read_frame(frame)
        frames += [frame]
        i += 1
        bytes = videoReader.readbits(6)
print(i)
video = Video('type', w, h, frame_rate, '4:2:0', frames)

entropy = dict()

for frame in video.frames:
    array = np.dstack((frame.y_matrix, frame.u_matrix.repeat(2, axis=0).repeat(2, axis=1),
                       frame.v_matrix.repeat(2, axis=0).repeat(2, axis=1)))
    BGR = cv2.cvtColor(array, cv2.COLOR_YUV2BGR)
    cv2.imshow('rgb',BGR)
    cv2.waitKey(1)
    unique, counts = np.unique(array, return_counts = True)
    temp = dict(zip(unique, counts))
    entropyC = Counter(entropy)
    tempC = Counter(temp)
    entropy = dict(entropyC + tempC)

cv2.destroyAllWindows()
"""
entropy = {k: v for k, v in sorted(entropy.items(), key=lambda item: item[1], reverse=True)}
#print(entropy)
entropyList = []
for i in entropy:
    entropyList += [(i,entropy[i])]
print(entropyList)
plt.bar(list(entropy.keys()), entropy.values(), color='g')
plt.show()
"""

