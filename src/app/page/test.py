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

# Insert the data into the table
cursor.executemany('''
INSERT INTO anggota (nama, email, telephone, status_anggota)
VALUES (?, ?, ?, ?)
''', anggota_data)
# Commit changes
conn.commit()

# Close the connection
conn.close()
