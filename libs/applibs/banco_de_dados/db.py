import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import sqlite3
from datetime import datetime
from pytz import timezone
import random
import pandas as pd

class Db():
    def __init__(self,name='Banco_de_Dados_ENGESEP'):
        self.name = name
    def lista_tables(self):
        con = self.create_connection('usina_db.db')
        cursor = con.cursor()
        query_list = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
        cursor.execute(query_list)
        dados = []
        for linha in cursor.fetchall():
            dados.append(list(linha))
        con.close()
        return dados
    def create_connection(self,name_db):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR,name_db)
        con = sqlite3.connect(db_path)
        return con
    def create_table(self,tabela):
        try:
            con = self.create_connection('usina_db.db')
            cursor = con.cursor()
            query_create = f"CREATE TABLE IF NOT EXISTS {tabela}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,criado_em DATE NOT NULL,ts timestamp)"
            query_reg = "CREATE TABLE IF NOT EXISTS dados_p (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ip_a real,ip_b real,memoria_a text,memoria_b text,nivel_memoria text,id_a text,id_b text,cidade text,usina text,criado_em DATE NOT NULL,ts timestamp)"
            test = cursor.execute(query_create)
            test2 = cursor.execute(query_reg)
            print('tabela criada com sucesso')
        except:
            return 2

    def seeddb(self):
        con = self.create_connection('usina_db.db')
        cursor = con.cursor()
        tabela = 'cgh_seed'
        query_create = f"CREATE TABLE IF NOT EXISTS {tabela}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,criado_em DATE NOT NULL,ts timestamp)"
        cursor.execute(query_create)
        i = 0
        nivel_m = 1000
        dados = []
        alta = 0
        baixa = 0
        z= 7
        aux = 0
        energia1 = 0
        energia2 = 0
        for ano in range(0,3):
            for mes in range(1, 13):
                for dia in range(1, 32):
                    for horas in range(0, 24):
                        aux = 0
                        for minutos in range(0, 4):
                            try:
                                i += 1
                                ip_a = '198.162.10.3'
                                ip_b = '198.162.10.3'
                                anos = 2019 +ano
                                if anos == 2021 and mes >= 6:
                                    break
                                min_date = datetime(anos, mes, dia, horas, aux, 5, 299)
                                id_a = 'UG-01'
                                id_b = 'UG-02'
                                timestamp = datetime.timestamp(min_date)
                                fuso_horario = timezone('America/Sao_Paulo')
                                min_date = min_date.astimezone(fuso_horario)
                                cidade = "Monte Carlo"
                                usina = "CGH Ponte Caida"
                                if random.randrange(0, 10) < z:
                                    nivel_m = nivel_m - random.randrange(0, 2)
                                    alta += 1
                                else:
                                    baixa += 1
                                    nivel_m = nivel_m + random.randrange(0, 2)
                                aux += 15
                                if anos == 2019:
                                    anoss = anos
                                if i%100==0:
                                    anoss= anos
                                    print('dados: ', energia1, energia2,ip_a, ip_b, nivel_m, id_a, id_b, cidade, usina,min_date,timestamp, alta,baixa)
                                if nivel_m > 1400:
                                    z = 6
                                if nivel_m < 600:
                                    z = 3
                                query = f"""insert into {tabela} (energia_a,energia_b,id_a,id_b,nivel, cidade, usina, criado_em, ts) values (?,?,?,?,?,?,?,?,?)"""
                                cursor.execute(query, (energia1,energia2,id_a,id_b,nivel_m,cidade,usina,min_date,timestamp))
                                con.commit()
                                energia1 = energia1 + random.randrange(15, 25)
                                energia2 = energia2 + random.randrange(15, 25)
                            except ValueError:
                                pass
        con.close()
        print("Seed Realizado!")
    def consulta_dados(self):
        con = self.create_connection('usina_db.db')
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM dados_p;""")
        dados = []
        for linha in cursor.fetchall():
            dados.append(list(linha))
        con.close()
        return dados

    def inserir_dados_conexao(self, ip_a,ip_b,reg_a,reg_b,nivel_m, id_a, id_b, cidade, usina):
        con = self.create_connection('usina_db.db')
        cursor = con.cursor()
        data = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        data_hora = data.astimezone(fuso_horario)
        timestamp = datetime.timestamp(data)

        print('        ')
        print('dados: ',ip_a,ip_b,reg_a,reg_b,nivel_m, id_a, id_b, cidade, usina, data_hora,timestamp)
        print('          ')
        cursor.execute("""INSERT INTO dados_p (ip_a,ip_b,memoria_a,memoria_b,nivel_memoria, id_a, id_b, cidade, usina, criado_em, ts)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (ip_a,ip_b,reg_a,reg_b,nivel_m, id_a, id_b, cidade, usina, data_hora,timestamp))
        con.commit()
        con.close()

    def inserir(self,tabela,energia_a,energia_b,id_a,id_b,nivel,cidade,usina):
        try:
            con = self.create_connection('usina_db.db')
            cursor = con.cursor()
            data = datetime.now()
            fuso_horario = timezone('America/Sao_Paulo')
            data_hora = data.astimezone(fuso_horario)
           # data_hora = data_hora.strftime('%d-%m-%Y %H:%M')
            print(data_hora)
            print(type(data_hora))
            timestamp = datetime.timestamp(data)
            query = f"""insert into {tabela} (energia_a,energia_b,id_a,id_b,nivel, cidade, usina, criado_em, ts) values (?,?,?,?,?,?,?,?,?)"""
            print(timestamp)
            print('----')
            print('nome tabela: ',tabela, type(tabela))
            print('energia a: ',energia_a,type(energia_a))
            print('energia b: ', energia_b, type(energia_b))
            print('id a: ',id_a,type(id_a))
            print('id b: ', id_b, type(id_b))
            print('nivel: ',nivel,type(nivel))
            print('cidade: ',cidade,type(cidade))
            print('query: ',query)

            cursor.execute(query, (energia_a,energia_b,id_a,id_b,nivel,cidade,usina,data_hora,timestamp))
            con.commit()
            con.close()
            print('salvo com sucesso',data_hora,timestamp)
            return 1
        except:
            con.close()
            return 0
    def consulta(self):
        con = self.create_connection('usina_db.db')
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        tabelas = self.lista_tables()
        name = ''
        contador = 0
        for tabela in tabelas:
            cursor.execute(f"""SELECT * FROM {tabela[0]};""")
            aux = len(cursor.fetchall())
            if aux > contador:
                name = tabela[0]
                contador = aux
        cursor.execute(f"""SELECT * FROM {name};""")
        row = cursor.fetchone()
        names = row.keys()
        print('chaves:::::',names)
        dados = []

        for linha in cursor.fetchall():
            dados.append(list(linha))
        dados_pd = pd.DataFrame(data=dados,columns=names)
        con.close()
        return dados_pd

    def delete_all(self,name_db):
        con = self.create_connection('usina_db.db')
        cur = con.cursor()
        sql = f"""DELETE FROM {name_db}"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()
        print('delete com sucesso')

# db = Db()
# db.delete_all('cgh_seed')
# db.seeddb()
