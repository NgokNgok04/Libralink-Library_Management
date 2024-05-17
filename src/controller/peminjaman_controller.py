import sqlite3
from dateutil import parser
from datetime import datetime
from models.peminjaman import *
from controller.buku_controller import *
class Peminjaman_Controller:
    def __init__(self):
        self.conn = sqlite3.connect("libralink.db")
        self.cursor = self.conn.cursor()
        self.buku_controller = Buku_Controller()

    def get_list_peminjaman(self,anggota_id):
        daftar_peminjaman = []
        self.cursor.execute('SELECT * FROM peminjaman WHERE anggota_id = ?',(anggota_id,))
        rows = self.cursor.fetchall()

        for row in rows:
            peminjaman = Peminjaman(*row)
            self.cursor.execute('SELECT judul FROM buku WHERE buku_id = ?',(row[1],))
            title = self.cursor.fetchall()
            peminjaman.addTitle(title)
            daftar_peminjaman.append(peminjaman)

        return daftar_peminjaman

    def insert_peminjaman(self, buku_id, tanggal_pinjam, tanggal_pengembalian, anggota_id)->tuple[str,bool]:
        if buku_id == "":
            message = "ID Buku harus berupa angka"
            return message, False

        isValidIDBuku = self.buku_controller.isIDBukuValid(buku_id)
        isCanBorrow = self.isAnggotaCanBorrow(anggota_id)
        isBukuBorrowed = self.isBukuBorrowed(buku_id)
        isDateValid = self.isDateValid(tanggal_pengembalian,tanggal_pinjam)
        if (isValidIDBuku and isCanBorrow and (not isBukuBorrowed) and isDateValid):
            self.cursor.execute("INSERT INTO peminjaman (anggota_id, buku_id, tanggal_pinjam, tanggal_pengembalian ) VALUES (?,?,?,?)",(anggota_id,buku_id,tanggal_pinjam,tanggal_pengembalian))
            self.conn.commit()
            message = "Tambah Peminjaman Berhasil"
            return message,True
        else:
            if not isValidIDBuku:
                message = "ID Buku tidak ada"
            if not isCanBorrow:
                message = "Anggota sudah melebihi batas maksimal peminjaman"
            if not isBukuBorrowed:
                message = "Buku sedang dipinjam anggota lain"
            if not isDateValid:
                message = "Pastikan tanggal pengembalian setelah tanggal peminjaman"
            
            return message, False
        
    def delete_peminjaman(self,buku_id):
        self.cursor.execute('SELECT anggota_id FROM peminjaman WHERE buku_id = ?', (buku_id,))
        anggotaToShow = self.cursor.fetchall()
        anggotaToShow = anggotaToShow[0][0]
        self.cursor.execute('DELETE FROM peminjaman WHERE buku_id = ?', (buku_id,))
        self.conn.commit()
        return anggotaToShow

    def isBukuBorrowed(self,buku_id):
        self.cursor.execute("SELECT * FROM peminjaman WHERE buku_id = ?", (buku_id,))
        result = self.cursor.fetchone()
        if not result:
            return False
        else:
            return True

    def isAnggotaCanBorrow(self,anggota_id):
        self.cursor.execute('SELECT * FROM peminjaman WHERE anggota_id = ?', (anggota_id,))
        return len(self.cursor.fetchall()) < 3

    def isAnggotaBorrow(self,anggota_id):
        self.cursor.execute("SELECT * FROM peminjaman WHERE anggota_id = ?", (anggota_id,))
        return len(self.cursor.fetchall()) != 0

    def isDateValid(self,date_after,date_before):

        outputTanggal = "%Y-%m-%d"
        date_format = "%Y-%m-%d"

        date_after = datetime.strptime(parser.parse(date_after).strftime(outputTanggal), date_format)
        date_before = datetime.strptime(parser.parse(date_before).strftime(outputTanggal), date_format)
        
        return date_after > date_before


    def __del__(self):
        self.cursor.close()
        self.conn.close()