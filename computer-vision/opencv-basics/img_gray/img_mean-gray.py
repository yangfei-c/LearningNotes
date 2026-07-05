import cv2
import numpy as np

img=cv2.imread("../../img/ZhaoJinMai2.webp")
if img is None:
    print("图像不存在请检查路径")
else:
    h,w=img.shape[:2]
    img_gray=np.zeros((h,w,3),np.uint8)
    for i in range(h):
        for j in range(w):
            gray=(int(img[i,j][0])+int(img[i,j][1])+int(img[i,j][2]))//3
            img_gray[i][j]=np.uint8(gray)
    cv2.imshow("origin",img)
    cv2.imshow("img_gray",img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()