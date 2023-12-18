import argparse
import logging
import re
import shutil
import sys
from pathlib import Path
from threading import Thread, Condition
from queue import Queue

from colorama import init as init_colorama, Fore, Style
from progress.bar import ShadyBar


SORTER_LOGO = """
 .oooooo..o                        .                     
d8P'    `Y8                      .o8                     
Y88bo.       .ooooo.  oooo d8b .o888oo  .ooooo.  oooo d8b
 `"Y8888o.  d88' `88b `888""8P   888   d88' `88b `888""8P
     `"Y88b 888   888  888       888   888ooo888  888    
oo     .d8P 888   888  888       888 . 888    .o  888    
8""88888P'  `Y8bod8P' d888b      "888" `Y8bod8P' d888b   
"""

CYRYLIC = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяёъы'
LATIN = (
    'a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i',
    'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
    'f', 'kh', 'ts', 'ch', 'sh', 'sch', '', 'yu', 'ya', 'yo', '', 'y'
)

TRANS = {}
for c, l in zip(CYRYLIC, LATIN):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

EXTENSIONS = {
    'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'video': ['AVI', 'MP4', 'MOV', 'MKV'],
    'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
    'archives': ['ZIP', 'GZ', 'TAR'],
}
REGISTERED_EXTENSIONS = {
    extension: folder
    for folder, extensions in EXTENSIONS.items()
    for extension in extensions
}

bar = ShadyBar()


def normalize(file_name: str) -> str:
    latin_name = file_name.translate(TRANS)
    parts = latin_name.rsplit('.', 1)
    parts[0] = re.sub(r'\W', '_', parts[0])
    return '.'.join(parts)


def master(path: Path, verbose=False):
    global bar
    dfs_folder(path, verbose)
    logging.info("Completed searching folder")
    with condition:
        bar = ShadyBar('Processing', max=len(folders.queue), suffix='%(percent)d%%')
        condition.notify_all()


def dfs_folder(path: Path, verbose=False) -> None:
    if verbose:
        logging.info(f"Start looking for folder in {path}")
    for el in path.iterdir():
        if el.is_dir():
            folders.put(el)
            dfs_folder(el)
            if verbose:
                logging.info(f"Found folder: {el}")


def copy_file(output: Path, verbose=False) -> None:
    with condition:
        condition.wait()
    while not folders.empty():
        path = folders.get()
        if verbose:
            logging.info(f'Looking for files in {path}')
        bar.next()
        for el in path.iterdir():
            if el.is_file():
                extension = el.suffix[1:].upper()
                if extension in REGISTERED_EXTENSIONS:
                    destination = output / REGISTERED_EXTENSIONS[extension]
                else:
                    destination = output / 'others'
                try:
                    destination.mkdir(exist_ok=True, parents=True)
                    shutil.copyfile(el, destination / normalize(el.name))
                    if verbose:
                        logging.info(f'Copied {el} to  {destination}')
                except OSError as err:
                    logging.error(err)


def prepare():
    init_colorama()
    print(Fore.BLUE + Style.BRIGHT + SORTER_LOGO)
    print(f" {Fore.CYAN}                    Welcome to your sorting app!")


def get_paths() -> tuple:
    """
    --source [-s] default is current folder
    --output [-o] default folder = 'sorted'
    --verbose [-v] default is False
    """

    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", default=".")
    parser.add_argument("--output", "-o", help="Output folder", default="sorted")
    parser.add_argument("--verbose", "-v", help="Verbose mode", action="store_true")

    args = vars(parser.parse_args())
    source = Path(args.get("source"))
    output = Path(args.get("output")).resolve()
    verbose = args.get("verbose")

    while True:
        source_path = Path(source).resolve()
        if not source_path.exists() or not source_path.is_dir():
            source = input(f'\nThere is no such folder "{source}"\n'
                           f'Please enter the path to the existing folder\n'
                           f'(enter nothing to sort current folder): {Fore.WHITE}')
        else:
            confirmation = input(
                f'\n{Fore.GREEN}Do You really want to sort {"this" if source else "current"} folder:\n"{source_path}"?\n'
                f'{Fore.GREEN}type {Fore.WHITE}y / n {Fore.GREEN} or enter another path: {Fore.WHITE}')
            if confirmation.lower() == 'n':
                return tuple()
            if confirmation.lower() == 'y':
                break
            source = confirmation

    return source_path, output, verbose


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    prepare()

    try:
        source, output, verbose = get_paths()
    except ValueError as err:
        logging.error(err)
        sys.exit(1)

    logging.info(f'\nStart in folder "{source}"')

    condition = Condition()
    folders = Queue()
    folders.put(source)

    master_thread = Thread(target=master, args=(source, verbose))
    master_thread.start()

    threads = []
    for i in range(5):
        th = Thread(target=copy_file, args=(output, verbose))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    logging.info(f"\nCompleted copying files to '{output}'.\n You can remove unsorted files.")
