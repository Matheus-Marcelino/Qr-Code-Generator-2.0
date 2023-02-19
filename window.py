from kivymd.app import MDApp
from kivymd.app import Builder

class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.__FILE = Builder.load_file('properties.kv')
        return self.__FILE
