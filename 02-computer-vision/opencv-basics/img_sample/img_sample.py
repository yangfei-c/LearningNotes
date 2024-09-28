import cv2
import numpy as np


def img_sample(h,w,level):
    new_img=np.zeros((h,w,3),np.uint8)
    numHeight=h//level
    numWeight=w//level
    for i in range(level):
        y=i*numHeight
        for j in range(level):
            x=j*numWeight
            b, g, r = img[y, x]
            # 填充整个网格区域
            new_img[y:y + numHeight, x:x + numWeight] = (b, g, r)
    return  new_img

img=cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("图像不存在请检查路径是否正确")
else:
    h,w=img.shape[:2]
    new_img=img_sample(h,w,min(h,w)-475)
            # b=img[y,x][0]
            # g=img[y,x][1]
            # r=img[y,x][2]
            # for n in range(numHeight):
            #     for m in range(numWeight):
            #         new_img[y+n,x+m][0]=np.uint8(b)
            #         new_img[y+n,x+m][1]=np.uint8(g)
            #         new_img[y+n,x+m][2]=np.uint8(r)
cv2.imshow("img",img)
cv2.imshow("sample",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()