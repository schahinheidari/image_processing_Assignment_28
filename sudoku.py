import argparse
import cv2 as cv
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description="Sudoku Detector")
parser.add_argument("--input", type=str,help="path of your input image")
parser.add_argument("--filter-size", type=str,help="size of GaussianBlur mask", default=7)
parser.add_argument("--output", type=str,help="path of your output image")

args = parser.parse_args()

img = cv.imread(args.input)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (args.filter_size,args.filter_size), 3)
plt.imshow(imgBlur, cmap="gray")
thresh = cv.adaptiveThreshold(imgBlur, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=2)
plt.imshow(thresh, cmap="gray")
#thresh = cv.adaptiveThreshold(imgBlur, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=2)

thresh = cv.bitwise_not(thresh)
plt.imshow(thresh, cmap="gray")
contours = cv.findContours(thresh, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
contours = contours[0]
contours
contours = sorted(contours, key=cv.contourArea, reverse=True)
sudokuContour = None
for contour in contours:

    epsilon = 0.01 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4 :
        sudokuContour = approx
        break
        
if sudokuContour is None:
    print("can't find sudoku table..." )
else:
    result = cv.drawContours(img, [sudokuContour], -1, (0,255,0), 4)
    plt.imshow(result)
    cv.imwrite(args.output, result)
