from values import list_of_directories
from values import backups_path_string

from zipfile import ZipFile
from pathlib import Path
from datetime import date
from sys import argv
import logging


# настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def help_function():
    """
     Выведет пользователю то, как правильно запустить скрипт
    """
    print(f"\nДля вывода текущей конфигурации:\n>> python3 main.py list\n")
    print(f"Для создания одного архива нужно передать ключ:\n>> python3 main.py <key_from_List>\n")
    print(f"Для создания всех архивов указанных в конфигурации выполнять без аргументов:\n>> python3 main.py\n")


def list_function(list_of_directories: dict):
    """
    Выведет пользователю текущую конфигурацию и то какие диретории бэкапятся
    """
    print("В текущей конфигурации следующие директории с папками:")
    for key, value in list_of_directories.items():
        print(f"{key}: {value}")

def get_files(path):
    """
    Возвращает список абсолютных путей всех файлов включая и подпапки
    """
    return [p for p in path.rglob("*") if p.is_file()]  # path.rglob("*") - рекурсивный обход директории


def create_zip_archive(backup_path, archive_name, files):
    """
    Создает zip архив с переданными файлами, на вход получает путь где создать архив, имя самого архива и список файлов
    """
    archive_path = backup_path / archive_name  # создаем полный путь до папки с zip файлом
    with ZipFile(archive_path, "w") as archive:
        for file in files:
            relative_path = file.relative_to(dir_path)      # получаем относительный путь от dir_path
            archive.write(file, arcname=str(relative_path)) # записываем файл в архив с относительным путем


def cleanup_function():
    """
    Функция очистки старых файлов, количество архивов которые должны оставаться задается в конфигурации
    """
    pass  # TODO: нужно очищать тачку от хлама

if __name__ == "__main__":
    backups_path = Path(backups_path_string)  # отформатируем путь до папки с бэкапами под класс pathlib.PosixPath
    backups_path.mkdir(exist_ok=True)         # создаем директорию для бэкапов если ее не существует

    if len(argv) == 2:
        match argv[1]:
            case "help":
                help_function()
            case "list":
                list_function(list_of_directories)
            case _:
                try:
                    key = argv[1]
                    dir_path = list_of_directories[key]

                    today = str(date.today())
                    archive_name = key + "." + today + ".zip"
                    logging.info(f"Создание архива {archive_name}")

                    files = get_files(Path(dir_path))
                    create_zip_archive(backups_path, archive_name, files)
                except Exception as e:
                    logging.error(f"Ошибка при создании архива {archive_name}: ошибка {e}")

                logging.info(f"Архив успешно создан {archive_name} по пути {backups_path}")
    else:
        for key, dir_path in list_of_directories.items():
            try:
                today = str(date.today())
                archive_name = key + "." + today + ".zip"
                logging.info(f"Создание архива {archive_name}")

                files = get_files(Path(dir_path))
                create_zip_archive(backups_path, archive_name, files)
            except Exception as e:
                logging.error(f"Ошибка при создании архива {archive_name}: ошибка {e}")
                continue

            logging.info(f"Архив успешно создан {archive_name} по пути {backups_path}")
