import cv2 as cv
import numpy as np
from alg1 import *

def genesis(frame):
    while True:
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        grayFrame = cv.GaussianBlur(grayFrame, (5, 5), 13)

        #bypass canny edge detecting the edge
        canny=grayFrame[10:575,5:855]

        nayFrame = cv.Canny(canny,170,195)
        # cv.imshow('frame',grayFrame)
        # cv.waitKey(0)

        lineys = cv.HoughLinesP(nayFrame[5:575,5:855], 1, np.pi / 90, 81,maxLineGap=500)
        xv = []
        yv = []
        xv2 = []
        yv2 = []

        if lineys is None:
            print("Hough Line Transform Failed! Skipping Frame...")
            break
        else:
            for line in lineys:
                x1, y1, x2, y2 = line[0]
                cv.line(frame,(x1+5,y1+5),(x2+5,y2+5),(255,0,0),3)
                xv.append(x1+5)
                xv2.append(x2+5)
                yv.append(y1+5)
                yv2.append(y2+5)


        a,b,c,d=findCenterLines(xv,yv,xv2,yv2)

        cv.line(frame,(int(a),int(b)),(int(c),int(d)),(0,0,255),5)


        return frame, nayFrame
