"""
Author: Rômulo do Carmo Sousa
Description: Remove todos os arquivos terminados em '(1)'
Date: 12-11-2020
"""
import os
import re
import time

# Cores ASCII
ciano_claro = "\033[1;96m"
verde = "\033[1;32m"
vermelho = "\033[1;31m"
reset = "\033[0;0m"


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
    print(f"{verde}Arquivos duplicados: {vermelho}{length}{reset}\n")

    if not repeated:
        print(f"{ciano_claro}✔ Não existe trabalho aqui ✨{reset}")
        return

    for file in repeated:
        print(f"{vermelho}✖ {verde}Removendo o arquivo: {vermelho}{file}{reset}")

        time.sleep(0.1)
        os.remove(file)
        print(f"{verde}✔ Arquivo removido!{reset}")

    print(f"{ciano_claro}✔ Tudo limpinho ✨{reset}")


if __name__ == "__main__":
    remove()
