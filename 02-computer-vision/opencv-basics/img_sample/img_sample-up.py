import cv2
img=cv2.imread("../../img/lena.jpg")
if img is None:
    print("检测不到图像请检查图像路径是否错误")
else:
    img=cv2.resize(img,(25,25))
    img_sample_up=cv2.pyrUp(img)
    img_sample_up1=cv2.pyrUp(img_sample_up)
    img_sample_up2=cv2.pyrUp(img_sample_up1)
    cv2.imshow("original",img)
    cv2.imshow("upsample",img_sample_up)
    cv2.imshow("upsample1",img_sample_up1)
    cv2.imshow("upsample2",img_sample_up2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()