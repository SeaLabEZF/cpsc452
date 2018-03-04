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
      self.e = dict(zip(string.ascii_lowercase, range(0,26)))
      self.d = {v: k for k, v in self.e.items()}
      self.chart = []
      for chart_index in range(0,26):
          self.chart.append([])
          for letter in string.ascii_lowercase[chart_index:] + string.ascii_lowercase[:chart_index]:
            self.chart[chart_index].append(letter)
      return True
  #Key Comparison Function 
  def textToKeyCompare(self, text):
      while len(self.key) < len(text):
          self.key += self.key
      if len(self.key) > len(text):
          self.key = self.key[:len(text)-len(self.key)]
  #Encrypt Function
  def encrypt(self, plaintext):
      self.textToKeyCompare(plaintext)
      return ''.join(self.chart[self.e[key_it]][self.e[plaintext_it]] for plaintext_it, key_it in zip(plaintext, self.key)[:-1])+'\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
      self.textToKeyCompare(ciphertext)
      return ''.join(self.d[self.chart[self.e[key_it]].index(ciphertext_it)] for ciphertext_it, key_it in zip(ciphertext, self.key)[:-1])+'\n'
