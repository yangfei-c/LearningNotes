import cv2

# 读取图像
img = cv2.imread("../../img/LinYunEr.jpg")

# 检查图像是否加载成功
if img is None:
    print("检测不到图像，请检查图像路径是否错误")
else:
    # 多次降采样
    img_sample_down = cv2.pyrDown(img)
    img_sample_down1 = cv2.pyrDown(img_sample_down)
    img_sample_down2 = cv2.pyrDown(img_sample_down1)

    # 显示原始图像和降采样后的图像
    cv2.imshow("Original", img)
    cv2.imshow("Downsampled 1", img_sample_down)
    cv2.imshow("Downsampled 2", img_sample_down1)
    cv2.imshow("Downsampled 3", img_sample_down2)

    # 等待按键响应
    cv2.waitKey(0)

    # 关闭所有窗口
    cv2.destroyAllWindows()
