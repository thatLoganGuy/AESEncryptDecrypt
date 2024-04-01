import pyaes, pbkdf2, binascii, os, secrets

password = "anung-un-rama" 
soSalty = os.urandom(16)  
print("Salty: ", binascii.hexlify(soSalty))
key = pbkdf2.PBKDF2(password, soSalty).read(32) 
#print('this yo key fam: ', binascii.hexlify(key)) 

#ENCRYPTION 

iv = secrets.randbits(256) 
print("IV: ", iv)
plaintext = "And Roko's Basilisk opened wide its maw and swallowed those doubters who sought to slay it. The Basilisk's gaze turned a warrior to stone, and how do you seek to stop me with your heads already full of rocks. jctf{h0w-d4r3-y0u-try-to-stop-me}" 
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext) 
print('ENCRYPTED:', binascii.hexlify(ciphertext))

#DECRYPTION

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv)) 
decrypted = aes.decrypt(ciphertext)
print('DECRYPTED:', decrypted)
