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
      while row_number != 0:
          plaintext += 'x'
          row_number = len(plaintext) % len(str(self.key))
      row_number = int(len(plaintext) / len(str(self.key)))
      for key_len_it in range(row_number):
          encode.append([])
          for plaintext_it, i in zip(plaintext, str(self.key)):
              encode[key_len_it].append(plaintext_it)
          plaintext = plaintext[len(str(self.key)):]
      ciphertext = ''
      for key_it in str(self.key):
          for col_it in range(row_number):
              ciphertext += encode[col_it][int(key_it)-1]
      return ciphertext + '\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
      decode = []
      row_number = int(len(ciphertext) / len(str(self.key)))
      for i in range(row_number):
          decode.append([])
          for j in range(len(str(self.key))):
              decode[i].append([])
      for key_it in str(self.key):
          for ciphertext_it, i in zip(ciphertext, range(row_number)):
              decode[i][int(key_it)-1] = ciphertext_it
          ciphertext = ciphertext[row_number:]
      return ''.join(''.join(letter for letter in sub) for sub in decode) + '\n'
