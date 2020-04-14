import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('txt'):
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", [file])
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file FROM tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "Text File: {}".format(item[0])
        print(msg)



    
