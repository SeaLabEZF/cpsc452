"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

CPSC 452
Project 1
"""

#Vigenere Cipher

import string
class Vigenere:
  #Set Key Function
  def setKey(self, key):
    if not key.isalpha():
        return False
    self.key = key
	#creating dictionary to store encryped and decryped data
    self.e = dict(zip(string.ascii_lowercase, range(0,26)))
    self.d = {v: k for k, v in self.e.items()}
    self.chart = []
	#2 dimensional data structure to contain vigenere square
    for chart_index in range(0,26):
        self.chart.append([])
        for letter in string.ascii_lowercase[chart_index:] + string.ascii_lowercase[:chart_index]:
          self.chart[chart_index].append(letter)
    return True
  #Key Comparison Function 
  def textToKeyCompare(self, text):
    #executes as long as the length of the key is smaller than the legnth of the text
    while len(self.key) < len(text):
        self.key += self.key
    if len(self.key) > len(text):
	#updating key with the elements after the index of the last element in the text
        self.key = self.key[:len(text)-len(self.key)]
  #Encrypt Function
  def encrypt(self, plaintext):
    self.textToKeyCompare(plaintext)
    #returning cipher text based off of key and plaintext in vigenere square
    return ''.join(self.chart[self.e[key_it]][self.e[plaintext_it]] for plaintext_it, key_it in zip(plaintext, self.key)[:-1])+'\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
    self.textToKeyCompare(ciphertext)
    #returning plaintext based off of key and cipher text in vigenere square 
    return ''.join(self.d[self.chart[self.e[key_it]].index(ciphertext_it)] for ciphertext_it, key_it in zip(ciphertext, self.key)[:-1])+'\n'
