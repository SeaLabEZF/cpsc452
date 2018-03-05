"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

CPSC 452
Project 1
"""

#Main program

import sys
import Caesar
import RailFence
import Row_Transposition
import Playfair
import Vigenere

#Checking user input 
if len(sys.argv) < 6:
    print("You are missing arguments, check your input.")
else:
	#Playfair Cipher
    if str(sys.argv[1]) == 'PLF':
        cipher_type = Playfair.Playfair()
	#Row_Transposition Cipher
    elif str(sys.argv[1]) == 'RTS':
        cipher_type = Row_Transposition.Row_Transposition()
	#RailFence Cipher
    elif str(sys.argv[1]) == 'RFC':
        cipher_type = RailFence.Railfence()
	#Vigenere Cipher
    elif str(sys.argv[1]) == 'VIG':
        cipher_type = Vigenere.Vigenere()
	#Caesar Cipher
    elif str(sys.argv[1]) == 'CES':
        cipher_type = Caesar.Caesar()
	#Invalid Input
    else:
        print("Unrecognized cipher type, check your spelling and try again.")
        exit()
	#Setting key from inputfile 
    if cipher_type.setKey(sys.argv[2]):
        inFile = open(str(sys.argv[4]),"r")
        inputText = inFile.read()
	#If user input is VIG then output to outputText from inputText
	if str(sys.argv[1]) == 'VIG':
	    cipher_type.textToKeyCompare(inputText)
        if str(sys.argv[3]) == 'ENC':
            outputText = cipher_type.encrypt(inputText)
        elif str(sys.argv[3] == 'DEC'):
            outputText = cipher_type.decrypt(inputText)
		#Invalid user input
        else:
            print("Unrecognized coding type, did you want Encode or Decode?")
            exit()
		#write to outFile
        outFile = open(str(sys.argv[5]), "w")
        outFile.write(outputText)
        
	inFile.close()
        outFile.close()
	#Encryption and decryption messages for other cipher operations
	if str(sys.argv[3]) == 'ENC':
            print("Encryption Complete. Stored in ", str(sys.argv[5]))
	else:
            print("Decryption Complete. Stored in ", str(sys.argv[5]))
    else:
        print("Key is incorrect check to ensure your key matches with the cipher type")         
