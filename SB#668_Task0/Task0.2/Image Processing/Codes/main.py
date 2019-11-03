import cv2
import numpy as np
import os
import csv


def partA():
    
    stats = []
    for f in os.listdir('../Images/'):
        if f.endswith('.jpg'):
            temp = []
            path = '../Images/'
            path = path+f
            temp.append(f) #ROW NAME
            
            img = cv2.imread(path,1)
            dimensions = list(img.shape)
            for d in dimensions:
                temp.append(d) #DIMENSIONS

            intensity = list(img[int(dimensions[0]/2,),int(dimensions[1]/2)])
            for i in intensity:
                temp.append(i) #CHANNEL INTENSITY

            with open('../Generated/stats.csv', 'a') as stat:
                write = csv.writer(stat)
                write.writerow(temp)

    pass

def partB():

    img = cv2.imread('../Images/cat.jpg',1)
    cat_red = img.copy()
    cat_red[:,:,0] = 0
    cat_red[:,:,1] = 0 #REMOVE OTHER CHANNELS CONTRIBUTION
    cv2.imwrite('../Generated/cat_red.jpg',cat_red)
    
    pass

def partC():

    img = cv2.imread('../Images/flowers.jpg',1)
    flowers_alpha = img.copy()
    flowers_alpha = cv2.cvtColor(flowers_alpha, cv2.COLOR_BGR2RGBA) #ADDING THE ALPHA CHANNEL
    flowers_alpha[:,:,3] = flowers_alpha[:,:,3]*0.5 #GIVING 50% TRANSPERENCY
    cv2.imwrite('../Generated/flowers_alpha.png',flowers_alpha)

    pass

def partD():
    img = cv2.imread('../Images/horse.jpg',1)
    horse_gray = img.copy()
    horse_gray[:,:,2] = (0.11*img[:,:,0])+(0.59*img[:,:,1])+(0.3*img[:,:,2]) #USING GIVEN EQUATION ON THE BGR CHANNEL
    horse_gray = cv2.cvtColor(horse_gray, cv2.COLOR_BGR2GRAY) #CONVERTING TO GRAYSCALE
    cv2.imwrite('../Generated/horse_gray.jpg',horse_gray)
    
    pass

partA()
partB()
partC()
partD()