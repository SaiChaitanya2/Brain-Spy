import cv2
import numpy as np
img=cv2.imread("supermario.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
blur=blur/9

img=cv2.filter2D(img,-1,blur)

sharp = np.array([
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
])

img = cv2.filter2D(img,-1,sharp,)

_,img = cv2.threshold(img,6,255,cv2.THRESH_BINARY)

cv2.imshow("mario!",img)
cv2.waitKey(0)
cv2.destroyAllWindows