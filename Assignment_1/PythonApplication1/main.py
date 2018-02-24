import Ciphers

plaintext = "welaunchatdawndonttellanyone"
key = "discovered"
ciphertext = ''
decrypted = ''

testCase = Ciphers.Vigenere()

testCase.setKey(key)
testCase.textToKeyCompare(plaintext)
ciphertext = testCase.encrypt(plaintext)
decrypted = testCase.decrypt(ciphertext)

print(plaintext)
print(ciphertext)
print(decrypted)