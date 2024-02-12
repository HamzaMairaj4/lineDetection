import numpy as np

#Find a line if you're given two points
def findLine(x1,y1,x2,y2):
   #Find the slope of the joining line
   try:
       slope = (y2-y1)/(x2-x1)

   #Find intercept (y=mx+b)
       inter = y1-(slope*x1)

   #return a dict with [slope, b]
       return {"slope":slope,"intercept":inter}
   except:
       print("No Slope! Terminating...")

#Find a middle line between two true parallel lines
def findParallelCenter(slope,int1,int2):
   #Find average Intercept
   aveInt=(int1+int2)/2

   #Establish middle line
   intSlope={"slope":slope,"intercept":aveInt}

   #return intSlope
   return intSlope

#Find the center line between two non-parallel lines
def findCenterLines(xz,yz,xz2,yz2):
    stX=0
    stY=0
    enX=0
    enY=0
    for i in range(len(xz)):
        stX+=xz[i]
        stY+=yz[i]
        enX+=xz2[i]
        enY+=yz2[i]
    stX=stX/len(xz)
    stY=stY/len(xz)
    enX=enX/len(xz2)
    enY=enY/len(yz2)

    return stX,stY,enX,enY
