import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("../../img/log.png")

# 检查图像是否加载成功
if img is None:
    print("检测不到图像，请检查图像路径是否错误")
else:
    h, w = img.shape[:2]

    # 伽马变换函数图像绘制
    def gamma_plot(c, v):
        x = np.arange(0, 256, 0.01)
        y = c * x ** v
        plt.plot(x, y, 'r', linewidth=1)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title('伽马变换函数')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim([0, 255]), plt.ylim([0, 255])
        plt.grid(True)
        plt.show()

    # 伽马变换实现
    def gamma_transform(img, c, v):
        lut = np.zeros(256, dtype=np.float32)
        for i in range(256):
            lut[i] = c * i ** v
        # 使用 LUT 进行像素映射
        output_img = cv2.LUT(img, lut)
        output_img = np.uint8(np.clip(output_img + 0.5, 0, 255))  # 加入 clip 防止溢出
        return output_img

    # 调整 c 和 v 值来优化图像效果
    gamma_plot(0.00000005, 4.0)  # 调整 c 和 v 观察效果

    # 应用伽马变换
    output = gamma_transform(img, 0.00000005, 4.0)

    # 显示原始图像和处理后的图像
    cv2.imshow("Input", img)
    cv2.imshow("Output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
