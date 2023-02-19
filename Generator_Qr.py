"""Criador de Qr Code"""
from os import mkdir
from os.path import dirname, realpath
from webbrowser import open as webopen
from qrcode.main import QRCode


def Creat_Qr(text: str, view: int) -> str:
    """Cria o Qr Code

    Args:
        text (str): Texto que será inserido do Qr Code
        view (int): 1 -> mostra a imagem na tela
                    0 -> Não mostra a imagem na tela
    """
    qr = QRCode()
    qr.add_data(text)

    text: str = text + '.png'
    FILE: str = dirname(realpath(__file__)) + '\output\\'

    qr_img = qr.make_image()
    try:
        qr_img.save(f'{FILE}{text}')
        if view == 1:
            webopen(FILE+text)  # mostra o Qr code na tela
        return FILE
    except FileNotFoundError:
        mkdir('output')
        Creat_Qr(text, view)


if __name__ == '__main__':
    Creat_Qr('Test', 1)
