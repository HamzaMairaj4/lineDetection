from alg1 import *
from laneDetection import *
import numpy as np

def centerLine(frame):
   try:
      lineFrame,nayFrame=genesis(frame)

      return lineFrame, nayFrame
   except:
      lineFrame=genesis(frame)

      return lineFrame