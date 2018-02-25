import Ciphers

plaintext = "transpositionciphers"
key = "2135467"
ciphertext = ''
decrypted = ''

testCase = Ciphers.Row_Transposition()

testCase.setKey(key)
ciphertext = testCase.encrypt(plaintext)
decrypted = testCase.decrypt(ciphertext)
print(plaintext)
print(ciphertext)
print(decrypted)


