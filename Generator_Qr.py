"""Criador de Qr Code"""
from os import mkdir
from os.path import dirname, realpath
from webbrowser import open
from qrcode.main import QRCode


def Creat_Qr(text: str, view: int) -> None:
    """Cria o Qr Code

    Args:
        text (str): Texto que será inserido do Qr Code
        check (int): 1 -> mostra a imagem na tela
    """
    qr = QRCode()
    qr.add_data(text)

    text: str = text + '.png'
    FILE: str = dirname(realpath(__file__)) + '\output\\'

    qr_img = qr.make_image()
    try:
        qr_img.save(f'{FILE}{text}')
        if view == 1:
            open(FILE+text)  # mostra o Qr code na tela
    except FileNotFoundError:
        mkdir('output')
        Creat_Qr(text)


if __name__ == '__main__':
    Creat_Qr('Test', 1)
