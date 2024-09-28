#打马赛克
import cv2

img=cv2.imread("../../img/ChenYao.jpg")
en=False
def draw(event,x,y,flag,param):
    global en
    if event==cv2.EVENT_LBUTTONDOWN:
        en=True
    elif event==cv2.EVENT_MOUSEMOVE and flag==cv2.EVENT_LBUTTONDOWN:
        if en:
            drawMask(y,x)
        elif event==cv2.EVENT_LBUTTONUP:
            en=False
def drawMask(x, y, size=20):
     #size*size 采样处理
     m = int(x / size * size)
     n = int(y / size * size)
     print(m, n)
     #10*10 区域设置为同一像素值
     for i in range(size):
         for j in range(size):
            img[m+i][n+j] = img[m][n]
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(10)&0xFF==27:
        break
    elif cv2.waitKey(10)&0xFF==115:
        cv2.imwrite('img_sample.jpg',img)
cv2.destroyAllWindows()

