from itertools import permutations

cipher = r"agqr{yue_stdcgciup_padas}"

key_1 = "ANGSTROMCTF"
key_2 = "BDEHIJKLPQUVWXYZ"


flag_part = "actf"
for i in range(len(flag_part)):
	print ((ord(flag_part[i]) - ord(cipher[i])))%26

key = key_1 + key_2
m = ""
for i in range(len(cipher)):
	c = cipher[i]
	#print (c.swapcase())
	if c == "{" or c =="}" or c == "_":
		m += c
		continue
	m += chr(key.index(c.swapcase()) + 97)
	
print (m)
print (key)
