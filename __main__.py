import cv2
import time
import sys
import os
from image_editor import *

# Фикс для Wayland на Linux
if "WAYLAND_DISPLAY" in os.environ:
    os.environ["QT_QPA_PLATFORM"] = "xcb"


def show_image(img, title="Image", delay=3000):
    """Показывает изображение с гарантированным временем"""
    try:
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        cv2.imshow(title, img)
        start_time = time.time()

        while True:
            if cv2.waitKey(100) >= 0 or (time.time() - start_time) * 1000 > delay:
                break

        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Ошибка отображения изображения: {e}")


def process_image_menu(original_img):
    """Меню обработки изображения"""
    current_img = original_img.copy()  # Рабочая копия изображения

    while True:
        try:
            print("\n=== МЕНЮ ОБРАБОТКИ ===")
            print("1. Применить негатив")
            print("2. Размыть по Гауссу")
            print("3. Нарисовать красный круг")
            print("4. Сохранить текущее изображение и выйти")
            print("5. Выйти без сохранения")

            choice = input("Выберите действие (1-5): ").strip()

            if choice == "1":
                current_img = apply_negative(current_img)
                show_image(current_img, "Негатив")
            elif choice == "2":
                try:
                    size = int(
                        input("Введите размер ядра (нечётное число, например 5): ")
                    )
                    if size % 2 == 0:
                        size += 1
                    current_img = apply_gaussian_blur(current_img, size)
                    show_image(current_img, "Размытие")
                except ValueError:
                    print("Ошибка: введите целое число!")
            elif choice == "3":
                try:
                    x = int(input("X координата центра: "))
                    y = int(input("Y координата центра: "))
                    radius = int(input("Радиус круга: "))
                    current_img = draw_red_circle(current_img, (x, y), radius)
                    show_image(current_img, "С кругом")
                except ValueError:
                    print("Ошибка: введите целые числа для координат!")
            elif choice == "4":
                filename = (
                    input("Введите имя файла (без расширения): ").strip() or "result"
                )
                try:
                    path = save_image(current_img, filename)
                    print(f"Изображение успешно сохранено в: {path}")
                    return True
                except Exception as e:
                    print(f"Ошибка сохранения: {e}")
            elif choice == "5":
                return False
            else:
                print("Неверный ввод! Попробуйте снова.")
        except KeyboardInterrupt:
            print("\nПрервано пользователем")
            return False
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


def main():
    print("=== IMAGE EDITOR (Вариант 5) ===")
    print("Для выхода в любой момент нажмите Ctrl+C\n")

    while True:
        try:
            print("\n=== ГЛАВНОЕ МЕНЮ ===")
            print("1. Загрузить изображение")
            print("2. Сделать фото с камеры")
            print("3. Выход")

            choice = input("Выберите действие (1-3): ").strip()

            if choice == "1":
                try:
                    path = input("Введите путь к изображению: ").strip()
                    if not path:
                        print("Ошибка: путь не может быть пустым!")
                        continue

                    img = load_image(path)
                    show_image(img, "Исходное изображение", 2000)
                    process_image_menu(img)
                except Exception as e:
                    print(f"Ошибка: {e}")
            elif choice == "2":
                try:
                    print("\nПодготовка камеры... Улыбнитесь!")
                    for i in range(3, 0, -1):
                        print(f"Снимок через {i}...")
                        time.sleep(1)

                    img = capture_from_webcam()
                    show_image(img, "Фото с камеры", 2000)
                    process_image_menu(img)
                except Exception as e:
                    print(f"Ошибка: {e}")
            elif choice == "3":
                print("Выход из программы...")
                break
            else:
                print("Неверный ввод! Попробуйте снова.")
        except KeyboardInterrupt:
            print("\nПрограмма завершена")
            break
        except Exception as e:
            print(f"Критическая ошибка: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
