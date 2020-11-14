"""
Author: Rômulo do Carmo Sousa
Description: Remove todos os arquivos terminados em '(1)'
Date: 12-11-2020
"""
import re
import os
import time


def repeated_files(files):
    """Retrona uma lista com os arquivos repetidos"""
    repeated = []

    for file in files:
        match = re.findall(r".*\(1\)$", file)

        if match:
            repeated.extend(match)

    return repeated


def remove():
    """Remove os arquivos"""
    repeated = repeated_files(os.listdir())
    length = len(repeated)
    print(f"\033[1;32mArquivos duplicados:\033[1;31m {length}\033[0;0m\033[0;0m\n")

    if not repeated:
        print("\033[1;96mNão existe trabalho aqui =) !!\033[0;0m")
        return

    for file in repeated:
        print(f"\033[1;32mRemovendo o arquivo:\033[0;0m \033[1;31m{file}\033[0;0m")

        time.sleep(0.1)
        os.remove(file)

    print("\n\033[1;96mTudo limpinho =) !!\033[0;0m")


if __name__ == "__main__":
    remove()
