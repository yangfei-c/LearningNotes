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

    # 对数变换函数图像绘制
    # 小c值：曲线较平缓，变化不剧烈，图像对比度提升效果较小。
    # 大 c值：曲线陡峭，对比度提升明显，低亮度部分的像素会被拉得更高，突出暗部细节
    def log_plot(c):
        x = np.arange(0, 256, 0.01)
        y = c * np.log(1 + x)
        plt.plot(x, y, 'r', linewidth=1)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title('对数变换函数')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(0, 255)
        plt.ylim(0, 255)
        plt.show()

    # 对数变换函数
    def log_transform(c, img):
        # 将图像转换为浮点型，避免溢出
        img_float = np.float32(img)
        # 应用对数变换
        output = c * np.log(1.0 + img_float)
        # 规范化输出到 0-255 并转换为 uint8 类型
        output = np.clip(output, 0, 255)  # 限制在 0-255 范围
        output = np.uint8(output)  # 转回 uint8 类型
        return output

    # 绘制对数变换函数图像
    log_plot(50)

    # 应用对数变换
    output = log_transform(50, img)

    # 显示原始图像和对数变换后的图像
    cv2.imshow("Input", img)
    cv2.imshow("Output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
