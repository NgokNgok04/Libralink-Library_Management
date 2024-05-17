from controller.buku_controller import *
from controller.peminjaman_controller import *
from controller.anggota_controller import *
def test_insert_buku():
    buku_controller = Buku_Controller()

    ### TEST Insert Buku Berhasil ####
    judul_true = "1001 Cara Melelehkan Wanita"
    isbn_true= "0987654321098"
    path_true = "../../assets/book cover/buku_999.png"

    result = buku_controller.insert_buku(judul_true,isbn_true,path_true)
    assert result[0] == "Sukses menambahkan buku"
    assert result[1] == True

    buku_terbaru = buku_controller.get_list_buku()[-1]
    assert buku_terbaru.judul == judul_true
    assert buku_terbaru.isbn == isbn_true
    assert buku_terbaru.path == path_true

    ### RESET DB TO Normal ###
    IDBukuTerbaru = buku_terbaru.buku_id
    buku_controller.delete_buku(IDBukuTerbaru)

    ### TEST Insert Buku dengan Kode Buku != 13 ###
    isbn_kurang_13 = "123456789012"
    isbn_lebih_13 = "1234567890123456"

    result_kurang_13 = buku_controller.insert_buku(judul_true,isbn_kurang_13,path_true)
    result_lebih_13 = buku_controller.insert_buku(judul_true,isbn_lebih_13,path_true)

    assert result_kurang_13[0] == "ISBN harus berupa 13 angka"
    assert result_lebih_13[0] == "ISBN harus berupa 13 angka"
    assert result_kurang_13[1] == False
    assert result_lebih_13[1] == False

    ### TEST Insert Buku dengan Kode Buku ada huruf ###
    isbn_huruf = "12345M6789012"
    result_huruf = buku_controller.insert_buku(judul_true,isbn_huruf,path_true)
    assert result_huruf[0] == "ISBN harus berupa 13 angka"
    assert result_huruf[1] == False

    ### TEST Insert Buku dengan input dengan tidak lengkap ###
    judul_false = ""
    isbn_false = ""
    path_false = ""
    result_judul_false = buku_controller.insert_buku(judul_false,isbn_true,path_true)
    result_isbn_false = buku_controller.insert_buku(judul_true,isbn_false,path_true)
    result_path_false = buku_controller.insert_buku(judul_true,isbn_true,path_false)
    assert result_judul_false[0] == "Harap melengkapi form"
    assert result_isbn_false[0] == "Harap melengkapi form"
    assert result_path_false[0] == "Harap melengkapi form"
    assert result_judul_false[1] == False
    assert result_isbn_false[1] == False
    assert result_path_false[1] == False

def test_edit_buku():
    buku_controller = Buku_Controller()

    ### INSERT BUKU ###
    judul_true = "1001 Cara Melelehkan Janda"
    isbn_true= "5544332211321"
    path_true = "../../assets/book cover/buku_777.png"

    result = buku_controller.insert_buku(judul_true,isbn_true,path_true)
    IDBukuTerbaru = buku_controller.get_list_buku()[-1].buku_id
    
    ### TEST Edit Buku Berhasil ####
    judul_edit = "1001 Cara Melelehkan Hati Janda"
    isbn_edit = "1112223334440"
    path_edit = "../../assets/book cover/buku_7777.png"
    result = buku_controller.edit_buku(judul_edit,isbn_edit,path_edit,IDBukuTerbaru)
    assert result[0] == "Sukses mengedit buku"
    assert result[1] == True

    buku_terbaru = buku_controller.get_list_buku()[-1]
    assert buku_terbaru.judul == judul_edit
    assert buku_terbaru.isbn == isbn_edit
    assert buku_terbaru.path == path_edit

    ### TEST Edit Buku dengan Kode Buku != 13 ###
    isbn_kurang_13 = "123456789012"
    isbn_lebih_13 = "1234567890123456"

    result_kurang_13 = buku_controller.edit_buku(judul_true,isbn_kurang_13,path_true,IDBukuTerbaru)
    result_lebih_13 = buku_controller.edit_buku(judul_true,isbn_lebih_13,path_true,IDBukuTerbaru)

    assert result_kurang_13[0] == "ISBN harus berupa 13 angka"
    assert result_lebih_13[0] == "ISBN harus berupa 13 angka"
    assert result_kurang_13[1] == False
    assert result_lebih_13[1] == False

    ### TEST Edit Buku dengan Kode Buku ada huruf ###
    isbn_huruf = "12345M6789012"
    result_huruf = buku_controller.edit_buku(judul_true,isbn_huruf,path_true,IDBukuTerbaru)
    assert result_huruf[0] == "ISBN harus berupa 13 angka"
    assert result_huruf[1] == False

    ### TEST Edit Buku dengan input dengan tidak lengkap ###
    judul_false = ""
    isbn_false = ""
    path_false = ""
    result_judul_false = buku_controller.edit_buku(judul_false,isbn_true,path_true,IDBukuTerbaru)
    result_isbn_false = buku_controller.edit_buku(judul_true,isbn_false,path_true,IDBukuTerbaru)
    result_path_false = buku_controller.edit_buku(judul_true,isbn_true,path_false,IDBukuTerbaru)
    assert result_judul_false[0] == "Harap melengkapi form"
    assert result_isbn_false[0] == "Harap melengkapi form"
    assert result_path_false[0] == "Harap melengkapi form"
    assert result_judul_false[1] == False
    assert result_isbn_false[1] == False
    assert result_path_false[1] == False

    ### RESET DB TO Normal ###
    IDBukuTerbaru = buku_terbaru.buku_id
    buku_controller.delete_buku(IDBukuTerbaru)

