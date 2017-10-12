import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# prepare object points
nx = 9#TODO: enter the number of inside corners in x
ny = 5#TODO: enter the number of inside corners in y

def showMyWindow(img):
    plt.imshow('Self Driving Car: Advanced Lane Finding', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Self Driving Car: Advanced Lane Finding')


# Make a list of calibration images
fname = 'camera_cal/calibration1.jpg'
img = cv2.imread(fname)
print(img.shape)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
print(gray.shape)

# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    cv2.imshow('image', img)
    cv2.waitKey(10000)
    cv2.destroyWindow('image')

else:
    print('Hi')
