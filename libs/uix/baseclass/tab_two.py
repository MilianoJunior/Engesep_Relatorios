from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.datatables import MDDataTable
import utils

utils.load_kv("tab_two.kv")


class TabTwo(FloatLayout, MDTabsBase):
    """
    Tab Item Two.
    """
