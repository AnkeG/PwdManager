import sqlite3
from sqlite3 import Error

def connect_db(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print("db connected\n")
		return conn
	except Error as e:
		print(e)

	return conn

def create_table(conn):
	try:
		c = conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS passwords(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			website TEXT NOT NULL,
			username TEXT NOT NULL,
			password BLOB NOT NULL
			);''')
	except Error as e:
		print(e)

def create_entry(conn, entry):
	sql = 'INSERT INTO passwords(website, username, password) VALUES(?, ?, ?)'
	cur = conn.cursor()
	cur.execute(sql, entry)
	conn.commit()
	return cur.lastrowid  #return id

def select_all(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM passwords")

	rows = cur.fetchall()

	#for row in rows:
		#print(row)

	return rows

def select_by_website(conn, web):
	cur = conn.cursor()
	cur.execute('SELECT * FROM passwords WHERE website = ?', (web,))
	rows = cur.fetchall()

	return rows

def select_by_username(conn, username):
	cur = conn.cursor()
	cur.execute('SELECT * FROM passwords WHERE username = ?', (username,))
	rows = cur.fetchall()

	return rows

def update_pwd_by_id(conn, pwd, entry_id):
	sql = 'UPDATE passwords SET password = ? WHERE id = ?'
	cur = conn.cursor()
	cur.execute(sql, (pwd, entry_id))
	conn.commit()

def delete_task(conn, id):
	sql = 'DELETE FROM passwords WHERE id = ?'
	cur = conn.cursor()
	cur.execute(sql, (id,))
	conn.commit()

def select_by_id(conn, id):
	cur = conn.cursor()
	cur.execute('SELECT * FROM passwords WHERE id = ?', (id,))
	rows = cur.fetchall()

	return rows