from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from Generator_Qr import Creat_Qr

class MainFrame(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.__FILE = Builder.load_file('properties.kv')
        self.__ID = self.__FILE.ids
        return self.__FILE

    def generate(self):
        path: str = Creat_Qr(self.__ID.rewrite_text.text,0)
        self.__ID.img.source = path

if __name__ == '__main__':
    MainFrame().run()
