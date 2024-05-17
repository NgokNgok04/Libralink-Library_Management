from controller.anggota_controller import *
from controller.buku_controller import *
from controller.peminjaman_controller import *

def test_insert_anggota():
    anggota_controller = Anggota_Controller()
    
    ### TEST Insert Anggota Berhasil ###
    nama_true = "SIR KING MATTHEW XII"
    email_true = "vladimirmatthew791@gmail.com"
    telepon_true = "085261138911"
    status_aktif = 1
    status_nonaktif = 0

    result = anggota_controller.insert_anggota(nama_true,email_true,telepon_true,status_aktif)
    assert result[0] == "Sukses menambahkan anggota"
    assert result[1] == True

    anggota_terbaru = anggota_controller.get_list_anggota()[-1]
    assert anggota_terbaru.nama == nama_true
    assert anggota_terbaru.email == email_true
    assert anggota_terbaru.telephone == telepon_true
    assert anggota_terbaru.status_anggota == status_aktif

    ### RESET DB TO Normal ###
    IDAnggotaTerbaru = anggota_terbaru.anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)

    ### TEST Insert Anggota dengan Telepon Tidak Berformat 08 atau Berpanjang 11 - 13 Digit ###
    telepon_not08 = "625261138911"
    telepon_kurang_11 = "0834567890"
    telepon_lebih_13 = "083456789012345"
    
    result_not08 = anggota_controller.insert_anggota(nama_true,email_true,telepon_not08,status_aktif)
    result_kurang_11 = anggota_controller.insert_anggota(nama_true,email_true,telepon_kurang_11,status_nonaktif)
    result_lebih_13 = anggota_controller.insert_anggota(nama_true,email_true,telepon_lebih_13,status_nonaktif)

    assert result_not08[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_kurang_11[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_lebih_13[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_not08[1] == False
    assert result_kurang_11[1] == False
    assert result_lebih_13[1] == False

    ### TEST Insert Anggota dengan Email Tidak Berformat %@%.% ###
    email_false1 = "@gmail.com"
    email_false2 = "vladimirmatthew791@.com"
    email_false3 = "vladimirmatthew791@gmail."
    
    result_false1 = anggota_controller.insert_anggota(nama_true,email_false1,telepon_true,status_aktif)
    result_false2 = anggota_controller.insert_anggota(nama_true,email_false2,telepon_true,status_aktif)
    result_false3 = anggota_controller.insert_anggota(nama_true,email_false3,telepon_true,status_aktif)

    assert result_false1[0] == "Format email harus berupa %@%.%"
    assert result_false2[0] == "Format email harus berupa %@%.%"
    assert result_false3[0] == "Format email harus berupa %@%.%"
    assert result_false1[1] == False
    assert result_false2[1] == False
    assert result_false3[1] == False

    ### TEST Insert Anggota dengan input yang tidak lengkap ###
    nama_false = ""
    email_false = ""
    telepon_false = ""

    result_false = anggota_controller.insert_anggota(nama_false,email_false,telepon_false,status_aktif)

    assert result_false[0] == "Harap melengkapi form"
    assert result_false[1] == False

def test_edit_anggota():
    anggota_controller = Anggota_Controller()

    ### INSERT ANGGOTA ###
    nama_true = "SIR KING MATTHEW XII"
    email_true = "vladimirmatthew791@gmail.com"
    telepon_true = "085261138911"
    status_aktif = 1
    status_nonaktif = 0

    result = anggota_controller.insert_anggota(nama_true,email_true,telepon_true,status_aktif)
    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id

    ### TEST Edit Anggota Berhasil ###
    nama_edit = "RAJA IBLIS MATTHEW XII"
    email_edit = "matthewvladimir791@gmail.com"
    telepon_edit = "081397683438"

    result = anggota_controller.edit_anggota(nama_edit,email_edit,telepon_edit,status_nonaktif,IDAnggotaTerbaru)
    assert result[0] == "Sukses mengedit anggota"
    assert result[1] == True

    anggota_terbaru = anggota_controller.get_list_anggota()[-1]
    assert anggota_terbaru.nama == nama_edit
    assert anggota_terbaru.email == email_edit
    assert anggota_terbaru.telephone == telepon_edit
    assert anggota_terbaru.status_anggota == status_nonaktif

    ### TEST Edit Anggota dengan Telepon Tidak Berformat 08 atau Berpanjang 11 - 13 Digit ###
    telepon_not08 = "625261138911"
    telepon_kurang_11 = "0834567890"
    telepon_lebih_13 = "083456789012345"

    result_not08 = anggota_controller.edit_anggota(nama_true,email_true,telepon_not08,status_aktif,IDAnggotaTerbaru)
    result_kurang_11 = anggota_controller.edit_anggota(nama_true,email_true,telepon_kurang_11,status_nonaktif,IDAnggotaTerbaru)
    result_lebih_13 = anggota_controller.edit_anggota(nama_true,email_true,telepon_lebih_13,status_nonaktif,IDAnggotaTerbaru)

    assert result_not08[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_kurang_11[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_lebih_13[0] == "Nomor telepon haris diawali '08' dan memiliki 11 - 13 digit"
    assert result_not08[1] == False
    assert result_kurang_11[1] == False
    assert result_lebih_13[1] == False

    ### TEST Edit Anggota dengan Email Tidak Berformat %@%.% ###
    email_false1 = "@gmail.com"
    email_false2 = "vladimirmatthew791@.com"
    email_false3 = "vladimirmatthew791@gmail."
    
    result_false1 = anggota_controller.edit_anggota(nama_true,email_false1,telepon_true,status_aktif,IDAnggotaTerbaru)
    result_false2 = anggota_controller.edit_anggota(nama_true,email_false2,telepon_true,status_aktif,IDAnggotaTerbaru)
    result_false3 = anggota_controller.edit_anggota(nama_true,email_false3,telepon_true,status_aktif,IDAnggotaTerbaru)

    assert result_false1[0] == "Format email harus berupa %@%.%"
    assert result_false2[0] == "Format email harus berupa %@%.%"
    assert result_false3[0] == "Format email harus berupa %@%.%"
    assert result_false1[1] == False
    assert result_false2[1] == False
    assert result_false3[1] == False

    ### TEST Edit Anggota dengan input yang tidak lengkap ###
    nama_false = ""
    email_false = ""
    telepon_false = ""

    result_false = anggota_controller.edit_anggota(nama_false,email_false,telepon_false,status_aktif,IDAnggotaTerbaru)

    assert result_false[0] == "Harap melengkapi form"
    assert result_false[1] == False

    ### RESET DB TO Normal ###
    IDAnggotaTerbaru = anggota_terbaru.anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)

def test_hapus_anggota():
    anggota_controller = Anggota_Controller()
    buku_controller = Buku_Controller()
    peminjaman_controller = Peminjaman_Controller()
    ### INSERT ANGGOTA ###
    nama_true = "PRESIDENT MATTHEW XXX"
    email_true = "mrpresident791@gmail.com"
    telepon_true = "085234836111"
    status_aktif = 1

    result = anggota_controller.insert_anggota(nama_true,email_true,telepon_true,status_aktif)
    anggotaTerbaru = anggota_controller.get_list_anggota()[-1]
    IDAnggotaTerbaru = anggotaTerbaru.anggota_id
    emailAnggotaTerbaru = anggotaTerbaru.email
    teleponAnggotaTerbaru = anggotaTerbaru.telephone
    statusAnggotaTerbaru = anggotaTerbaru.status_anggota

    ### TEST Hapus Anggota ###
    result = anggota_controller.delete_anggota(IDAnggotaTerbaru)
    assert result[0] == "Sukses menghapus anggota"
    assert result[1] == True

    anggotaTerakhir = anggota_controller.get_list_anggota()[-1]
    assert anggotaTerakhir.anggota_id != IDAnggotaTerbaru
    assert anggotaTerakhir.email != emailAnggotaTerbaru
    assert anggotaTerakhir.telephone != teleponAnggotaTerbaru
    assert (anggotaTerakhir.status_anggota == statusAnggotaTerbaru) or (anggotaTerakhir.status_anggota == (not statusAnggotaTerbaru))

    ### INSERT Anggota ###
    result = anggota_controller.insert_anggota(nama_true,email_true,telepon_true,status_aktif)
    IDAnggotaTerakhir = anggota_controller.get_list_anggota()[-1].anggota_id

    ### INSERT Buku ###
    judul = "HOW TO EAT BABY"
    isbn = "1234567890123"
    path = "../../assets/book cover/buku_121.png"
    result = buku_controller.insert_buku(judul,isbn,path)
    IDBukuTerakhir = buku_controller.get_list_buku()[-1].buku_id

    ### INSERT Peminjaman ###
    tanggal_pinjam = "2022-04-04"
    tanggal_pengembalian = "2022-04-16"
    result_borrow = peminjaman_controller.insert_peminjaman(IDBukuTerakhir,tanggal_pinjam,tanggal_pengembalian,IDAnggotaTerakhir)
    
    ### TEST Hapus Anggota ###
    result = anggota_controller.delete_anggota(IDAnggotaTerakhir)
    assert result[0] == "Tidak dapat menghapus anggota yang memiliki peminjaman buku."
    assert result[1] == False

    ### RESET DB TO Normal ###
    peminjaman_controller.delete_peminjaman(IDBukuTerakhir)
    buku_controller.delete_buku(IDBukuTerakhir)
    anggota_controller.delete_anggota(IDAnggotaTerakhir)
    

def test_filter_anggota():
    anggota_controller = Anggota_Controller()

    ### INSERT 5 Anggota Berawalan PETANI HEBAT
    nama1 = "PETANI HEBAT MATTHEW"
    nama2 = "PETANI HEBAT DANIEL"
    nama3 = "PETANI HEBAT KIEL"
    nama4 = "PETANI HEBAT AISYAH"
    nama5 = "PETANI HEBAT RAFI"
    email = "mrpetanihebat@mantap.com"
    telephone = "081122334455"

    result = anggota_controller.insert_anggota(nama1,email,telephone,1)
    result = anggota_controller.insert_anggota(nama2,email,telephone,1)
    result = anggota_controller.insert_anggota(nama3,email,telephone,0)
    result = anggota_controller.insert_anggota(nama4,email,telephone,0)
    result = anggota_controller.insert_anggota(nama5,email,telephone,1)
    
    ### TEST Filter Anggota Berawalan PETANI HEBAT
    
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 5

    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 4
    
    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 3
    
    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 2
    
    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 1
    
    IDAnggotaTerbaru = anggota_controller.get_list_anggota()[-1].anggota_id
    anggota_controller.delete_anggota(IDAnggotaTerbaru)
    anggota_bernama_PETANIHEBAT = anggota_controller.get_list_filter_anggota("PETANI HEBAT")
    assert len(anggota_bernama_PETANIHEBAT) >= 0