from pwn import *
from Crypto.Util.number import *
import json
from cracker import RandCrack
import string
import base64
import random

def otp(a, b):
	r = ""
	for i, j in zip(a, b):
		r += chr(ord(i) ^ ord(j))
	return r

def genSample():
	p = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(random.randint(1, 30))])
	k = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(len(p))])

	x = otp(p, k)

	return x, p, k

io = remote("misc.2020.chall.actf.co", 20301)
print (io.recvuntil(">"))
Time = int(time.time())
print ("Time: {}".format(Time))
io.sendline("2")
recv_x = io.recvline().strip().decode()
print("recv_x: {}".format(recv_x))

for i in range(Time-100, Time+100):
	random.seed(i)
	x, p, k = genSample()
	if base64.b64encode(x.encode()).decode() == recv_x:
		io.sendline(p)
		print ("Found_p: {}".format(p)	)
		break

while True:
	print(io.recvline())


