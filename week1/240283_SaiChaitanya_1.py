import cv2
import numpy as np
img=cv2.imread("supermario.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sharp=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0],
])

img=cv2.filter2D(img,-1,sharp)

img_blur=cv2.GaussianBlur(img,(3,3),sigmaX=1,sigmaY=1)
img_blur=cv2.Laplacian(img_blur,-1)
_,img_blur=cv2.threshold(img_blur,10,255,cv2.THRESH_BINARY)


cv2.imshow("supermario!", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
