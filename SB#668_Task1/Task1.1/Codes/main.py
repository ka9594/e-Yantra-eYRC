import cv2
import numpy as np
import math
import os
import csv


def getCenter(lower_color, upper_color):
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(img,img, mask= mask)

    res = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    res = cv2.medianBlur(res,5)
    circle = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,2,20,param1=50,param2=10,minRadius=0,maxRadius=20)

    return circle[0,0,0], circle[0,0,1]

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang



stats = []
for f in os.listdir('../Images/'):
    if f.endswith('.png'):
        temp = []
        path = '../Images/'
        path = path+f
        temp.append(f) #ROW NAME
        
        img = cv2.imread(path,1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,255,255])
        upper_red = np.array([10,255,255])

        lower_green = np.array([20,255,255])
        upper_green = np.array([60,255,255])

        red_center = getCenter(lower_red, upper_red)
        green_center = getCenter(lower_green, upper_green)

        img_center = img.shape[0]/2, img.shape[1]/2

        angle = round(getAngle(red_center, img_center, green_center),2)
        if angle>180:
            angle = 360-angle

        temp.append(str(round(angle,2)))

        # print(str(round(angle,2)))

    with open('../Generated/angles.csv', 'a') as stat:
        write = csv.writer(stat)
        write.writerow(temp)




