from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

start = time.time()

keyPair = RSA.generate(3072)

time.sleep(1)


pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'A falkensmaze'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

end = time.time()  

print(f"Runtime is {end - start}")