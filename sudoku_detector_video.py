import numpy as np
import cv2 as cv
from imutils.perspective import four_point_transform 

cap = cv.VideoCapture(-1)
font = cv.FONT_ITALIC
fontSize = 1
textColor = (0, 0, 0)
thickness = 1

while True:

    
    ret, frame = cap.read()
    frame = cv.resize(frame,(700,700), fx = 0, fy = 0, interpolation=cv.INTER_CUBIC)
    filter = np.ones((50,50))/ 2500
    cv.rectangle(frame, (200,200), (500,500), (0,0,0), 4)
    point = frame[200:500, 200:500]

    res = cv.filter2D(frame, -1, filter)
    res[200:500, 200:500] = point
    detect = res[200:500, 200:500]
    
    if ret == False:
        break
        
    imgGray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (7,7), 3)
    thresh = cv.adaptiveThreshold(imgBlur, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=2)
    contours = cv.findContours(thresh, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0]
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    

    sudokuContour = None
    key = cv.waitKey(100)
    for contour in contours:
        epsilon = 0.01 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4 :
            sudokuContour = approx
            break
            
    if sudokuContour is None:
        cv.putText(res, "can't find sudoku table...", (10, 10), font, fontSize, textColor, thickness)

    else:
        result = cv.drawContours(res, [sudokuContour], -1, (0,255,0), 4)
        #cv.imshow("result",result)
        if key == 115 or 83: # press key 's' or 'S' ASCII
            cropSudoku = four_point_transform(res, approx.reshape(4,2))
            plate = cv.resize(cropSudoku, (600, 600))
            #cv.imshow(plate)
            cv.imwrite("crop.jpg" , plate)

    cv.imshow("frame", imgBlur)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break


cap.release()
cv.destroyAllWindows()