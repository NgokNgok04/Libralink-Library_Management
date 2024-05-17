from controller.peminjaman_controller import Peminjaman_Controller
from controller.anggota_controller import *
from controller.buku_controller import *
def test_insert_peminjaman():
    anggota_controller = Anggota_Controller()
    buku_controller = Buku_Controller()
    peminjaman_controller = Peminjaman_Controller()

    ### INSERT Buku 1 ###
    judul = "1001 Cara Melelehkan Wanita"
    isbn = "0987654321098"
    path = "../../assets/book cover/buku_585.png"

    result = buku_controller.insert_buku(judul,isbn,path)

    ### Insert Anggota ###
    nama = "SIR KING MATTHEW XII"
    email = "vladimirmatthew791@gmail.com"
    telepon = "085261138911"
    status = 1

    result = anggota_controller.insert_anggota(nama,email,telepon,status)

    ### TEST Insert Peminjaman Berhasil ###
    IDAnggota_true = anggota_controller.get_list_anggota()[-1].anggota_id
    IDBuku_true = buku_controller.get_list_buku()[-1].buku_id
    tanggal_pinjam_true = "2004-04-16"
    tanggal_pengembalian_true = "2004-05-11"

    result = peminjaman_controller.insert_peminjaman(IDBuku_true, tanggal_pinjam_true, tanggal_pengembalian_true,IDAnggota_true)
    assert result[0] == "Tambah Peminjaman Berhasil"
    assert result[1] == True

    peminjaman_terbaru = peminjaman_controller.get_list_peminjaman(IDAnggota_true)[-1]
    assert peminjaman_terbaru.anggota_id == IDAnggota_true
    assert peminjaman_terbaru.buku_id == IDBuku_true
    assert peminjaman_terbaru.tanggal_pinjam == tanggal_pinjam_true
    assert peminjaman_terbaru.tanggal_pengembalian == tanggal_pengembalian_true

    ### TEST Insert Peminjaman dengan ID Buku Bukan Angka atau Tidak Ada ###
    IDBuku_notAngka = "0A"
    IDBuku_notValid = 343

    result_notAngka = peminjaman_controller.insert_peminjaman(IDBuku_notAngka,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_true)
    result_notValid = peminjaman_controller.insert_peminjaman(IDBuku_notValid,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_true)

    assert result_notAngka[0] == "ID Buku harus berupa angka"
    assert result_notValid[0] == "ID Buku tidak ada pada daftar buku"
    assert result_notAngka[1] == False
    assert result_notValid[1] == False

    ### Insert Buku 2 ###
    result = buku_controller.insert_buku(judul,isbn,path)
    IDBuku2 = buku_controller.get_list_buku()[-1].buku_id

    ### Insert Buku 3 ###
    result = buku_controller.insert_buku(judul,isbn,path)
    IDBuku3 = buku_controller.get_list_buku()[-1].buku_id
    ### Insert Buku 4 ###
    result = buku_controller.insert_buku(judul,isbn,path)
    IDBuku4 = buku_controller.get_list_buku()[-1].buku_id
    
    ### TEST Insert Peminjaman dengan Anggota Mencapai Batas Peminjaman ###
    result_borrow = peminjaman_controller.insert_peminjaman(IDBuku2,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_true)
    assert result_borrow[0] == "Tambah Peminjaman Berhasil"
    assert result_borrow[1] == True

    result_borrow = peminjaman_controller.insert_peminjaman(IDBuku3,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_true)
    assert result_borrow[0] == "Tambah Peminjaman Berhasil"
    assert result_borrow[1] == True

    result_borrow = peminjaman_controller.insert_peminjaman(IDBuku4,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_true)
    assert result_borrow[0] == "Anggota sudah melebihi batas maksimal peminjaman"
    assert result_borrow[1] == False

    ### TEST Insert Peminjaman dengan Buku sudah dipinjam orang lain ###
    result = anggota_controller.insert_anggota(nama,email,telepon,status)
    IDAnggota_wantToBorrowBorrowedBook = anggota_controller.get_list_anggota()[-1].anggota_id
    result_borrow = peminjaman_controller.insert_peminjaman(IDBuku2,tanggal_pinjam_true,tanggal_pengembalian_true,IDAnggota_wantToBorrowBorrowedBook)
    assert result_borrow[0] == "Buku sedang dipinjam anggota lain"
    assert result_borrow[1] == False

    ### TEST Insert Peminjaman dengan Tanggal Pengembalian sebelum Tanggal Pinjam ###
    tanggal_pengembalian_false = "2004-04-04"
    result_borrow = peminjaman_controller.insert_peminjaman(IDBuku4,tanggal_pinjam_true,tanggal_pengembalian_false,IDAnggota_wantToBorrowBorrowedBook)
    assert result_borrow[0] == "Pastikan tanggal pengembalian setelah tanggal peminjaman"
    assert result_borrow[1] == False

    ### RESET DB TO Normal ###
    peminjaman_controller.delete_peminjaman(IDBuku3)
    peminjaman_controller.delete_peminjaman(IDBuku2)
    peminjaman_controller.delete_peminjaman(IDBuku_true)

    anggota_controller.delete_anggota(IDAnggota_wantToBorrowBorrowedBook)
    anggota_controller.delete_anggota(IDAnggota_true)

    buku_controller.delete_buku(IDBuku4)
    buku_controller.delete_buku(IDBuku3)
    buku_controller.delete_buku(IDBuku2)
    buku_controller.delete_buku(IDBuku_true)

def test_delete_peminjaman():
    anggota_controller = Anggota_Controller()
    buku_controller = Buku_Controller()
    peminjaman_controller = Peminjaman_Controller()

    ### INSERT Buku 1 ###
    judul = "1001 Cara Melelehkan Wanita"
    isbn = "0987654321098"
    path = "../../assets/book cover/buku_585.png"

    result = buku_controller.insert_buku(judul,isbn,path)

    ### Insert Anggota ###
    nama = "SIR KING MATTHEW XII"
    email = "vladimirmatthew791@gmail.com"
    telepon = "085261138911"
    status = 1

    result = anggota_controller.insert_anggota(nama,email,telepon,status)

    ### Insert Peminjaman ###
    IDAnggota_true = anggota_controller.get_list_anggota()[-1].anggota_id
    IDBuku_true = buku_controller.get_list_buku()[-1].buku_id
    tanggal_pinjam_true = "2004-04-16"
    tanggal_pengembalian_true = "2004-05-11"

    result = peminjaman_controller.insert_peminjaman(IDBuku_true, tanggal_pinjam_true, tanggal_pengembalian_true,IDAnggota_true)
    
    peminjaman_controller.delete_peminjaman(IDBuku_true)    