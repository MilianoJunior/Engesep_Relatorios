from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from libs.applibs.banco_de_dados.db import Db
from libs.uix.components.print import config_print
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class Painel(MDScreen):
    dialog = None
    def __init__(self, **kwargs):
        super(Painel, self).__init__(**kwargs)
        self.object_db = Db()
        self.consulta = self.object_db.consulta()
        self.on()
    def on(self):
        for i in range(1, 20):
            icon = IconLeftWidget(icon="hydro-power")
            self.listItem = ThreeLineIconListItem(text= str(self.consulta.energia_a.values[-i])+" W",
                                              secondary_text= str(self.consulta.id_a.values[-i]),
                                              tertiary_text=self.consulta.criado_em.values[-i].split('.')[0])
            self.listItem.add_widget(icon)
            self.ids.box.add_widget(self.listItem)
            #----------------------------------------------------------------------------------------------------
            icon = IconLeftWidget(icon="hydro-power")
            self.listItem = ThreeLineIconListItem(text=str(self.consulta.energia_b.values[-i])+" W",
                                              secondary_text=str(self.consulta.id_b.values[-i]),
                                              tertiary_text=self.consulta.criado_em.values[-i].split('.')[0])
            self.listItem.add_widget(icon)
            self.ids.box.add_widget(self.listItem)
            #---------------------------------------------------------------------------------------------------
            icon = IconLeftWidget(icon="water")
            self.listItem = ThreeLineIconListItem(text= str(self.consulta.nivel.values[-i]) +" cm",
                                              secondary_text="Nível de Água",
                                              tertiary_text= self.consulta.criado_em.values[-i].split('.')[0])
            self.listItem.add_widget(icon)
            self.ids.box.add_widget(self.listItem)
            #---------------------------------------------------------------------------------------------------------
    def dialog_config(self):
        print('Testando')
        print(self.height)
        if not self.dialog:
            self.dialog = MDDialog(
                title="Configurações para gerar o relatório",
                type="custom",
                content_cls=config_print(),
                buttons=[
                    MDFlatButton(
                        text="Cancelar",
                        on_release=self.dialog_close,
                    ),
                    MDFlatButton(
                        text="Proseguir",
                        on_release=self.impressao,
                    ),
                ],
                size_hint=(0.9, 1.0)
            )
        self.dialog.height = self.height
        self.dialog.open()
    def dialog_close(self,dt):
        print('fechando')
    def impressao(self,dt):
        
        print('imprimindo 1 ')
