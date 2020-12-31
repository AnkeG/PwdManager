def welcomemsg():
	print("Welcome to Password Manager")
	MasterPwd = input("Plase enter the Master Password:")

	while MasterPwd != "12345":
		print("Wrong Master Password")
		MasterPwd = input("Plase enter the Master Password:")

	print("You are in!\n")

def menu():
	while(1):
		print("[1] Search Password")
		print("[2] Add/update Password")
		print("[3] Show all")
		print("[4] quit\n")

		option = input()

		if option == "1":
			print("asking website and username/email, then print associated pwd")
		elif option == "2":
			print("asking website and username/email, then user can enter pwd")
		elif option == "3":
			print("Show the entire data base")
			#need some way to organize this
		elif option == "4":
			print("Bye!")
			break
		else: #error handle
			print("no such option\n")


welcomemsg()
menu()

