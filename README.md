# PwdManager
Storing passwords for different website and accounts

Passwords that stored are encrypted with a randomly generated key.  User has to use the same key to access the passwords database

Note:
menu.py is the main file
Using getpass to hide the encryption key entry, but it doesn't work with 'Ctrl+V'. I use Powershell on Windows 10 and found right click would actually paste. Different system and terminal may work differently

To-do:
1. create a hased masterpassword to add another layer of security.
2. automatically generate password.