import cv2
import numpy as np
img=cv2.imread("supermario.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(img,(3,3),sigmaX=1,sigmaY=1)

sharp = np.array([
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
])

img = cv2.filter2D(img,-1,sharp,)

imgx=cv2.Sobel(img,-1,1,0)
imgy=cv2.Sobel(img,-1,0,1)
img=cv2.addWeighted(imgx,0.5,imgy,0.5,0)



_,img=cv2.threshold(img,15,255,cv2.THRESH_BINARY)

cv2.imshow("sobel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()