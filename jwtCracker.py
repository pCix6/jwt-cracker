#!/usr/bin/python3
import hmac, hashlib, base64, sys
from concurrent.futures import ThreadPoolExecutor

jwt=sys.argv[1] #jwt
alg=sys.argv[2] #Hash algorithm
wl=sys.argv[3]  #WordList to use
t=int(sys.argv[4])  #Number of threads

#Splitting JWT
jwt=jwt.split('.')
try:
    h=jwt[0]    #Header
    p=jwt[1]    #Payload
    sign=bytes(jwt[2].replace('_','/').replace('-','+'),'utf-8') #Will use it in bytes
    #Adding padd to avoid errors in decoding and then from bytes to string
    h=base64.b64decode(h+'='*(len(h)%3)).decode('utf-8')    #Decoded string
    p=base64.b64decode(p+'='*(len(p)%3)).decode('utf-8')    #Decoded string
except:
    print('Error processing jwt')
    sys.exit()

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

#Header and Payload base64url encoded
#h/p to bytes to encode b64url, decode it to string to strip padd and then to bytes
h64=bytes(base64.urlsafe_b64encode(bytes(h,'utf-8')).decode('utf-8').strip('='),'utf-8')
p64=bytes(base64.urlsafe_b64encode(bytes(p,'utf-8')).decode('utf-8').strip('='),'utf-8')

#Reading wordlist
f=open(wl,'r')
words=f.readlines()
f.close()
words=[s.replace('\n','') for s in words]

#Threads will use this function to try to crack jwt
def crack(n):
   listT=words[(len(words)//t)*(n):index(n)]    #Words a nThread will use
   for i in listT:
       hmac_value = hmac.new(bytes(i,'utf-8'), (h64+b'.'+p64), alg).hexdigest() #Calculating HMAC
       s= bytes.fromhex(hmac_value) #From a hexadecimal string to bytes
       s64=bytes(base64.b64encode(s).decode('utf-8').strip('='),'utf-8')    #B64 encoding, to str to strip padding and to bytes
       if sign in s64:
           print('PASSWORD FOUND!!: ',i)
           sys.exit()

#Calculate the last wordlist index the n Thread should use
def index(n):
    d=(len(words)//t)*(n+1)
    if n==t-1:
        d=len(words)
    return d
#Create a pool of Threads and execute their tasks
executor = ThreadPoolExecutor(max_workers=t+1)
for i in range(t):
    executor.submit(crack,i)