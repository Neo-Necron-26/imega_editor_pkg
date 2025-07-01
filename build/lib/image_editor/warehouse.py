from pathlib import Path


class ImageWarehouse:
    """Управление сохранёнными изображениями"""

    def __init__(self, save_dir="saved_images"):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(exist_ok=True)

    def list_saved_images(self):
        """Список всех сохранённых файлов"""
        return list(self.save_dir.glob("*.jpg"))

    def clear_saved_images(self):
        """Очистка папки с сохранениями"""
        for file in self.save_dir.glob("*"):
            file.unlink()
