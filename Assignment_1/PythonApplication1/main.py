import Ciphers

plaintext = "testcase"
key = "asdfasdfasdfasdfasdfasdfasdfasdf"
ciphertext = ''
decrypted = ''

testCase = Ciphers.Vigenere()

testCase.createChart(key, plaintext)
print(testCase.key)