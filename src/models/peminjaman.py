class Peminjaman:
    def __init__(self,anggota_id,buku_id,tanggal_pinjam,tanggal_pengembalian):
        self.anggota_id = anggota_id
        self.buku_id = buku_id
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_pengembalian = tanggal_pengembalian
    
    def addTitle(self,title):
        self.title = title