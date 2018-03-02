import string
class Railfence:

  def setKey(self, key):
      if key.isalpha():
          return False
      self.key = int(key)
      return True
  
  def encrypt(self, plaintext):
        cipherArr = ["" for i in range(self.key)]
        count = 0
	plaintext = plaintext[:-1]
        for char in plaintext:
            cipherArr[count % self.key] += char
            count += 1

        if int(len(plaintext) % self.key) is not 0:
            for i in range(self.key - 1, int(len(plaintext) % self.key) - 1, -1):
                cipherArr[i] += " "

        return "".join(cipherArr) + '\n'
  
  def decrypt(self, ciphertext):
        cipherArr = ["" for i in range(self.key)]
        plaintext = ""
        offset = int(len(ciphertext) / self.key)
	ciphertext = ciphertext[:-1]
        for i in range(self.key):
            cipherArr[i] = ciphertext[(i * offset):(i * offset) + offset]
        strIndex = 0
        for i in range(len(ciphertext)):
            if i % self.key is 0 and i is not 0:
                strIndex += 1
            plaintext += cipherArr[i % self.key][strIndex]

        return plaintext + '\n'
