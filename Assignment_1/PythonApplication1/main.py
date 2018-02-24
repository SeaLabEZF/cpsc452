import Ciphers

plaintext = "welaunchatdawndonttellanyone"
key = "discovered"
ciphertext = ''
decrypted = ''

testCase = Ciphers.Vigenere()

testCase.setKey(key)
ciphertext = testCase.encrypt(plaintext)
decrypted = testCase.decrypt(ciphertext)

print("plaintext = ",plaintext)
print("ciphertext = ",ciphertext)
print("decrypted = ",decrypted)