import sqlite3
import re
from models.anggota import *
class Anggota_Controller:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_list_anggota(self):
        daftar_anggota = []
        self.cursor.execute('SELECT * FROM anggota')
        rows = self.cursor.fetchall()

        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)

        return daftar_anggota

    def insert_anggota(self, nama, email, telepon, status):
        if nama and email and telepon and status is not None:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check email format
                if re.match(r"^08\d{9,11}$", telepon):  # Check telephone pattern

                    self.cursor.execute("INSERT INTO anggota (nama, email, telephone, status_anggota) VALUES (?, ?, ?, ?)", (nama, email, telepon, status))
                    self.conn.commit()

                    return True

        return False

    def edit_anggota(self, nama, email, telepon, status, anggota_id):
        if nama and email and telepon and status is not None:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check email format
                if re.match(r"^08\d{9,11}$", telepon):  # Check telephone pattern
                    self.cursor.execute("UPDATE anggota SET nama = ?, email = ?, telephone = ?, status_anggota = ? WHERE anggota_id = ?", (nama, email, telepon, status, anggota_id))
                    self.conn.commit()
                    return True
        return False
    
    def get_list_filter_anggota(self,search_query):
        self.cursor.execute('SELECT * FROM anggota WHERE nama LIKE ?', ('%' + search_query + '%',))
        rows = self.cursor.fetchall()
        
        daftar_anggota = []
        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)
        
        return daftar_anggota
    
    def delete_anggota(self,anggota_id):
        self.cursor.execute('DELETE FROM anggota WHERE anggota_id = ?', (anggota_id,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()