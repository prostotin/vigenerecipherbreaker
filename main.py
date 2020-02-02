ciphertext = 'zeoldugkqrxzfifhfetkdobk'
letters='abcdefghijklmnopqrstuvwzyz' #used to create the key
def decrypt(key): #function that decrypts the ciphertext
    keyLength = len(key)
    keyAsInt = [ord(i) for i in key]
    ciphertextInt = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertextInt)):
        value = (ciphertextInt[i] - keyAsInt[i % keyLength]) % 26
        plaintext += chr(value + 65)
    return plaintext.lower()

i=0;j=0;k=0;l=0 
counter = 0

key=''
index = []
#bruteforce through every possible key and see if droid is contained in the decrypted message
for i in range(0,26):
    for j in range(0,26):        
        for k in range (0,26):
            for l in range(0,26):
                key = letters[i] + letters[j] + letters[k] + letters[l]
                counter+=1
                result = decrypt (key)    
                if 'droid' in result:
                    index.append(counter)
                    print('Success. Key used |' + key + "|, decrypted message:|" + result + "|")
#print reslts                    
print('Program finished, tries: ' + str(counter) + ",matches found at indexes: ")
print(index)
