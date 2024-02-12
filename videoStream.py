from centerLine import *
import cv2 as cv
import numpy as np

def videoStreamProcess(port):
   #open video
   capture = cv.VideoCapture(port)
   upperLeft = (530,270)
   bottomRight = (1390,850)


   while True:
       #capture frame
       ret, frame = capture.read()

       #if frame is read correctly ret is True

       if not ret:
           print("Can't receive frame (stream end?). Exiting ...")
           break

       # mask
       rect = cv.rectangle(frame, upperLeft, bottomRight, (0,0,0), 5)
       rectFrame = frame[upperLeft[1]: bottomRight[1], upperLeft[0]:bottomRight[0]]

       # process frame
       procFrame = rectFrame
       try:
          procFrame, nayFrame = centerLine(rectFrame)
       except:
           procFrame=centerLine(rectFrame)

       # replace mask
       try:
           frame[upperLeft[1]: bottomRight[1], upperLeft[0]:bottomRight[0]]=procFrame

       except:
           pass

       #Display the resulting frame
       cv.imshow('frame', frame)
       try:
          cv.imshow('nay',nayFrame)
       except:
           pass
       if cv.waitKey(1) == ord('q'):
           break

   capture.release()
   cv.destroyAllWindows()




