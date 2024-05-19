from models.peminjaman import *

class test_peminjaman_model:
    def test_peminjaman_model(self):
        IDAnggota = 7
        IDBuku = 6
        tanggal_pinjam = "2004-04-16"
        tanggal_pengembalian = "2024-05-17"
        
        peminjaman = Peminjaman(IDAnggota,IDBuku,tanggal_pinjam,tanggal_pengembalian)

        assert peminjaman.anggota_id == IDAnggota
        assert peminjaman.buku_id == IDBuku
        assert peminjaman.tanggal_pinjam == tanggal_pinjam
        assert peminjaman.tanggal_pengembalian == tanggal_pengembalian