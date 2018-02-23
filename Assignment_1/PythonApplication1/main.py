import Ciphers

plaintext = "testcase"
key = "asdfasdf"
ciphertext = ''
decrypted = ''

testCase = Ciphers.Vigenere()

if testCase.createChart(key, plaintext):
    ciphertext = testCase.encrypt(plaintext)
    decrypted = testCase.decrypt(ciphertext)
    print(plaintext)
    print(ciphertext)
    print(decrypted)