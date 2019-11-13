import cv2
import numpy as np
import os



count =0 
for f in os.listdir('../Images/'):
    if f.endswith('.png'):
        path = '../Images/'
        path = path+f
        img = cv2.imread(path)

        mask = np.zeros(shape = img.shape, dtype='uint8') #MAKE AN EMPTY IMG OF SAME DIMENTIONS

        center = int(img.shape[0]/2), int(img.shape[1]/2)
        radius = 305
        color = 255,255,255
        thickness = 40
        cv2.circle(mask, center, radius, color, thickness)#DRAW THE CIRCLE


        res_circle = cv2.bitwise_and(src1 = img, src2 = mask)#CUT THAT CIRCLE FROM IMG


        hsv = cv2.cvtColor(res_circle, cv2.COLOR_BGR2HSV)

        lower_w = np.array([0,0,255])
        upper_w = np.array([255,1,255])


        mask_w = cv2.inRange(hsv, lower_w, upper_w)
        res = cv2.bitwise_and(res_circle,res_circle, mask= mask_w)#SEPARATE ONLY WHITE FOMR IMG
        count = count+1
        res = cv2.bitwise_not(res)

        cv2.imshow('res',res)
        cv2.waitKey(0)
        cv2.imwrite('../Generated/image_%d_fill_in.png'%count,res)
