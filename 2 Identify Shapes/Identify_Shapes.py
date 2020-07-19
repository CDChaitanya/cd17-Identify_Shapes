# Identify Shapes

import cv2
import numpy as np

# Loading and then gray scale image
image = cv2.imread('someshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Identifying Shapes' , image)
cv2.waitKey(0)

ret , thresh = cv2.threshold(src=gray, thresh=127, maxval=255, type=1)

#Extract Contours
contours , hierarchy = cv2.findContours(image=thresh.copy(), mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    
    # GETTING APPROXIMATE POLYGON 
    approx = cv2.approxPolyDP(curve=cnt, epsilon=0.01*cv2.arcLength(curve=cnt , closed=True), closed=True)
############################## TRIANGLE #########################
    if len(approx) == 3:
        shape_name = "TRIANGLE"
        cv2.drawContours(image=image, contours=[cnt], contourIdx=0, color=(0,255,0), thickness=-1)
        
        # Finding Contour Center TO place THE TEXT AT CENTER
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img=image, text=shape_name, org=(cx-50,cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=1)
############################## RECTANGLE #########################

    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(cnt)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # CHECK TO SEE IF 4 SIDE polygon IS SQUARE OR RECTANGLE
        if abs(w-h) <= 3:
            shape_name = "SQUARE"
            cv2.drawContours(image=image, contours=[cnt], contourIdx=0, color=(0,125,255), thickness=-1)
            cv2.putText(img=image, text=shape_name, org=(cx-50,cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=1)
        else:
            shape_name = "RECTANGLE"
            cv2.drawContours(image=image, contours=[cnt], contourIdx=0, color=(0,0,255), thickness=-1)
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(img=image, text=shape_name, org=(cx-50,cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=1)
############################## STAR #########################        

    elif len(approx) == 10:
        shape_name = "STAR"
        cv2.drawContours(image=image, contours=[cnt], contourIdx=0, color=(255,255,0), thickness=-1)
        
        # Finding Contour Center TO place THE TEXT AT CENTER
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img=image, text=shape_name, org=(cx-50,cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=1)
############################## CIRCLE #########################  
     
    elif len(approx) >= 15:
        shape_name = "CIRCLE"
        cv2.drawContours(image=image, contours=[cnt], contourIdx=0, color=(0,255,255), thickness=-1)
        
        # Finding Contour Center TO place THE TEXT AT CENTER
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img=image, text=shape_name, org=(cx-50,cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=1)
##############################################################
        
    cv2.imshow('Identifing Shapes', image)
    cv2.waitKey(0)
    