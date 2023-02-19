from kivymd.app import MDApp
from kivymd.app import Builder
from kivy.core.window import Window
from Generator_Qr import Creat_Qr


class MainFrame(MDApp):
    def build(self):
        Window.minimum_height, Window.minimum_width = 400, 755
        self.theme_cls.theme_style = 'Dark'
        self.__FILE = Builder.load_file('properties.kv')
        self.__ID = self.__FILE.ids
        self.__verify: bool = False
        return self.__FILE

    def copy(self) -> None:
        if self.__ID.first_text.text != '':
            self.__ID.rewrite_text.text = self.__ID.first_text.text

    def check_clear(self, *args):
        self.__value_clear = args[1]

    def check_open_image(self, *args):
        self.__value_open_image = args[1]
        

    def generate(self) -> None:
        if self.__ID.rewrite_text.text != '':
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
        try:
            if self.__value_clear:
                self.__ID.rewrite_text.text = self.__ID.first_text.text = ''
        except AttributeError:
            pass


if __name__ == '__main__':
    MainFrame().run()
