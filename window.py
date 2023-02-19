from kivymd.app import MDApp
from kivymd.app import Builder
from Generator_Qr import Creat_Qr


class MainFrame(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.__FILE = Builder.load_file('properties.kv')
        self.__ID = self.__FILE.ids
        return self.__FILE

    def generate(self) -> None:
        if self.__ID.rewrite_text.text != '':
            path: str = Creat_Qr(self.__ID.rewrite_text.text,0)
            self.__ID.img.color = (1, 1, 1, 1)
            self.__ID.img.source = path

    def copy(self) -> None:
        self.__ID.rewrite_text.text = self.__ID.first_text.text


if __name__ == '__main__':
    MainFrame().run()
