from models.buku import *
def test_buku_model():
    buku_id = 10
    judul = "The Legend Of Rizzler"
    isbn = 1234567890123
    path = "../../assets/book cover/buku_100.png"
    
    buku = Buku(buku_id,judul,isbn,path)

    assert buku.buku_id == 10
    assert buku.judul == judul
    assert buku.isbn == isbn
    assert buku.path == "path"