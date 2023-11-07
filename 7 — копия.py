import sqlite3

con = sqlite3.connect('Jokkk.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Jokes(id INTEGER PRIMARY KEY, Joke VARCHAR)')
cur.execute('INSERT INTO Jokes(Joke) VALUES("Не знаю, с кем спит мой мозг, но мысли рождаются идиотские.")')
cur.execute('INSERT INTO Jokes(Joke) VALUES("Я не умела садиться на шпагат до тех пор, пока не сварила ребёнку кисель…")')
cur.execute('INSERT INTO Jokes(Joke) VALUES("Чтобы заполнить пустоту внутри себя, нужно читать книги, а не жрать.")')
cur.execute('INSERT INTO Jokes(Joke) VALUES("Официанта Жору в ресторане шутя называли Георгий—обедоносец.")')


con.commit()

cur.close()
con.close()