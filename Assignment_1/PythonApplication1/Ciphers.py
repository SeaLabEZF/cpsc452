import string


class Caesar:
  
  def setKey(self,key):
    if key.isalpha():
        return False
    self.key = key % 26
    self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))
    self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
    return True
  
  def encrypt(self, plaintext):
    return ''.join([self.e[letter] if letter in self.e else letter for letter in plaintext])
    
  def decrypt(self, ciphertext):
    return ''.join([self.d[letter] if letter in self.d else letter for letter in ciphertext])


class Playfair:
  
  def setKey(self, key):
      if not key.isalpha():
          return False
      newkey = ""
      for ch in key:
          if ch not in newkey:
              if ch  is "j":
                  if "i" not in newkey:
                      newkey += "i"
              else: 
                  newkey += ch
      for ch in string.ascii_lowercase:
          if ch not in newkey and ch is not "j": 
              newkey += ch
          self.key = [['x' for i in range(5)] for j in range(5)]
      row = 0
      for i in range(len(newkey)):
          self.key[row][i % 5] = newkey[i]
          if ((i + 1) % 5 is 0): 
              row += 1
      return True

  def encrypt(self, plaintext):
        formattedPlainText = ""
        prev = ""
        for ch in plaintext:
            if ch is prev: formattedPlainText += "x"
            formattedPlainText += ch
            prev = ch

        if len(formattedPlainText) % 2 == 1: formattedPlainText += "x"

        ciphertext = ""
        i = 0
        while (i < len(formattedPlainText)):
            pos1row, pos1col = self.getGridPosition(formattedPlainText[i])
            i += 1
            pos2row, pos2col = self.getGridPosition(formattedPlainText[i])
            i += 1

            if (pos1row == pos2row): 
                ciphertext += self.key[pos1row][(pos1col + 1) % 5];
                ciphertext += self.key[pos1row][(pos2col + 1) % 5];
            elif (pos1col is pos2col):
                ciphertext += self.key[(pos1row + 1) % 5][pos1col];
                ciphertext += self.key[(pos2row + 1) % 5][pos1col];
            else:
                ciphertext += self.key[pos1row][pos2col];
                ciphertext += self.key[pos2row][pos1col];

        return ciphertext
  
  def decrypt(self, ciphertext):
        plaintext = ""
        i = 0
        while (i < len(ciphertext)):
            pos1row, pos1col = self.getGridPosition(ciphertext[i])
            i += 1
            pos2row, pos2col = self.getGridPosition(ciphertext[i])
            i += 1

            if (pos1row == pos2row):
                plaintext += self.key[pos1row][(pos1col + 4) % 5];
                plaintext += self.key[pos1row][(pos2col + 4) % 5];
            elif (pos1col == pos2col):
                plaintext += self.key[(pos1row + 4) % 5][pos1col];
                plaintext += self.key[(pos2row + 4) % 5][pos1col];
            else:
                plaintext += self.key[pos1row][pos2col];
                plaintext += self.key[pos2row][pos1col];

        return plaintext

  def getGridPosition(self, charToFind):
        for i in range(5):
            for j in range(5):
                if self.key[i][j] is charToFind:
                    return i,j
        return 0,0

    
class Row_Transposition:

  def setKey(self, key):
      if key.isalpha():
          return False
      self.key = key
      return True
  
  def encrypt(self, plaintext):
      encode = []
      row_number = len(plaintext) % len(str(self.key))
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
      return ciphertext

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
      return ''.join(''.join(letter for letter in sub) for sub in decode)

    
class Railfence:

  def setKey(self, key):
    return True
  
  def encrypt(self, plaintext):
    return ""
  
  def decrypt(self, ciphertext):
    return ""

    
class Vigenere:

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

  def textToKeyCompare(self, text):
      while len(self.key) < len(text):
          self.key += self.key
      if len(self.key) > len(text):
          self.key = self.key[:len(text)-len(self.key)]

  def encrypt(self, plaintext):
    return ''.join(self.chart[self.e[key_it]][self.e[plaintext_it]] for plaintext_it, key_it in zip(plaintext, self.key))
  
  def decrypt(self, ciphertext):
    return ''.join(self.d[self.chart[self.e[key_it]].index(ciphertext_it)] for ciphertext_it, key_it in zip(ciphertext, self.key))
