import cv2
import numpy as np
import os

fps = 25
sec_req = 6
frame_req = sec_req*fps+1

def partA():

    count = 0
    path = '../Videos/RoseBloom.mp4'
    vid = cv2.VideoCapture(path)
    ack,frame = vid.read()
    while ack:
        if count == (frame_req):
            cv2.imwrite('../Generated/frame_as_6.jpg', frame)
            break
        else:
            ack,frame = vid.read()
            count = count +1

    pass

def partB():

    count = 0
    path = '../Videos/RoseBloom.mp4'
    vid = cv2.VideoCapture(path)
    ack,frame = vid.read()
    while ack:
        if count == (frame_req):
            frame[:,:,0] = 0
            frame[:,:,1] = 0 #REMOVE OTHER CHANNELS CONTRIBUTION
            cv2.imwrite('../Generated/frame_as_6_red.jpg', frame)
            break
        else:
            ack,frame = vid.read()
            count = count +1

    pass

partA()
partB()