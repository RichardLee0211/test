openCV tutorial
from: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/
from: https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/data/home.jpg
Last update is 2014

openCV github: https://github.com/opencv/opencv/tree/master/samples/python

it doesn't seem that opencv-python has a nice document, and I hate it
here's one website with content of >>> help(cv2)
https://madebyollin.github.io/opencv-python-docs/

```python
# %%
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)

# %%

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# %%

import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
else:
    print("others")

# %%
## MacOS likes it more
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.axis("off")
plt.show()

# %%

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi4.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

# %%

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
```

```python

# %%

## For individual pixel access, Numpy array methods, array.item() and array.itemset() is considered to be better
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.dtype) # datatype

## wenchen: so if take img as matrix, x axis growing downward becomes reasonable

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

b,g,r = cv2.split(img) ## costly
img = cv2.merge((b,g,r))

```

boarder
```python

# %%

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate =     cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_REPLICATE)
reflect =       cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_REFLECT)
reflect101 =    cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_REFLECT_101)
wrap =          cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_WRAP)
constant=       cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

# %%

## OpenCV addition is a saturated operation while Numpy addition is a modulo operation.
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) # 250+10 = 260 => 255
print(x+y)          # 250+10 = 260 % 256 = 4

# %%

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv_logo.png')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

# %%

# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

plt.imshow(img1)
# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# %%

## Normally, OpenCV functions are faster than Numpy functions.
## 2333
%timeit

# %%

import cv2
import numpy as np

## this is so cool
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: # ESC key
        break

cv2.destroyAllWindows()

# %%

## scale
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

# %%

## translation (move)
import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],
				[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

# %%
M = np.float32([[1, 0, 0],
				[0, 1, 0],
				[0.001, 0, 1]])
dst = cv2.warpPerspective(img,M,(cols,rows))
plt.imshow(dst)

# %%

# rotated rectangle

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image, convert to grayscale, Otsu's threshold for binary image
# image = cv2.imread('./img/2Q1Sj.jpeg')
image = cv2.imread('2Q1Sj.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh_value, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours, find rotated rectangle, obtain four verticies, and draw
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
rect = cv2.minAreaRect(cnts[0])
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], 0, (36,255,12), 3) # OR
# cv2.polylines(image, [box], True, (36,255,12), 3)

plt.imshow(image[:, :, ::-1])
# cv2.imshow('image', image)
# cv2.waitKey()

# %%

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

# %%

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
dst = cv2.warpAffine(img,M,(cols+100,rows+100))

# %%

## affine transformation
img = cv2.imread('drawing.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

# %%

## perspective  transformation
img = cv2.imread('sudokusmall.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

# %%

## image filtering

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')

# %%

## Averaging

img = cv2.imread('opencv_logo.png')
blur1 = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
## salt and peper noisy
blur3 = cv2.bilateralFilter(img,9,75,75)
## this is very boring read

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.subplot(132),plt.imshow(blur1),plt.title('Blurred')
plt.subplot(133),plt.imshow(blur2),plt.title('Blurred')

# %%

import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion  = cv2.erode (img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
#...

# %%

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.png',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

# %%

## canny edge detection
## maybe read the wiki: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

# %%

## image pyramids
img = cv2.imread('messi5.jpg')
# lower_reso = cv2.pyrDown(higher_reso)
lower_reso = cv2.pyrDown(img)
higher_reso2 = cv2.pyrUp(lower_reso)

# %%

## pyramids blending
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

A = cv2.imread('./img/apple.png')
B = cv2.imread('./img/orange.png')
A = A[0:472, 0:472, :]
B = B[0:472, 0:472, :]

## im_rgb = im_bgr[:, :, ::-1]
# A_rbg = cv2.cvtColor(A, cv2.COLOR_BGR2RGB)
# B_rbg = cv2.cvtColor(B, cv2.COLOR_BGR2RGB)
# plt.imshow(A_rbg)
# plt.imshow(B_rbg)


# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    print(i)
    GE = cv2.pyrUp(gpA[i])
    if GE.shape != gpA[i-1].shape:
        min_dim = min(GE.shape[0], gpA[i-1].shape[0])
        GE = GE[0:min_dim, 0:min_dim, :]
        gpA[i-1] = gpA[i-1][0:min_dim, 0:min_dim, :]
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    if GE.shape != gpB[i-1].shape:
        min_dim = min(GE.shape[0], gpB[i-1].shape[0])
        GE = GE[0:min_dim, 0:min_dim, :]
        gpB[i-1] = gpB[i-1][0:min_dim, 0:min_dim, :]
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    # ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    ls = np.vstack((la[0:int(rows/2),:] , lb[int(rows/2):, :]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    if ls_.shape != LS[i].shape:
        min_dim = min(ls_.shape[0], LS[i].shape[0])
        ls_ = ls_[0:min_dim, 0:min_dim, :]
        LS[i] = LS[i][0:min_dim, 0:min_dim, :]
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)

# %%

## contour

import numpy as np
import cv2

im = cv2.imread('./messi4.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# %%

# contour features 1. moments

import cv2
import numpy as np

img = cv2.imread('star.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)

# %%

img = cv2.imread('home.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist,bins = np.histogram(img.ravel(),256,[0,256])
plt.hist(img.ravel(),256,[0,256])

# %%

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')
color = ('b','g','r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
plt.show()


# %%

img = cv2.imread('home.jpg',0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

# %%

## histogram equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('wiki.png',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max() # cdf/cdf.max() normal to [0, 1]

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

## 相当于构建了一个255 到255 的映射, 如果CDF 很陡峭, 很小的范围可以映射到很大的范围
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min()) # 按比例压缩到255范围
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

# %%

img = cv2.imread('wiki.png',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)

# %%

import numpy as np
import cv2

img = cv2.imread('tsukuba_l.png',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.jpg'l1)

# %%

import cv2
import numpy as np

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# %%
```

While it is not a good material to learn principals, only for APIs

TOCONTINUE: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
