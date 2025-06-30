import cv2
import numpy as np


def apply_negative(img):
    """Негатив изображения"""
    return 255 - img


def apply_gaussian_blur(img, kernel_size=5):
    """Размытие по Гауссу"""
    if kernel_size % 2 == 0:
        kernel_size += 1  # Ядро должно быть нечётным
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def draw_red_circle(img, center, radius):
    """Рисование красного круга"""
    return cv2.circle(img.copy(), center, radius, (0, 0, 255), 2)