def test_hapus_buku():
    buku_controller = Buku_Controller()
    anggota_controller = Anggota_Controller()
    peminjaman_controller = Peminjaman_Controller()

    ### INSERT BUKU ###
    judul_true = "1001 Cara Melelehkan Pria"
    isbn_true= "1122334455123"
    path_true = "../../assets/book cover/buku_666.png"

    result = buku_controller.insert_buku(judul_true,isbn_true,path_true)
    
    bukuTerbaru = buku_controller.get_list_buku()[-1]
    IDBukuTerbaru = bukuTerbaru.buku_id
    judulBukuTerbaru = bukuTerbaru.judul
    isbnBukuTerbaru = bukuTerbaru.isbn
    pathBukuTerbaru = bukuTerbaru.path

    ### TEST Hapus buku ###
    result = buku_controller.delete_buku(IDBukuTerbaru)
    assert result[0] == "Sukses menghapus buku"
    assert result[1] == True

    bukuTerakhir = buku_controller.get_list_buku()[-1]
    assert bukuTerakhir.buku_id != IDBukuTerbaru
    assert bukuTerakhir.judul != judulBukuTerbaru
    assert bukuTerakhir.isbn != isbnBukuTerbaru
    assert bukuTerakhir.path != pathBukuTerbaru

    ### Insert Anggota ###
    nama = "Dimas"
    email = "dimasunch@gmail.com"
    telephone = "085261138911"
    status = 1
    result = anggota_controller.insert_anggota(nama,email,telephone,status)
    IDAnggotaTerbaru1 = anggota_controller.get_list_anggota()[-1].anggota_id
    
    ### Insert Buku ###
    result = buku_controller.insert_buku(judul_true,isbn_true,path_true)
    IDBukuTerbaru = buku_controller.get_list_buku()[-1].buku_id

    ### Insert Peminjaman ###
    tanggal_pinjam = "2004-04-04"
    tanggal_pengembalian = "2004-04-16"
    result_borrow = peminjaman_controller.insert_peminjaman(IDBukuTerbaru,tanggal_pinjam,tanggal_pengembalian,IDAnggotaTerbaru1)

    ### TEST Hapus buku yang dipinjam ###
    result = buku_controller.delete_buku(IDBukuTerbaru)
    assert result[0] == "Tidak dapat menghapus buku yang sedang dipinjam."
    assert result[1] == False

    ### RESET DB TO Normal ###
    result = peminjaman_controller.delete_peminjaman(IDBukuTerbaru)
    result = buku_controller.delete_buku(IDBukuTerbaru)
    result = anggota_controller.delete_anggota(IDAnggotaTerbaru1)

def test_filter_buku():
    buku_controller = Buku_Controller()

    ### INSERT 3 Buku Berjudul KWOK KWOK KWOK ###
    judul1 = "KWOK KWOK KWOK DONALD"
    judul2 = "KWOK KWOK KWOK GOBER"
    judul3 = "KWOK KWOK KWOK DESI"
    isbn = "1234567890123"
    path = "../../assets/book cover/buku_kwok.png"


    result = buku_controller.insert_buku(judul1,isbn,path)
    result = buku_controller.insert_buku(judul2,isbn,path)
    result = buku_controller.insert_buku(judul3,isbn,path)

    ### TEST Filter Buku Berjudul KWOK KWOK KWOK ###

    buku_berjudul_KWOK = buku_controller.get_filter_list_buku("KWOK KWOK KWOK")
    assert len(buku_berjudul_KWOK) >= 3

    IDBukuTerbaru = buku_controller.get_list_buku()[-1].buku_id
    buku_controller.delete_buku(IDBukuTerbaru)
    buku_berjudul_KWOK = buku_controller.get_filter_list_buku("KWOK KWOK KWOK")
    assert len(buku_berjudul_KWOK) >= 2

    IDBukuTerbaru = buku_controller.get_list_buku()[-1].buku_id
    buku_controller.delete_buku(IDBukuTerbaru)
    buku_berjudul_KWOK = buku_controller.get_filter_list_buku("KWOK KWOK KWOK")
    assert len(buku_berjudul_KWOK) >= 1

    IDBukuTerbaru = buku_controller.get_list_buku()[-1].buku_id
    buku_controller.delete_buku(IDBukuTerbaru)
    buku_berjudul_KWOK = buku_controller.get_filter_list_buku("KWOK KWOK KWOK")
    assert len(buku_berjudul_KWOK) >= 0