import cv2
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ensure_saves_dir():
    """Создаёт папку saves если её нет"""
    try:
        Path("saves").mkdir(exist_ok=True)
    except Exception as e:
        logger.error(f"Ошибка создания папки saves: {e}")
        raise


def load_image(file_path):
    """Загрузка изображения с проверкой формата"""
    try:
        ensure_saves_dir()
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Файл {file_path} не найден!")

        img = cv2.imread(file_path)
        if img is None:
            raise ValueError(
                "Неподдерживаемый формат изображения (используйте JPG/PNG)"
            )

        return img
    except Exception as e:
        logger.error(f"Ошибка загрузки изображения: {e}")
        raise


def capture_from_webcam():
    """Захват фото с веб-камеры"""
    try:
        ensure_saves_dir()
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Не удалось подключиться к камере!")

        # Даём камере время на инициализацию
        for _ in range(5):
            cap.read()

        ret, frame = cap.read()
        cap.release()

        if not ret:
            raise RuntimeError("Не удалось получить кадр с камеры")

        return frame
    except Exception as e:
        logger.error(f"Ошибка захвата с камеры: {e}")
        raise


def save_image(img, filename="result"):
    """Сохранение в папку saves"""
    try:
        ensure_saves_dir()
        save_path = f"saves/{filename}.jpg"
        if not cv2.imwrite(save_path, img):
            raise RuntimeError("Ошибка сохранения файла")
        return save_path
    except Exception as e:
        logger.error(f"Ошибка сохранения изображения: {e}")
        raise
