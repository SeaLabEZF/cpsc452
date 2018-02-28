import sys
import Caesar
import RailFence
import Row_Transposition
import Playfair
import Vigenere

if len(sys.argv) < 6:
    print("You are missing arguments, check your input.")
else:
    if str(sys.argv[1]) == 'PLF':
        cipher = Playfair.Playfair
    elif str(sys.argv[1]) == 'RTS':
        cipher = Row_Transposition.Row_Transposition
    elif str(sys.argv[1]) == 'RFC':
        cipher = RailFence.Railfence
    elif str(sys.argv[1]) == 'VIG':
        cipher = Vigenere.Vigenere
    elif str(sys.argv[1]) == 'CES':
        cipher = Caesar.Caesar     
    else:
        print("Unrecognized cipher type, check your spelling and try again.")
        exit()
    if cipher.setKey(str(sys.argv[2])):
        inFile = open(str(sys.argv[4]),"r")
        inputText = inFile.read()
        if str(sys.argv[3]) == 'ENC':
            outputText = cipher.encrypt(inputText)
        elif str(sys.argv[3] == 'DEC'):
            outputText = cipher.decrypt(inputText)
        else:
            print("Unrecognized coding type, did you want Encode or Decode?")
            exit()
        outFile = open(str(sys.argv[5]), "w")
        outFile.write(outputText)
        inFile.close()
        outFile.close()
        print("Encryption Complete. Stored in ", str(sys.argv[5]))  
    else:
        print("Key is incorrect check to ensure your key matches with the cipher type")         