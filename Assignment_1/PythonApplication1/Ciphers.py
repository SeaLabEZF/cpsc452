import string
import itertools


class Caesar:
  
  def setKey(self,key):
    self.key = key % 26
    self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))
    self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
  
  def encrypt(self, plaintext):
    return ''.join([self.e[letter] if letter in self.e else letter for letter in plaintext])
    
  def decrypt(self, ciphertext):
    return ''.join([self.d[letter] if letter in self.d else letter for letter in ciphertext])


class Playfair:
  
  def setKey(self, key):
    return False

  def encrypt(self, plaintext):
    return ""
  
  def decrypt(self, ciphertext):
    return ""

    
class Row_Transposition:

  def setKey(self, key):
      return False
  
  def encrypt(self, plaintext):
    return ""
  
  def decrypt(self, cyphertext):
    return ""

    
class Railfence:

  def setKey(self, key):
    return False
  
  def encrypt(self, plaintext):
    return ""
  
  def decrypt(self, ciphertext):
    return ""

    
class Vigenere:

  def setKey(self, key):
      self.key = key
      self.e = dict(zip(string.ascii_lowercase, range(0,26)))
      self.d = {v: k for k, v in self.e.items()}
      self.chart = []
      for chart_index in range(0,26):
          self.chart.append([])
          for letter in string.ascii_lowercase[chart_index:] + string.ascii_lowercase[:chart_index]:
            self.chart[chart_index].append(letter)

  def textToKeyCompare(self, text):
      while len(self.key) < len(text):
          self.key += self.key
      if len(self.key) > len(text):
          self.key = self.key[:len(text)-len(self.key)]

  def encrypt(self, plaintext):
    return ''.join(self.chart[self.e[key_it]][self.e[plaintext_it]] for plaintext_it, key_it in zip(plaintext, self.key))
  
  def decrypt(self, ciphertext):
    return ''.join(self.d[self.chart[self.e[key_it]].index(ciphertext_it)] for ciphertext_it, key_it in zip(ciphertext, self.key))
