from kivymd.app import MDApp
from kivymd.app import Builder
from kivy.core.window import Window
from Generator_Qr import Creat_Qr


class Application(MDApp):
    def build(self):
        Window.minimum_height, Window.minimum_width = 400, 755
        self.theme_cls.theme_style = 'Dark'
        self.__FILE = Builder.load_file('properties.kv')
        self.__ID = self.__FILE.ids
        self.__verify: bool = False
        return self.__FILE

    def copy(self) -> None:
        """Copia o texto do primeiro field para o segundo
        """
        if self.__ID.first_text.text != '':
            self.__ID.rewrite_text.text = self.__ID.first_text.text

    def check_clear(self, *args):
        """Pega o valor da checkbox"""
        self.__value_clear = args[1]

    def check_open_image(self, *args):
        """Pega o valor da checkbox"""
        self.__value_open_image = args[1]

    def __verify_text(self, mode: bool=True):
        """Verifica os textos nos fields

        Args:
            mode (bool, optional): True -> para acionar o erro.
                                   False -> para desfazer o erro.
        """
        if mode:
            self.__ID.first_text.error = self.__ID.rewrite_text.error = True
            self.__ID.first_text.helper_text = self.__ID.rewrite_text.helper_text =\
                'The fields have to be the same and contain something'
        else:
            self.__ID.first_text.error = self.__ID.rewrite_text.error = False
            self.__ID.first_text.helper_text = self.__ID.rewrite_text.helper_text = ''

    def generate(self) -> None:
        """
        Gera o Qr Code e cria o caminho para a imagem na tela
        """
        if self.__ID.rewrite_text.text != '' and self.__ID.rewrite_text.text == self.__ID.first_text.text:
            try:
                if isinstance(self.__value_open_image, bool):
                    if self.__value_open_image is True:
                        self.__verify = True
                    else:
                        self.__verify = False
            except AttributeError:
                pass

            path: str = Creat_Qr(self.__ID.rewrite_text.text, self.__verify)
            self.__ID.img.color = (1, 1, 1, 1)
            self.__ID.img.source = path
            self.__verify_text(False)
        else:
            self.__verify_text()

        try:
            if self.__value_clear:
                self.__ID.rewrite_text.text = self.__ID.first_text.text = ''
        except AttributeError:
            pass


if __name__ == '__main__':
    Application().run()
