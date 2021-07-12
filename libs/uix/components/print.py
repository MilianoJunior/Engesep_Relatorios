from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
import datetime
import utils

utils.load_kv("config_print.kv")
 
class Config_print(BoxLayout):
    def __init__(self,object_db,**kwargs,):
        super(Config_print, self).__init__(**kwargs) 
        self.consulta =object_db.consulta()
        print(self.consulta)
        self.config_print = {
            'nome_usina':str(self.consulta.usina.values[-1]),
            'local':str(self.consulta.cidade.values[-1]),
            'dados': 'Todos os dados',
            'periodo': 'Mensal',
            'ug1': True,
            'ug2':True
        }
    def callback_personalizado(self, instance,root, value):
        print(root,value)
        if root == 'Personalizado' and value:
            inicio = self.consulta['criado_em'][0]
            fim = self.consulta['criado_em'][len(self.consulta) - 1]
            inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d %H:%M:%S.%f%z')
            fim = datetime.datetime.strptime(fim, '%Y-%m-%d %H:%M:%S.%f%z')
            if self.config_print['periodo'] == 'Diário':
                date_dialog = MDDatePicker(mode="picker")
            if self.config_print['periodo'] == 'Mensal':
                date_dialog = MDDatePicker(mode="range",
                                       min_date=inicio.date(),
                                       max_date=fim.date(),
                                       )
            if self.config_print['periodo'] == 'Anual':
                print(type(inicio))
                print(type(fim))
                di = inicio.strftime("%m/%d/%Y").split('/')
                df = fim.strftime("%m/%d/%Y").split('/')
                ano_inicio = int(di[2])
                ano_final = int(df[2])
                print(ano_inicio,ano_final,di[0],di[1])
                date_dialog = MDDatePicker(mode="range",
                                       # year = ano_inicio,
                                       month = int(di[0]),
                                       # day = 1,
                                       min_year = ano_inicio,
                                       # max_year = ano_final,
                                       #font_name="C:\\Engesep\\relatorios\\Engesep_Relatorios\\assets\\fonts\\ZenTokyoZoo-Regular.ttf"
                                       )
                date_dialog.transformation_to_dialog_select_year()
            # r = 0
            # for s in dir(date_dialog):
            #     r+= 1
            #     print(r,s)
            #     print(getattr(date_dialog,s))
            #     print('-----')
            date_dialog.bind(on_save=self.on_save)
            date_dialog.open()
        print(self.config_print)
    def on_save(self, instance, value, date_range):
        if value:
            self.config_print.update({'dados': date_range})
        print(self.config_print)
    def callback_select(self, instance,root, value):
        print(root,value)
        print('----------------')
        if root == 'Anual':
            self.config_print.update({'periodo':root})
        if root == 'Diário':
            self.config_print.update({'periodo':root})
        if root == 'Mensal':
            self.config_print.update({'periodo':root})
        if root == 'Todos os Dados':
            self.config_print.update({'dados':'Todos os Dados'})
        if root == 'UG-01':
            self.config_print.update({'ug1':value})
        if root == 'UG-02':
            self.config_print.update({'ug2':value})
        print(self.config_print)
