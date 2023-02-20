"""Criador de Qr Code"""
from os import mkdir
from os.path import dirname, realpath
from webbrowser import open as webopen
from qrcode.main import QRCode


def Creat_Qr(text: str, view: bool) -> str:
    """Cria o Qr Code

    Args:
        text (str): Texto que será inserido do Qr Code
        view (int): 1 -> mostra a imagem na tela
                    0 -> Não mostra a imagem na tela

    Returns:
        str: Caminho do arquivo
    """
    treated_text = text.replace('/', ' ')
    treated_text = treated_text.replace('\\', ' ') + '.png'
    
    qr = QRCode()
    qr.add_data(text)

    if '.png' not in text:
        text = text + '.png'

    FILE: str = dirname(realpath(__file__)) + '\output\\'

    qr_img = qr.make_image()
    try:
        qr_img.save(f'{FILE}{treated_text}')
        if view == 1:
            webopen(FILE+treated_text)  # mostra o Qr code na tela
        return FILE+treated_text
    except FileNotFoundError:
        mkdir('output')
        return Creat_Qr(text, view)
