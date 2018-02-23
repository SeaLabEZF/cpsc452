import string

class Caesar:
  
  def setKey(self,key=3):
    self.key = key % 26
    
    self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))
    self.e.update(dict(zip(string.ascii_uppercase, string.ascii_uppercase[self.key:] + string.ascii_uppercase[:self.key])))
    
    self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
    self.d.update(dict(zip(string.ascii_uppercase[self.key:] + string.ascii_uppercase[:self.key], string.ascii_uppercase)))
  
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

  def createChart(self, key, plaintext):
      if len(key) < len(plaintext):
          key_len_it = len(key) + 1
          key_it = 0
          while key_len_it <= len(plaintext):
              key += (key[key_it])
              key_len_it += 1
              key_it += 1
      elif len(key) > len(plaintext):
          diff_len = len(key) - len(plaintext)
          key = key[:-diff_len]
      self.key = key
      self.e = dict(zip(string.ascii_lowercase, range(0,26)))
      self.d = {v: k for k, v in self.e.items()}
      self.chart = []
      for index in range(0,26):
          self.chart.append([])
          for it in range(0,26):
              letter = chr(ord('a') + it + index)
              if ord(letter) > ord('z'):
                  letter = chr(ord('a') + (ord(letter) - ord('z')))
              self.chart[index].append(letter)

  def encrypt(self, plaintext):
    ret = ''
    it = 0
    for i in plaintext:
        ret += self.chart[self.e[self.key[it]]][self.e[plaintext[it]]]
        it += 1
    return ret
  
  def decrypt(self, ciphertext):
    ret = ''
    it = 0
    plaintext_convert = ''
    for i in ciphertext:
        plaintext_convert = self.chart[self.e[self.key[it]]].index(ciphertext[it])
        ret += self.d[plaintext_convert]
        it += 1
    return ret
