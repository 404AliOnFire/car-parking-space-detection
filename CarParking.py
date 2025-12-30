import cv2 as cv
import pickle
import numpy as np

pos_list = []
width = 108
height = 46

try:
    with open('car_pos','rb') as f:
        pos_list = pickle.load(f)
except FileNotFoundError:
    pos_list = []

def mouse_click(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        pos_list.append((x,y))
    elif event == cv.EVENT_RBUTTONDOWN:
            for i,pos in enumerate(pos_list):
               x1,y1 = pos
               if x1 < x < x1 + width and y1 < y < y1 + height:
                   pos_list.pop(i)

    with open('car_pos','wb') as f:
        pickle.dump(pos_list, f)




while True:
    frame = cv.imread('carParkImg.png')
    for pos in pos_list:
        cv.rectangle(frame,pos,(pos[0] + width, pos[1] + height), (0, 0, 255), 2)

    cv.imshow('Image',frame)
    cv.setMouseCallback('Image',mouse_click)
    cv.waitKey(1)





