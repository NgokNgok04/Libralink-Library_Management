import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('datarpl.db')

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
    CREATE TABLE IF NOT EXISTS data_peminjaman_buku (
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
    ('Jeremiah Gray', 'jeremiahgray8679@gmail.com', '086028857808', 1),
    ('Natasha Carlson', 'natashacarlson9945@gmail.com', '089632107505', 1),
    ('Ashley Boone', 'ashleyboone0449@gmail.com', '081505999037', 1),
    ('Sara Cook', 'saracook9033@gmail.com', '087342753572', 1),
    ('Traci Wagner', 'traciwagner8211@gmail.com', '082554503955', 1),
    ('Jesus Myers', 'jesusmyers9563@gmail.com', '083889265551', 1),
    ('Brenda Taylor', 'brendataylor4128@gmail.com', '084584923294', 1),
    ('Tina Parker', 'tinaparker9189@gmail.com', '088480162036', 1),
    ('Daniel Williams', 'danielwilliams7562@gmail.com', '089549148270', 1),
    ('Melissa Smith', 'melissasmith6430@gmail.com', '080928716278', 1),
    ('Michael Day', 'michaelday4920@gmail.com', '089436829801', 1),
    ('Brittney Turner', 'brittneyturner3575@gmail.com', '080908756714', 1),
    ('Vincent Fuentes', 'vincentfuentes3550@gmail.com', '083604699069', 1),
    ('Courtney Reynolds', 'courtneyreynolds9234@gmail.com', '081365553927', 1),
    ('Cody Harper', 'codyharper2104@gmail.com', '083285754964', 1),
    ('Robert Vasquez', 'robertvasquez2039@gmail.com', '080233759059', 1),
    ('Richard Aguilar', 'richardaguilar4415@gmail.com', '088178999598', 1),
    ('Jeffrey Brown', 'jeffreybrown6018@gmail.com', '082382491928', 1),
    ('Holly Gibson', 'hollygibson8512@gmail.com', '083992806684', 1),
    ('Breanna Robertson', 'breannarobertson8493@gmail.com', '086299305700', 1)
]

buku_data  = [
    (1,'Moonlight Forest','906516623- 6',"NULL"),
    (2,'Legend Chronicles','010950220- 5',"NULL"),
    (3,'Legend Chronicles','010950220- 5',"NULL"),
    (4,'Legend Chronicles','010950220- 5',"NULL"),
    (5,'Legend Chronicles','010950220- 5',"NULL"),
    (6,'Legend Chronicles','010950220- 5',"NULL"),
    (7,'Legend Chronicles','010950220- 5',"NULL"),
    (8,'Moonlight Legend','243709775- 5',"NULL"),
    (9,'Moonlight Legend','243709775- 5',"NULL"),
    (10,'Moonlight Legend','243709775- 5',"NULL"),
    (11,'Moonlight Legend','243709775- 5',"NULL"),
    (12,'Moonlight Legend','243709775- 5',"NULL"),
    (13,'Moonlight Legend','243709775- 5',"NULL"),
    (14,'Forest Forest','716550905- 9',"NULL"),
    (15,'Forest Forest','716550905- 9',"NULL"),
    (16,'Forest Forest','716550905- 9',"NULL"),
    (17,'Forest Forest','716550905- 9',"NULL"),
    (18,'Forest Forest','716550905- 9',"NULL"),
    (19,'Forest Journey','900262331- 7',"NULL"),
    (20,'Chronicles Legend','670607980- 4',"NULL"),
    (21,'Chronicles Legend','670607980- 4',"NULL"),
    (22,'Chronicles Legend','670607980- 4',"NULL"),
    (23,'Chronicles Legend','670607980- 4',"NULL"),
    (24,'Forest Chronicles','484476832- 1',"NULL"),
    (25,'Forest Chronicles','484476832- 1',"NULL"),
    (26,'Forest Chronicles','484476832- 1',"NULL"),
    (27,'Forest Chronicles','484476832- 1',"NULL"),
    (28,'Moonlight Secret','444181509- 4',"NULL"),
    (29,'Moonlight Secret','444181509- 4',"NULL"),
    (30,'River Forest','281994735- 6',"NULL"),
    (31,'River Forest','281994735- 6',"NULL"),
    (32,'River Forest','281994735- 6',"NULL"),
    (33,'Valley Secret','321601717- 5',"NULL"),
    (34,'Sunset Journey','996097919- 9',"NULL"),
    (35,'Sunset Journey','996097919- 9',"NULL"),
    (36,'Sunset Journey','996097919- 9',"NULL"),
    (37,'Sunset Journey','996097919- 9',"NULL"),
    (38,'Legend Valley','701091022- 8',"NULL"),
    (39,'Legend Valley','701091022- 8',"NULL"),
    (40,'Secret Legend','069814964- 2',"NULL"),
    (41,'Secret Legend','069814964- 2',"NULL"),
]

peminjaman_data = [
    (1,4,'2021-01-08','2021-10-05'),
    (3,26,'2020-10-26','2022-04-25'),
    (4,34,'2022-04-28','2023-03-04'),
    (5,7,'2023-03-16','2023-08-07'),
    (6,35,'2022-11-12','2023-02-03'),
    (8,28,'2023-08-09','2023-11-25'),
    (9,39,'2022-12-08','2023-09-23'),
    (10,8,'2022-04-08','2023-06-22'),
    (10,34,'2022-02-11','2023-10-21'),
    (12,38,'2022-02-16','2023-01-14'),
    (13,30,'2022-01-29','2023-11-11'),
    (13,32,'2020-04-14','2020-07-27'),
    (14,38,'2020-01-11','2023-09-25'),
    (16,15,'2023-02-03','2023-11-07'),
    (17,2,'2021-12-23','2023-04-12'),
    (17,39,'2022-06-12','2023-01-31'),
    (17,41,'2022-05-21','2023-09-10'),
    (18,8,'2020-10-30','2021-04-18'),
    (20,27,'2023-05-10','2023-09-10'),
    (20,30,'2020-04-02','2021-04-20'),
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
INSERT INTO data_peminjaman_buku (anggota_id, buku_id, tanggal_pinjam, tanggal_pengembalian)
VALUES (?, ?, ?, ?)
''', peminjaman_data)

# Commit changes
conn.commit()

# Close the connection
conn.close()
