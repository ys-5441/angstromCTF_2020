from pwn import *
from Crypto.Util.number import *
import re
from primefac import factorint
​
"""
We define a^^b to be such that a^^0 = 1 and a^^b = a^(a^^(b-1)), where x^y represents x to the power of y.
Given this, find a positive integer x such that a^^x = b mod p.
"""
​
def totient(n):
    totient = n
    for factor in factorint(n):
        totient -= totient // factor
    return totient
​
def Double_exp(a, b, p):
	if (b == 0):
		return 1
	return pow(a, Double_exp(a, b-1, totient(p)), p)
​
def Solv():
	print(io.recvuntil("..."))
	raw_m = io.recvuntil(":").strip().decode()
	print ("raw_m: {}".format(raw_m))
	numbers = re.findall(pattern, raw_m)
	p = int(numbers[0])
	a = int(numbers[1])
	b = int(numbers[2])
​
	for x in range(2, 500):
		b_cand = Double_exp(a, x, p)
		#print("b_cand: {}".format(b_cand))
		if b == b_cand:
			print ("found_x: {}".format(x))
			break
	return x
​
​
io = remote("3.228.7.55", 20603)
pattern = "[0-9]+"
​
for i in range(10):
	print ("i: {}".format(i))
	found_x = Solv()
	io.sendline(str(found_x))
	
while True:
	print(io.recvline())
