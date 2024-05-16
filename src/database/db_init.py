import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('libralink.db')

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
    (1,'A Brief History Of Time','9789792292121',"./assets/coverBukuCollection/buku_1.png"),
    (2,'Melangkah','9786020523316',"./assets/coverBukuCollection/buku_2.png"),
    (3,'Ahok Pun Digoyang','SCOOPG108828',"./assets/coverBukuCollection/buku_3.png"),
    (4,'Komik Next G Vol. 499: Kipas Angin Misteri','9786023679621',"./assets/coverBukuCollection/buku_4.png"),
    (5,'Bukan Perawan Maria','9786022918172',"./assets/coverBukuCollection/buku_5.png"),
    (6,'Adolf Hitler (Sang Diktator, Dalang Rasisme dan Aktor Intelektual Holocaust)','9781022215172',"./assets/coverBukuCollection/buku_6.png"),
    (7,'Naruto Volume 61','SCOOPG202905',"./assets/coverBukuCollection/buku_7.png"),
    (8,'Naruto Volume 52','9786020004075',"./assets/coverBukuCollection/buku_8.png"),
    (9,'Doraemon 03','9789792795332',"./assets/coverBukuCollection/buku_9.png"),
    (10,'50 Nasihat Pernikahan','9786238114351',"./assets/coverBukuCollection/buku_10.png"),
    (11,'Si Anak Spesial','9786025734441',"./assets/coverBukuCollection/buku_11.png"),
    (12,'Si Anak Pintar Tere Liye','9786025734502',"./assets/coverBukuCollection/buku_12.png"),
    (13,'Si Anak Kuat Tere Liye','9786025734427',"./assets/coverBukuCollection/buku_13.png"),
    (14,'Si Anak Pemberani Tere Liye','9786025734526',"./assets/coverBukuCollection/buku_14.png"),
    (15,'Si Anak Cahaya Tere Liye','9786025734540',"./assets/coverBukuCollection/buku_15.png"),
    (16,'Si Anak Badai','9786025734939',"./assets/coverBukuCollection/buku_16.png"),
    (17,'Pulang','9786020822129',"./assets/coverBukuCollection/buku_17.png"),
    (18,'Pergi','978683704329',"./assets/coverBukuCollection/buku_18.png"),
    (19,'Sunset & Rosie','9786029474084',"./assets/coverBukuCollection/buku_19.png"),
    (20,'Satan-ku Nggak Gigit, Lho 2','9786020455389',"./assets/coverBukuCollection/buku_20.png"),
    (21,'Stop Jadi Youtuber! Kalau Nggak Tahu Cara Marketingnya','SCOOPG193836',"./assets/coverBukuCollection/buku_21.png"),
    (22,'The Bully Book','SCOOPG78009',"./assets/coverBukuCollection/buku_22.png"),
    (23,'Bully Aja, I Don’t Care!','9786020623856',"./assets/coverBukuCollection/buku_23.png"),
    (24,'JANGAN TAKUT MENIKAH','SCOOPG5487',"./assets/coverBukuCollection/buku_24.png"),
    (25,'Nikah Tanpa Panik: Ternyata Menikah & Bahagia Itu Muda','9786232444539',"./assets/coverBukuCollection/buku_25.png"),
    (26,'Segeralah Menikah!','SCOOPG115777',"./assets/coverBukuCollection/buku_26.png"),
    (27,'Rumah Janda','SCOOPG123534',"./assets/coverBukuCollection/buku_27.png"),
    (28,'Nama Saya Nujood, Usia 10 Dan Janda','9786232200432',"./assets/coverBukuCollection/buku_28.png"),
    (29,'JANDA-JANDA KOSMOPOLITAN','9789792252705',"./assets/coverBukuCollection/buku_29.png"),
    (30,'Bingkisan Cantik untuk Ibu Hamil','9786020401355',"./assets/coverBukuCollection/buku_30.png"),
    (31,'Ternyata Hamil dan Melahirkan Tanpa Rasa Sakit Itu Muda','978673932129',"./assets/coverBukuCollection/buku_31.png"),
    (32,'Buku Kepoin Ganjar: Antiribet, Kerjanya Sat-Set','9786230414305',"./assets/coverBukuCollection/buku_32.png"),
    (33,'Paradoks Koalisi Tanpa Syarat','978618432229',"./assets/coverBukuCollection/buku_33.png"),
    (34,'Melampaui Mimpi Bersama Anies Baswedan @Twitterland','SCOOPG45642',"./assets/coverBukuCollection/buku_34.png"),

]

# anggota_id, buku_id, pinjam, kembali
peminjaman_data = [
    (1,4,'2021-01-08','2021-10-05'),
    (2,26,'2020-10-26','2022-04-25'),
    (3,34,'2022-04-28','2023-03-04'),
    (4,17,'2023-03-16','2023-08-07'),
    (13,13,'2022-11-12','2023-02-03'),
    (7,20,'2023-08-09','2023-11-25'),
    (9,3,'2022-12-08','2023-09-23'),
    (17,5,'2022-04-08','2023-06-22'),
    (19,7,'2022-02-11','2023-10-21'),
    (17,8,'2022-02-16','2023-01-14'),
    (17,12,'2022-02-16','2023-01-14'),
    (13,30,'2022-01-29','2023-11-11'),
    (21,32,'2020-04-14','2020-07-27'),
    (14,11,'2020-01-11','2023-09-25'),
    (8,33,'2023-02-03','2023-11-07'),
    (20,2,'2021-12-23','2023-04-12'),
    (8,23,'2022-06-12','2023-01-31'),
    (1,12,'2022-05-21','2023-09-10'),
    (9,8,'2020-10-30','2021-04-18'),
    (5,14,'2023-05-10','2023-09-10'),
    (6,33,'2020-04-02','2021-04-20'),
]
# Insert the data into the table
cursor.executemany('''
INSERT INTO anggota (nama, email, telephone, status_anggota)
VALUES (?, ?, ?, ?)
''', anggota_data)

cursor.executemany('''
INSERT INTO buku (buku_id, judul, isbn, path)
VALUES (?, ?, ?, ?)
''', buku_data)

cursor.executemany('''
INSERT INTO peminjaman (anggota_id, buku_id, tanggal_pinjam, tanggal_pengembalian)
VALUES (?, ?, ?, ?)
''', peminjaman_data)

# Commit changes
conn.commit()

# Close the connection
conn.close()
