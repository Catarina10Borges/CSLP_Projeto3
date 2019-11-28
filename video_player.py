import cv2
import numpy as np

filename = "akiyo_cif.y4m"

f = open(filename, 'rb')

line = f.readline().decode()
config = line.split(' ')
print(config)
w = int(config[1][1:])
h = int(config[2][1:])
frame_ratio = config[3][1:].split(':')
frame_rate = int(round(int(frame_ratio[0])/int(frame_ratio[1])))
print(f.readline().decode())
next_line = f.readline()
print(next_line[:w*h*3])









# play_video(cap)
# Closes all the frames
cv2.destroyAllWindows()
