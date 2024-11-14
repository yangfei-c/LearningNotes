#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/14 20:15 
@file: 3.20.11.py
@email: ccc420513@gmail.com
"""
import os
import cv2
import numpy as np

# 读取图像
image_path = '../img/3.11/img.png'
image = cv2.imread(image_path)
image_name=os.path.splitext(os.path.basename(image_path))[0]
if image is not None:
    # 高斯模糊
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(f'../img/3.11/{image_name}_blurred_image.jpg', blurred_image)  # 保存模糊图像
    print("高斯模糊图像已保存。")

    # 锐化
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)  # 确保值在0-255之间
    cv2.imwrite(f'../img/3.11/{image_name}_sharpened_image.jpg', sharpened_image)  # 保存锐化图像
    print("锐化图像已保存。")

    # 中值滤波去噪
    denoised_image = cv2.medianBlur(image, 5)
    cv2.imwrite(f'../img/3.11/{image_name}_denoised_image.jpg', denoised_image)  # 保存去噪图像
    print("去噪图像已保存。")

    # 双边滤波
    bilateral_image = cv2.bilateralFilter(image, 9, 75, 75)
    cv2.imwrite(f'../img/3.11/{image_name}_bilateral_image.jpg', bilateral_image)  # 保存双边滤波图像
    print("双边滤波图像已保存。")
else:
    print("图像读取失败，程序终止。")
