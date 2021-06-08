"""
HotReloader
-----------
Uses kaki module for Hot Reload (limited to some uses cases).
Before using, install kaki by `pip install kaki`

"""


import os
import platform
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

from kaki.app import App as HotReloaderApp  # NOQA: E402
from kivy.logger import LOG_LEVELS, Logger  # NOQA: E402

Logger.setLevel(LOG_LEVELS["debug"])

from kivy.core.window import Window  # NOQA: E402
from kivymd.app import MDApp  # NOQA: E402

from libs.uix.baseclass.root import Root  # NOQA: E402

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

KV_FOLDER = os.path.join(os.getcwd(), "libs", "uix", "kv")


class Relatorios(MDApp, HotReloaderApp):  # NOQA: N801
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    CLASSES = {'Root': 'libs.uix.baseclass.root', 
               'HomeScreen': 'libs.uix.baseclass.home_screen', 
               'TabOne': 'libs.uix.baseclass.tab_one', 
               'TabTwo': 'libs.uix.baseclass.tab_two', 
               'TabThree': 'libs.uix.baseclass.tab_three'}  # NOQA: F821

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(Relatorios, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Engesep "

        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build_app(self):  # build_app works like build method
        return Root()


if __name__ == "__main__":
    Relatorios().run()
