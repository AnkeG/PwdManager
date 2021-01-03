import db

def welcomemsg():
	print("Welcome to Password Manager")
	MasterPwd = input("Plase enter the Master Password:")

	while MasterPwd != "12345":
		print("Wrong Master Password")
		MasterPwd = input("Plase enter the Master Password:")

	print("You are in!\n")

def display_pwds(rows):
	print("Id    website    username    pwds")
	print("---------------------------------------------------------------")
	for row in rows:
		print(row[0], "    ", row[1], "    ", row[2], "    ", row[3])
	print("\n")

def menu(conn):
	while(1):
		print("*******************************")
		print("[1] Search Passwords")
		print("[2] Add A Password")
		print("[3] Show All")
		print("[4] Update A Password")
		print("[5] Delete A Password")
		print("[6] quit")
		print("*******************************")

		option = input()

		if option == "1":
			web = input("Which website?")
			web = web.lower()
			rows = db.select_by_website(conn, web)
			if not rows:
				print("No password of ", web, " stored\n")
			else:
				display_pwds(rows)
			#print("asking website and username/email, then print associated pwd")

		elif option == "2":
			web = input("Which website? ")
			web = web.lower()
			user = input("What is your username? ")
			pwd = input("What is your password? ")
			db.create_entry(conn, (web, user, pwd))
			print("password stored\n")
			#print("asking website and username/email, then user can enter pwd")

		elif option == "3":
			rows = db.select_all(conn)
			if not rows:
				print("no passwords stored yet\n")
			else:
				display_pwds(rows)
			#print("Show the entire data base")
			#need some way to organize this

		elif option == "4":
			pwdid = input("Enter the id of the password need to be updated: ")
			pwdid = int(pwdid)
			pwd = input("Enter the new password: ")
			db.update_pwd_by_id(conn, pwd, pwdid)
			rows = db.select_by_id(conn, pwdid)
			display_pwds(rows)
			#print("update password")

		elif option == "5":
			pwdid = input("Enter the id of the password need to delete: ")
			pwdid = int(pwdid)
			db.delete_task(conn, pwdid)

		elif option == "6":
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
