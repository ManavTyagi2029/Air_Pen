import cv2
import numpy as np
def nothing(a):
    pass
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
mybgr = [[150,94,221],[217,207,47],[40,171,26]]
mycolor = [[124,122,104,255,255,255],[81,75,96,163,255,255],[31,107,0,88,255,146]]

def getpos(mask):
    x,y,w,h = 0,0,0,0
    cont,h = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i in cont:
        a = cv2.contourArea(i)
        if a>250:
            p=cv2.arcLength(i,True)
            app =  cv2.approxPolyDP(i,0.02*p,True)
            x,y,w,h = cv2.boundingRect(app)
    return x+w//2,y

def colord(img):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    pr = []
    count = 0
    for c in mycolor:
        lower = np.array(c[0:3])
        upper = np.array(c[3:6])
        mask = cv2.inRange(hsv,lower,upper)
        cv2.imshow(str(c[0]),mask)
        x,y = getpos(mask)
        cv2.circle(img1,(x,y),9,mybgr[count],cv2.FILLED)   
        if x!=0 and y!=0:
            pr.append([x,y,count])
        count = count+1
    return pr

def drawp(p):
    for o in p:
        cv2.circle(img1,(o[0],o[1]),10,mybgr[o[2]],cv2.FILLED)
p = []
while (1):
    ret,frame=cap.read()
    img1 = frame.copy()
    pr=colord(frame)
    if len(pr)!=0:
        for j in pr:
            p.append(j)
    if len(p)!=0:
        drawp(p)
    video = cv2.flip(img1,1)
    cv2.imshow('a',video)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
