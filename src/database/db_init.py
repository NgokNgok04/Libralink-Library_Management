import sqlite3
import os
# Connect to the database (or create it if it doesn't exist)
db_folder = os.path.join(os.path.dirname(__file__), '../database')
os.makedirs(db_folder, exist_ok=True)
db_path = os.path.join(db_folder, 'libralink.db')

conn = sqlite3.connect(db_path)

# Create a cursor object
cursor = conn.cursor()
# Execute a SQL command to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS anggota (
        anggota_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        email TEXT DEFAULT NULL,
        telephone TEXT DEFAULT NULL,
        status_anggota INTEGER NOT NULL DEFAULT 1
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS buku (
        buku_id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        isbn TEXT NOT NULL,
        path TEXT DEFAULT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS peminjaman (
        anggota_id INTEGER NOT NULL,
        buku_id INTEGER NOT NULL,
        tanggal_pinjam DATE NOT NULL,
        tanggal_pengembalian DATE NOT NULL,
        PRIMARY KEY (anggota_id, buku_id),
        FOREIGN KEY (anggota_id) REFERENCES anggota (anggota_id),
        FOREIGN KEY (buku_id) REFERENCES buku (buku_id)
    )
''')

anggota_data = [
    ('Jeremiah Gray', 'jeremiahgray8679@gmail.com', '086028857808', 0),
    ('Natasha Carlson', 'natashacarlson9945@gmail.com', '089632107505', 0),
    ('Ashley Boone', 'ashleyboone0449@gmail.com', '081505999037', 0),
    ('Sara Cook', 'saracook9033@gmail.com', '087342753572', 0),
    ('Traci Wagner', 'traciwagner8211@gmail.com', '082554503955', 1),
    ('Jesus Myers', 'jesusmyers9563@gmail.com', '083889265551', 0),
    ('Brenda Taylor', 'brendataylor4128@gmail.com', '084584923294', 0),
    ('Tina Parker', 'tinaparker9189@gmail.com', '088480162036', 0),
    ('Daniel Williams', 'danielwilliams7562@gmail.com', '089549148270', 0),
    ('Melissa Smith', 'melissasmith6430@gmail.com', '080928716278', 1),
    ('Michael Day', 'michaelday4920@gmail.com', '089436829801', 1),
    ('Brittney Turner', 'brittneyturner3575@gmail.com', '080908756714', 0),
    ('Vincent Fuentes', 'vincentfuentes3550@gmail.com', '083604699069', 0),
    ('Courtney Reynolds', 'courtneyreynolds9234@gmail.com', '081365553927', 0),
    ('Cody Harper', 'codyharper2104@gmail.com', '083285754964', 0),
    ('Robert Vasquez', 'robertvasquez2039@gmail.com', '080233759059', 1),
    ('Richard Aguilar', 'richardaguilar4415@gmail.com', '088178999598', 0),
    ('Jeffrey Brown', 'jeffreybrown6018@gmail.com', '082382491928', 1),
    ('Holly Gibson', 'hollygibson8512@gmail.com', '083992806684', 0),
    ('Breanna Robertson', 'breannarobertson8493@gmail.com', '086299305700', 0)
]

buku_data  = [
    ('A Brief History Of Time','9789792292121',"../../assets/book cover/buku_1.png"),
    ('Melangkah','9786020523316',"../../assets/book cover/buku_2.png"),
    ('Ahok Pun Digoyang','SCOOPG108828',"../../assets/book cover/buku_3.png"),
    ('Komik Next G Vol. 499: Kipas Angin Misteri','9786023679621',"../../assets/book cover/buku_4.png"),
    ('Bukan Perawan Maria','9786022918172',"../../assets/book cover/buku_5.png"),
    ('Adolf Hitler (Sang Diktator, Dalang Rasisme dan Aktor Intelektual Holocaust)','9781022215172',"../../assets/book cover/buku_6.png"),
    ('Naruto Volume 61','SCOOPG202905',"../../assets/book cover/buku_7.png"),
    ('Naruto Volume 52','9786020004075',"../../assets/book cover/buku_8.png"),
    ('Doraemon 03','9789792795332',"../../assets/book cover/buku_9.png"),
    ('50 Nasihat Pernikahan','9786238114351',"../../assets/book cover/buku_10.png"),
    ('Si Anak Spesial','9786025734441',"../../assets/book cover/buku_11.png"),
    ('Si Anak Pintar Tere Liye','9786025734502',"../../assets/book cover/buku_12.png"),
    ('Si Anak Kuat Tere Liye','9786025734427',"../../assets/book cover/buku_13.png"),
    ('Si Anak Pemberani Tere Liye','9786025734526',"../../assets/book cover/buku_14.png"),
    ('Si Anak Cahaya Tere Liye','9786025734540',"../../assets/book cover/buku_15.png"),
    ('Si Anak Badai','9786025734939',"../../assets/book cover/buku_16.png"),
    ('Pulang','9786020822129',"../../assets/book cover/buku_17.png"),
    ('Pergi','978683704329',"../../assets/book cover/buku_18.png"),
    ('Sunset & Rosie','9786029474084',"../../assets/book cover/buku_19.png"),
    ('Satan-ku Nggak Gigit, Lho 2','9786020455389',"../../assets/book cover/buku_20.png"),
    ('Stop Jadi Youtuber! Kalau Nggak Tahu Cara Marketingnya','SCOOPG193836',"../../assets/book cover/buku_21.png"),
    ('The Bully Book','SCOOPG78009',"../../assets/book cover/buku_22.png"),
    ('Bully Aja, I Don’t Care!','9786020623856',"../../assets/book cover/buku_23.png"),
    ('JANGAN TAKUT MENIKAH','SCOOPG5487',"../../assets/book cover/buku_24.png"),
    ('Nikah Tanpa Panik: Ternyata Menikah & Bahagia Itu Muda','9786232444539',"../../assets/book cover/buku_25.png"),
    ('Segeralah Menikah!','SCOOPG115777',"../../assets/book cover/buku_26.png"),
    ('Rumah Janda','SCOOPG123534',"../../assets/book cover/buku_27.png"),
    ('Nama Saya Nujood, Usia 10 Dan Janda','9786232200432',"../../assets/book cover/buku_28.png"),
    ('JANDA-JANDA KOSMOPOLITAN','9789792252705',"../../assets/book cover/buku_29.png"),
    ('Bingkisan Cantik untuk Ibu Hamil','9786020401355',"../../assets/book cover/buku_30.png"),
    ('Ternyata Hamil dan Melahirkan Tanpa Rasa Sakit Itu Muda','978673932129',"../../assets/book cover/buku_31.png"),
    ('Buku Kepoin Ganjar: Antiribet, Kerjanya Sat-Set','9786230414305',"../../assets/book cover/buku_32.png"),
    ('Paradoks Koalisi Tanpa Syarat','978618432229',"../../assets/book cover/buku_33.png"),
    ('Melampaui Mimpi Bersama Anies Baswedan @Twitterland','SCOOPG45642',"../../assets/book cover/buku_34.png"),
    ('Journal of Joy', '9786231341143', "../../assets/book cover/buku_35.png"),
    ('Akasha : Monster 02', '9786230311123', "../../assets/book cover/buku_36.png"),
    ('Great at Work', '9786020522715', "../../assets/book cover/buku_37.png"),
    ('Sang Alkemis', '9786020656069', "../../assets/book cover/buku_38.png"),
    ('Blue Lock 07', '9786230036866', "../../assets/book cover/buku_39.png"),
    ('Malioboro at Midnight', '9786022204909', "../../assets/book cover/buku_40.png"),
    ('Namaku Alam', '592302176', "../../assets/book cover/buku_41.png"),
    ('The Dip: Saat Kita Ditantang untuk Bertahan atau Berhenti', '9786230408007', "../../assets/book cover/buku_42.png"),
    ('Level Comic: Aku no Hana-Kembang Jahanam 02', '9786230047985', "../../assets/book cover/buku_43.png"),
    ('The Apothecary Diaries 4', '9786230305856', "../../assets/book cover/buku_44.png"),
    ('English Classics: The Happy Prince and Other Tales', '9786020335636', "../../assets/book cover/buku_45.png"),
    ('Sherlock : The Blind Banker', '9786024282950', "../../assets/book cover/buku_46.png"),
    ('English Classics: Dubliners', '9786020629698', "../../assets/book cover/buku_47.png"),
    ('Minotaur', 'SCOOPG87115', "../../assets/book cover/buku_48.png"),
    ('The Quintessential Quintuplets Vol.08', '9786230022166', "../../assets/book cover/buku_49.png"),
    ('Level Comic: Attack on Titan 30', '9786230026683', "../../assets/book cover/buku_50.png"),
]

# anggota_id, buku_id, pinjam, kembali
peminjaman_data = [
    (11,28,'2021-01-08','2021-10-05'),
    (17,20,'2020-10-26','2022-04-25'),
    (14,3,'2022-04-28','2023-03-04'),
    (9,41,'2023-03-16','2023-08-07'),
    (14,18,'2022-11-12','2023-02-03'),
    (20,35,'2023-08-09','2023-11-25'),
    (10,34,'2022-12-08','2023-09-23'),
    (14,45,'2022-04-08','2023-06-22'),
    (16,8,'2022-02-11','2023-10-21'),
    (13,6,'2022-02-16','2023-01-14'),
    (19,1,'2022-02-16','2023-01-14'),
    (1,16,'2022-01-29','2023-11-11'),
    (15,23,'2020-04-14','2020-07-27'),
    (16,40,'2020-01-11','2023-09-25'),
    (9,42,'2023-02-03','2023-11-07'),
    (1,17,'2021-12-23','2023-04-12'),
    (4,30,'2022-06-12','2023-01-31'),
    (20,19,'2022-05-21','2023-09-10'),
    (3,22,'2020-10-30','2021-04-18'),
    (8,47,'2023-05-10','2023-09-10'),
    (19,4,'2020-04-02','2021-04-20'),
    (1,11,'2020-04-02','2021-04-21'),
    (7,39,'2020-04-02','2021-04-22'),
    (11,26,'2020-04-02','2021-04-23'),
    (13,44,'2020-04-02','2021-04-24'),
    (20,14,'2020-04-02','2021-04-25'),
    (13,13,'2020-04-02','2021-04-25'),
    (7,48,'2020-04-02','2021-04-25'),
    (12,32,'2020-04-02','2021-04-26'),
    (11,27,'2020-04-02','2021-04-26'),
    (19,24,'2020-04-02','2021-04-27'),
    (2,12,'2020-04-02','2021-04-28'),
    (4,9,'2020-04-02','2021-04-27'),
    (5,49,'2020-04-02','2021-04-29'),
    (5,36,'2020-04-02','2021-04-21'),
]
# Insert the data into the table
cursor.executemany('''
INSERT INTO anggota (nama, email, telephone, status_anggota)
VALUES (?, ?, ?, ?)
''', anggota_data)

cursor.executemany('''
INSERT INTO buku (judul, isbn, path)
VALUES (?, ?, ?)
''', buku_data)

cursor.executemany('''
INSERT INTO peminjaman (anggota_id, buku_id, tanggal_pinjam, tanggal_pengembalian)
VALUES (?, ?, ?, ?)
''', peminjaman_data)

# Commit changes
conn.commit()

# Close the connection
conn.close()
