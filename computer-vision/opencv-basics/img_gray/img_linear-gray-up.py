#灰度上移提升亮度
import cv2
import numpy as np

img=cv2.imread("../../img/LinYunEr.jpg")

h,w=img.shape[:2]
img_gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

result=np.zeros((h,w),np.uint8)
for i in range(h):
    for j in range(w):
        if(int(img_gray[i,j]+50)>255):
            gray=255
        else:
            gray=int(img_gray[i,j]+55)
        result[i,j]=np.uint8(gray)
cv2.imshow("origin",img_gray)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()