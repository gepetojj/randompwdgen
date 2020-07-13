# __author__ = Gepetojj #
# coding = utf-8 #

# libs #

import os
import time
import random
import string
import pyperclip
from rich.console import Console
from rich.markdown import Markdown
from alive_progress import alive_bar
from win10toast import ToastNotifier

# -- #

toaster = ToastNotifier()
os.system('color')


def pwd_creation(qnt, possibilities):
    return ''.join(random.choice(possibilities) for x in range(qnt))


def prompt():
    MARKDOWN = """
## Random Password Generator

# Siga estes passos para criar sua senha:

* Escolha a quantidade de caracteres.
* Escolha se aceita caracteres especiais.
* A senha será gerada e copiada automaticamente para sua área de transferência.
    """

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

    qnt = int(console.input("\n\n[blue]Quantidade de caracteres :point_right:  "))
    esp = str(console.input("[blue]Aceita caracteres especiais? (sim/nao) :point_right:  "))

    if qnt > 50:
        console.print("\n[red underline]:x:  A senha não pode ter mais de 50 caracteres. :x:")
        time.sleep(2)
        console.clear()
        prompt()

    elif esp == "sim":
        possibilities = "12345!@" + string.ascii_letters + "#*67890"
        password = pwd_creation(qnt, possibilities)
        pyperclip.copy(password)
        toaster.show_toast("Random Password Generator", "Sua senha foi copiada para a área de transferência!", duration=3)
        console.print("[yellow]\nSua senha aparecerá e sumirá em 4 segundos após aparecer.")
        time.sleep(2)
        with alive_bar(4) as bar:
            for i in range(4):
                time.sleep(1)
                bar()
        console.print(f"[red]\n:point_right:  {password}  :point_left:")
        time.sleep(4)
        console.clear()
        prompt()

    elif esp == "nao":
        possibilities = "67890" + string.ascii_letters + "12345"
        password = pwd_creation(qnt, possibilities)
        pyperclip.copy(password)
        toaster.show_toast("Random Password Generator", "Sua senha foi copiada para a área de transferência!", duration=3)
        console.print("[yellow]\nSua senha aparecerá e sumirá em 4 segundos após aparecer.")
        time.sleep(2)
        with alive_bar(4) as bar:
            for i in range(4):
                time.sleep(1)
                bar()
        console.print(f"[red]\n:point_right:  {password}  :point_left:")
        time.sleep(4)
        console.clear()
        prompt()

    else:
        console.print("\n[red underline]:x:  A resposta deve sem apenas 'sim' ou 'nao'. :x:")
        time.sleep(2)
        console.clear()
        prompt()


if __name__ == "__main__":
    prompt()
