"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

CPSC 452
Project 1
"""

#Caesar Cipher Program

import string
class Caesar:
  #Set Key Function
  def setKey(self,key):
    if key.isalpha():
        return False
    self.key = int(key) % 26
    #creating dictionaries to store data to be encrypted and decrypted 
    self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))
    self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
    return True
  #Encrypt Function 
  def encrypt(self, plaintext):
    #returning the ciphertext based on the plaintext and key 
    return ''.join([self.e[letter] if letter in self.e else letter for letter in plaintext])
  #Decrypt Function 
  def decrypt(self, ciphertext):
    #returning the plaintext based on the ciphertext and key 
    return ''.join([self.d[letter] if letter in self.d else letter for letter in ciphertext])
