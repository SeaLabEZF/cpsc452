"""
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

CPSC 452
Project 1
"""

#RailFence Cipher

import string
class Railfence:
  #Set Key Function
  def setKey(self, key):
      if key.isalpha():
          return False
	  #converting key into integer
      self.key = int(key)
      return True
  #Encrypt Function
  def encrypt(self, plaintext):
        cipherArr = ["" for i in range(self.key)]
        count = 0
	#removing newline character from plaintext
	if plaintext.endswith('\n'):
	    plaintext = plaintext[:-1]
	#updating contents of cipherArr based on the key and plaintext
	for char in plaintext:
            cipherArr[count % self.key] += char
            count += 1
	    #updating contents of cipherArr based on the key and plaintext, adding newlines for each new row
        if int(len(plaintext) % self.key) is not 0:
            for i in range(self.key - 1, int(len(plaintext) % self.key) - 1, -1):
                cipherArr[i] += " "
        return "".join(cipherArr) + '\n'
  #Decrypt Function
  def decrypt(self, ciphertext):
        cipherArr = ["" for i in range(self.key)]
        plaintext = ""
	#removing last element of ciphertext
	ciphertext = ciphertext[:-1]
		#used for finding letter to use in cipher row
        offset = int(len(ciphertext) / self.key)
        for i in range(self.key):
			#update cipherArr based off the offset and current element of ciphertext 
            cipherArr[i] = ciphertext[(i * offset):(i * offset) + offset]
        strIndex = 0
	
        for i in range(len(ciphertext)):
            if i % self.key is 0 and i is not 0:
                strIndex += 1
			#updating plaintext with correct letter in rail-fence row index
            plaintext += cipherArr[i % self.key][strIndex]
		#adding newline to end of plaintext
        return plaintext + '\n'
