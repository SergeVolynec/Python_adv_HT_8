""" Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий."""

import os
from os.path import getsize, join
import csv
import json
import pickle


def get_folds_and_files(path: str) -> list:
    """Функция принимает каталог и возвращает все вложенные файлы и папки с их 
        размером, родительской папкой и признаком папка"""

    dir_sizes = dict()
    for root, dirs, files in os.walk(path, topdown=False):
        size = 0
        
        # Обходим и добавляем все файлы в папке и суммируем их размер
        for name in files:
            dir_sizes[join(root, name)] = getsize(join(root, name))
            size += getsize(join(root, name))
            
        # Обходим и добавляем все каталоги в папке и суммируем их размер
        size += sum(dir_sizes[join(root, d)] for d in dirs)
        dir_sizes[root] = size

    # Добавляем в словарь нужные характеристики
    folds_and_files = []
    for path, total_size in dir_sizes.items():
        folds_and_files.append({"name": path, "size": total_size,
                                "parent_name": os.path.dirname(path),
                                "is_dir": os.path.isdir(path)})

    return folds_and_files


if __name__ == '__main__':
    folds_and_files = get_folds_and_files('../fold')

    # Запишем в csv
    with open("folds_and_files.csv", "w", newline="") as file_csv:
        columns = ["name", "size", "parent_name", "is_dir"]
        writer = csv.DictWriter(file_csv, fieldnames=columns)
        writer.writeheader()
        writer.writerows(folds_and_files)

    # Запишем в json
    folds_and_files_json = json.dumps(folds_and_files)
    with open("folds_and_files.json", "w") as file_json:
        file_json.write(folds_and_files_json)

    # Запишем в pickle
    with open('folds_and_files.pickle', 'wb') as f:
        pickle.dump(folds_and_files, f)
