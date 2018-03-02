import string
class Caesar:
  
  def setKey(self,key):
    if key.isalpha():
        return False
    self.key = int(key) % 26
    self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))
    self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
    return True
  
  def encrypt(self, plaintext):
    return ''.join([self.e[letter] if letter in self.e else letter for letter in plaintext])
    
  def decrypt(self, ciphertext):
    return ''.join([self.d[letter] if letter in self.d else letter for letter in ciphertext])
