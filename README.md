# image_processing_Assignment_28

# imutils
A series of convenience functions to make basic image processing functions such as approxPolyDP,adaptiveThreshold, resizing, four_point_transform, and displaying Matplotlib images easier with OpenCV and Python 3.

For more information, along with a detailed code review check out the following posts on the [PyImageSearch.com]


## Installation
Provided you already have NumPy, Matplotlib, and OpenCV already installed, the `imutils` package is completely `pip`-installable:

<pre>$ pip install imutils</pre>


## Executing
### Run

```shell
cd <Sudoku_HOME>
python3 image_processing_Assignment_28/sudoku.py --input sudoku.jpg --output result.jpg
```
### Help
```shell
cd <Sudoku_HOME>
python3 image_processing_Assignment_28/sudoku.py --help
```

## Finding function OpenCV functions by name
OpenCV can be a big, hard to navigate library, especially if you are just getting started learning computer vision and image processing. The `find_function` method allows you to quickly search function names across modules (and optionally sub-modules) to find the function you are looking for.

#### Example:
Let's find all function names that contain the text `contour`:

<pre>import imutils
imutils.find_function("contour")</pre>

#### Output:
<pre>1. drawContours
2. findContours</pre>


Here we are converting our BGR image to a grayscale image.
#### Output:
<img src="output/imgGray.jpg" alt="grayscale image" style="max-width: 500px;">

Here we are using Gaussian Blur to remove the Gaussian Noise from the image.
#### Output:
<img src="output/imgBlur.jpg" alt="Gaussian Blur mask" style="max-width: 500px;">

Here we are threshold to applying different thresholding techniques on the input image.
#### Output:
<img src="output/thresh.jpg" alt="Gaussian Blur mask" style="max-width: 500px;">

Here, since our background image is white, we need the background of our photo to be black for better image processing, 
that's why we use cv2.bitwise_not.
#### Output:
<img src="output/threshBitwiseNot.jpg" alt="Gaussian Blur mask" style="max-width: 500px;">

Finding all the contours in the image
Sorting the contours in descending order based on their contour area.
Traversing in contours and finding the contour with 4 sides using cv2.approxPolyDP().
We are simply drawing line around of the rectangle. These are the points that we got above in the contour detection step using the CHAIN_APPROX_SIMPLE method.
#### Output:
<img src="output/result.jpg" alt="drawing line around of the rectangle" style="max-width: 500px;">

## Cropping
We are applying the `four-point-transformation` to the image. It means that we will only extract the document from the image. Or we can also say that we just want to extract the rectangle formed by the four points.

## Resizing
Resizing an image in OpenCV is accomplished by calling the `cv2.resize` function. However, special care needs to be taken to ensure that the aspect ratio is maintained.  This `resize` function of `imutils` maintains the aspect ratio and provides the keyword arguments `width` and `height` so the image can be resized to the intended width/height while (1) maintaining aspect ratio and (2) ensuring the dimensions of the image do not have to be explicitly computed by the developer.

#### Example:
<pre># resize the image to
for width in (500, 500):
	# resize the image and display it
plate = imutils.resize(cropSudoku, height = 500)
cv2.imshow("Width=%dpx" % (width), plate)</pre>

#### Output:

<img src="output/crop.jpg" alt="Resizing example" style="max-width: 500px;">
