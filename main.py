from threading import Thread
import logging
from pathlib import Path
from shutil import copyfile
import os

root_dir = Path(os.getcwd())
source = root_dir.joinpath('source')
output = root_dir.joinpath('output')

folders = []


def scan_folders(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)

            thread_scan = Thread(target=scan_folders, args=(el,))
            thread_scan.start()
            threads.append(thread_scan)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output.joinpath(ext)
            ext_folder.mkdir(exist_ok=True)
            copyfile(el, ext_folder.joinpath(el.name))


if __name__ == '__main__':
    threads = []
    folders.append(source)

    thread = Thread(target=scan_folders, args=(source,))
    thread.start()
    threads.append(thread)

    [el.join() for el in threads]

    for folder in folders:
        print(folder)
        thread = Thread(target=copy_file, args=(folder,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]
