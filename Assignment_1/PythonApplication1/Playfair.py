"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

CPSC 452
Project 1
"""

#Playfair Cipher

import string
class Playfair:
  #Set Key Function
  def setKey(self, key):
    if not key.isalpha():
        return False
    newkey = ""
    for ch in key:
        if ch not in newkey:
            #take care of I/J situation in playfair key matrix
            if ch  is "j":
                if "i" not in newkey:
                    newkey += "i"
			#every other letter n playfair key matrix
            else: 
                newkey += ch
	  #add characters to newkey, other than J
    for ch in string.ascii_lowercase:
        if ch not in newkey and ch is not "j": 
            newkey += ch
        self.key = [['x' for i in range(5)] for j in range(5)]
    row = 0
	#create playfair matrix
    for i in range(len(newkey)):
        self.key[row][i % 5] = newkey[i]
        if ((i + 1) % 5 is 0): 
            row += 1
    return True
  #Encrypt Function
  def encrypt(self, plaintext):
    formattedPlainText = ""
    prev = ""
    #plaintext minus last element 
    for ch in plaintext[:-1]:
        #taking care of repeated character situation
        if ch is prev: formattedPlainText += "x"
        formattedPlainText += ch
        prev = ch

    if len(formattedPlainText) % 2 == 1: formattedPlainText += "x"

    ciphertext = ""
    i = 0
    while (i < len(formattedPlainText)-1):
        #call getGridPosition for both characters
        pos1row, pos1col = self.getGridPosition(formattedPlainText[i])
        i += 1
        pos2row, pos2col = self.getGridPosition(formattedPlainText[i])
        i += 1
		#if same row, letter to the right
        if (pos1row == pos2row): 
            ciphertext += self.key[pos1row][(pos1col + 1) % 5];
            ciphertext += self.key[pos1row][(pos2col + 1) % 5];
        #if same column, letter below
        elif (pos1col is pos2col):
            ciphertext += self.key[(pos1row + 1) % 5][pos1col];
            ciphertext += self.key[(pos2row + 1) % 5][pos1col];
        else:
            ciphertext += self.key[pos1row][pos2col];
            ciphertext += self.key[pos2row][pos1col];
    #adding newline to end of ciphertext
    return ciphertext + '\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
    plaintext = ""
    i = 0
    while (i < len(ciphertext) - 1):
    #call getGridPosition for both characters
        pos1row, pos1col = self.getGridPosition(ciphertext[i])
        i += 1
        pos2row, pos2col = self.getGridPosition(ciphertext[i])
        i += 1
        #if same row, letter to the left
        if (pos1row == pos2row):
            plaintext += self.key[pos1row][(pos1col + 4) % 5];
            plaintext += self.key[pos1row][(pos2col + 4) % 5];
		#if same column, letter above
        elif (pos1col == pos2col):
            plaintext += self.key[(pos1row + 4) % 5][pos1col];
            plaintext += self.key[(pos2row + 4) % 5][pos1col];
        else:
            plaintext += self.key[pos1row][pos2col];
            plaintext += self.key[pos2row][pos1col];
        return plaintext + '\n'
  #Grid Position Function
  def getGridPosition(self, charToFind):
    #search playfair matrix to find positon of charToFind
    for i in range(5):
        for j in range(5):
            if self.key[i][j] is charToFind:
                return i,j
    return 0,0

