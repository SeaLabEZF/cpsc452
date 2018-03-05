"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean
CPSC 452
Project 1
"""

#Row Transportation Cipher

import string
class Row_Transposition:
  #Set Key Function
  def setKey(self, key):
    if key.isalpha():
        return False
    self.key = key
    return True
  #Encrypt Function
  def encrypt(self, plaintext):
    encode = []
    row_number = len(plaintext) % len(str(self.key))
    plaintext = plaintext[:-1]
    while row_number != 0:  # while loop adds filler character 'x' in order to fill out the rows evenly
        plaintext += 'x'
        row_number = len(plaintext) % len(str(self.key))  # if there are any remainders that means the row is not full
    row_number = int(len(plaintext) / len(str(self.key)))
    for key_len_it in range(row_number):
        encode.append([])
        for plaintext_it, i in zip(plaintext, str(self.key)):
            encode[key_len_it].append(plaintext_it)  # appends into encode 1 by 1 the zip of plaintext and key
        plaintext = plaintext[len(str(self.key)):]  # sets plaintext to all characters after length of key
    ciphertext = ''
    for key_it in str(self.key):
        for col_it in range(row_number):
            ciphertext += encode[col_it][int(key_it)-1]  # ciphertext is made by ordering the columns based on the key
    return ciphertext + '\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
    decode = []
    row_number = int(len(ciphertext) / len(str(self.key)))
    for i in range(row_number):
        decode.append([])
        for j in range(len(str(self.key))):
            decode[i].append([])  # decode is empty with no elements in it yet
    for key_it in str(self.key):
        for ciphertext_it, i in zip(ciphertext, range(row_number)):
            decode[i][int(key_it)-1] = ciphertext_it  # the ciphertext ordered in decode based on the key
        ciphertext = ciphertext[row_number:]
    # joined to to make decrypted text
    return ''.join(''.join(letter for letter in sub) for sub in decode) + '\n'