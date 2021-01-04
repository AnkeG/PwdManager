import db, crypt, pyperclip

def welcomemsg():
	print("Welcome to Password Manager")
	MasterPwd = input("Please enter the Master Password:")

	while MasterPwd != "12345":
		print("Wrong Master Password")
		MasterPwd = input("Please enter the Master Password:")

	print("You are in!\n")

def display_pwds(cipher, rows):
	print("Id    website    username    pwds")
	print("---------------------------------------------------------------")
	for row in rows:
		print(row[0], "    ", 
			row[1], "    ", 
			row[2], "    ", 
			crypt.decrypt_pwd(cipher, row[3]))
	print("\n")

def get_key():
	key = input("Please enter the encryption key: ")
	key = str.encode(key)
	print(key)
	return key

def submenu(conn, cipher):
	print("**[1] Update; [2] Delete [3]Copy to clip board**")
	option = input("Enter above option numnber or other keys to quit: ")
	if option == '1':
		pwdid = input("What is the id of the password need to be updated? ")
		pwdid = int(pwdid)
		pwd = input("What is the new password? ")
		pwd = crypt.encrypt_pwd(cipher, pwd)
		db.update_pwd_by_id(conn, pwd, pwdid)
		print("Password updated")
		rows = db.select_by_id(conn, pwdid)
		display_pwds(cipher, rows)
	elif option == '2':
		pwdid = input("Enter the id of the password need to delete: ")
		pwdid = int(pwdid)
		db.delete_task(conn, pwdid)
		print("Password deleted\n")
	elif option == '3':
		pwdid = input("Enter the id of the password need to be copied: ")
		pwdid = int(pwdid)
		rows = db.select_by_id(conn, pwdid)
		for row in rows:
			pwd = crypt.decrypt_pwd(cipher, row[3])
			pyperclip.copy(pwd)
		print("Password copied to clipboard\n")


def menu(conn, key):

	cipher = crypt.read_key(key)

	while(1):
		print("*******************************")
		print("[1] Search Passwords by website")
		print("[2] Add A Password")
		print("[3] Show All")
		print("[4] Exit")
		print("*******************************")

		option = input("Enter number of the option: ")

		if option == "1":
			web = input("Which website?")
			web = web.lower()
			rows = db.select_by_website(conn, web)
			if not rows:
				print("No password of ", web, " stored\n")
			else:
				display_pwds(cipher, rows)
				submenu(conn, cipher)

		elif option == "2":
			web = input("Which website? ")
			web = web.lower()
			user = input("What is your username? ")
			pwd = input("What is your password? ")
			pwd = crypt.encrypt_pwd(cipher, pwd)
			db.create_entry(conn, (web, user, pwd))
			print("password stored\n")

		elif option == "3":
			rows = db.select_all(conn)
			if not rows:
				print("no passwords stored yet\n")
			else:
				display_pwds(cipher, rows)
				submenu(conn, cipher)

		elif option == "4":
			print("Bye!")
			break

		else: #error handle
			print("no such option\n")



conn = db.connect_db(r"pwds.db")
db.create_table(conn)

print("If you are the first time here, please use the following key and save it to a safe place.")
print("You will need to enter this key to get your passwords in the future")
print(crypt.new_key(), '\n')

#welcomemsg()
key = get_key()
menu(conn, key)
