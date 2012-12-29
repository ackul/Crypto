'''ENCRYPTING AND DECRYPTING using AES CBC mode'''
import sys
import chilkat
'''Using the Chilkat Crypto library'''
crypt = chilkat.CkCrypt2()
if (success != True):
    print "Crypt component unlock failed"
    sys.exit()
'''Defining Crypto Algorithm'''
crypt.put_CryptAlgorithm("aes")
crypt.put_CipherMode("cbc")
crypt.put_KeyLength(128)
inBytes = ''
for i in range(0,256):
	inBytes = inBytes + chr(i)
keyBytes = ''
for i in range(0,16):
	keyBytes = keyBytes + chr(i)
ivBytes = ''
for i in range(0,16):
	ivBytes = ivBytes + chr(i)
crypt.SetSecretKey(keyBytes,16)
crypt.SetIV(ivBytes,16)

inData = chilkat.CkByteData()
inData.append(inBytes,256)
'''Putting Encrypted Data'''
encryptedData = chilkat.CkByteData()
crypt.EncryptBytes(inData,encryptedData)
encryptedBytes = encryptedData.getBytes()
print "encrypted size = " + str(len(encryptedBytes)) + " bytes\n"
'''Saving the data'''
encryptedData.saveFile("encryptedData.dat")
print crypt.encodeBytes(encryptedBytes,len(encryptedBytes),"hex") + "\n"

'''Decrypting the Data'''
decryptedData = chilkat.CkByteData()
crypt.DecryptBytes(encryptedData,decryptedData )
decryptedBytes = decryptedData.getBytes()
print "Decrypted size = " + str(len(decryptedBytes)) + " bytes\n"
print crypt.encodeBytes(decryptedBytes,len(decryptedBytes),"hex") + "\n"