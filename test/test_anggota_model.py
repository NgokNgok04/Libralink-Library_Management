from models.anggota import *

class test_anggota_model:
    def test_anggota_model(self):
        IDAnggota = 100
        nama = "Kera Sakti Chan"
        email = "rainbowpowerpuff@gmail.com"
        telephone = "085261138911"
        status = 1

        anggota = Anggota(IDAnggota,nama,email,telephone,status)

        assert anggota.anggota_id == IDAnggota
        assert anggota.nama == nama
        assert anggota.email == email
        assert anggota.telephone == telephone
        assert anggota.status_anggota == status