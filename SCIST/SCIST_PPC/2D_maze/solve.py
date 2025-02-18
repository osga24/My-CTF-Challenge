from pwn import *
from tqdm import trange
r = remote('lab.scist.org',31012)

r.recvlines(14)

for i in trange(100):
    r.recvlines(3+9)
    r.sendlineafter(b': ','w'.encode())

r.interactive()
