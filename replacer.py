"""
Программа-страж, наблюдающая за изменением файла.
Как стоик, она безмятежно принимает перемены,
но мудро вносит исправления, когда это необходимо.
Написано в духе Марка Аврелия.
"""

import os
import time

# Эти строки - наши добродетели
OLD_STRING = "заблуждение"  # То, что требует изменения
NEW_STRING = "мудрость"  # Исправленная истина

FILE_PATH = "ook"  # Путь к наблюдаемому файлу


def meditate_on_file():
    """
    Созерцание файла - подобно медитации над рекой Гераклита.
    Мы не можем войти в один файл дважды, ибо при втором входе
    это уже будет другой файл.
    """
    last_modified = 0
    last_size = 0

    while True:
        try:
            # Проверяем существование файла, как стоик проверяет свои впечатления
            if not os.path.exists(FILE_PATH):
                print(f"Файл {FILE_PATH} не существует. Это внешнее - не в нашей власти.")
                time.sleep(5)
                continue

            current_modified = os.path.getmtime(FILE_PATH)
            current_size = os.path.getsize(FILE_PATH)

            # Если обнаружены перемены (а они неизбежны)
            if current_modified != last_modified or current_size != last_size:
                print("Обнаружены изменения в файле. Всё течёт, всё меняется...")

                # Читаем содержимое с невозмутимостью философа
                with open(FILE_PATH, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Если найдено заблуждение, заменяем его мудростью
                if OLD_STRING in content:
                    new_content = content.replace(OLD_STRING, NEW_STRING)

                    # Записываем с бесстрастием мудреца
                    with open(FILE_PATH, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    print(f"Исправлено: '{OLD_STRING}' → '{NEW_STRING}'. "
                          "Добродетель восторжествовала.")
                else:
                    print("Заблуждений не обнаружено. Продолжаем наблюдение.")

                # Обновляем наши знания о файле
                last_modified = current_modified
                last_size = current_size

            # Созерцаем изменения с интервалом, подобно упражнениям в добродетели
            time.sleep(1)

        except Exception as e:
            print(f"Произошло событие вне нашего контроля: {e}. "
                  "Принимаем это с невозмутимостью.")
            time.sleep(5)


if __name__ == "__main__":
    print("Начинаем наблюдение за файлом...")
    print("Помни: ничто не вечно, кроме добродетели.")
    meditate_on_file()
