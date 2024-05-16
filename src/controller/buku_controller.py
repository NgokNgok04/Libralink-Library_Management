import sqlite3
from models.buku import *
class Buku_Controller:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_list_anggota(self):
        daftar_buku = []
        self.cursor.execute('SELECT * FROM buku')
        rows = self.cursor.fetchall()

        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)

        return daftar_buku

    def __del__(self):
        self.cursor.close()
        self.conn.close()