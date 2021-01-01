import db

def welcomemsg():
	print("Welcome to Password Manager")
	MasterPwd = input("Plase enter the Master Password:")

	while MasterPwd != "12345":
		print("Wrong Master Password")
		MasterPwd = input("Plase enter the Master Password:")

	print("You are in!\n")

def menu(conn):
	while(1):
		print("[1] Search Password")
		print("[2] Add Password")
		print("[3] Show all")
		print("[4] quit\n")

		option = input()

		if option == "1":
			web = input("Which website?")
			web = web.lower()
			rows = db.select_by_website(conn, web)
			for row in rows:
				print(row)
			#print("asking website and username/email, then print associated pwd")
		elif option == "2":
			web = input("Which website?")
			web = web.lower()
			user = input("What is your username?")
			pwd = input("What is your password?")
			db.create_entry(conn, (web, user, pwd))
			#print("asking website and username/email, then user can enter pwd")
		elif option == "3":
			rows = db.select_all(conn)
			for row in rows:
				print(row)
			#print("Show the entire data base")
			#need some way to organize this
		elif option == "4":
			print("Bye!")
			break
		else: #error handle
			print("no such option\n")

conn = db.connect_db(r"pwds.db")
try:
	db.select_all()
except:
	db.create_table(conn)

welcomemsg()
menu(conn)
