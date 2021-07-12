'''
 Menu principal,
'''

import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from libs.applibs.banco_de_dados.db import Db

from libs.uix.baseclass.root import Root


# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class Relatorios(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(Relatorios, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Engesep "

        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Root()
        
        
