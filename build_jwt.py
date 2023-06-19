#!/usr/bin/python3
import hmac, hashlib, base64, sys
from concurrent.futures import ThreadPoolExecutor

h=sys.argv[1]   #Header in JSON
p=sys.argv[2]   #Payload in JSON
secret=bytes(sys.argv[3],'utf-8')  #Secret
alg=sys.argv[4] #Hash algorithm

#Selecting Algorithm
if alg=='md5':
    alg=hashlib.md5
elif alg=='sha256':
    alg=hashlib.sha256
elif alg=='sha512':
    alg=hashlib.sha512
else:
    print('Unknow hash algorithm')
    sys.exit()

#Header and Body b64url
h64=bytes(base64.urlsafe_b64encode(bytes(h,'utf-8')).decode('utf-8').strip('='),'utf-8')
p64=bytes(base64.urlsafe_b64encode(bytes(p,'utf-8')).decode('utf-8').strip('='),'utf-8')
#Calculating HMAC with sha256 using the secret
hmac_value = hmac.new(secret, (h64+b'.'+p64), alg).hexdigest()
s= bytes.fromhex(hmac_value)
s64=bytes(base64.b64encode(s).decode('utf-8').strip('='),'utf-8')

print('Header: ',h64.decode('utf-8'))
print('Payload ',p64.decode('utf-8'))
print('Signature: ',s64.decode('utf-8'))
print('\njwt: ',h64.decode('utf-8')+'.'+p64.decode('utf-8')+'.'+s64.decode('utf-8') )