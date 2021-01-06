# PwdManager
Storing passwords for different website and accounts

Passwords that stored are encrypted with a randomly generated 32 bit key.  User has to use the same key to access the passwords database

Autogenerate 10 characters password with least 1 upper letter, 1 lower letter, 1 special character, and 3 numbers

Note:
1. menu.py is the main file.
2. Using getpass module to hide the encryption key entry, but it doesn't work with 'Ctrl+V'. I use Powershell on Windows 10 and found right click would paste. Different system and terminal may work differently