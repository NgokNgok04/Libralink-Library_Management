import sqlite3
from models.peminjaman import *
class Peminjaman_Controller:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_list_peminjaman(self):
        daftar_peminjaman = []
        self.cursor.execute('SELECT * FROM data_peminjaman_buku')
        rows = self.cursor.fetchall()

        for row in rows:
            peminjaman = peminjaman(*row)
            daftar_peminjaman.append(peminjaman)

        return daftar_peminjaman

    def __del__(self):
        self.cursor.close()
        self.conn.close()