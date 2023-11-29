# open the file X
# create a sql database and connect
# interate through the file and find all the emails
# add the email to a data base
import re
import sqlite3

con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter File Name Here: ')
fhand = open(fname)

for lines in fhand:
    if not lines.startswith('From: '):
        continue
    line = lines.split()
    domain = re.findall('@([^ ]*)', line[1])[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?, 1)',(domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

con.commit()

cur.close()


