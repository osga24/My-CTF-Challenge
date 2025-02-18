import base64
from string import ascii_lowercase, ascii_uppercase

check = ['apple', 'grape', 'peach', 'berry', 'plum', 'lemon', 'melon', 'mango', 'bread', 'cheese', 'honey', 'candy', 'salad', 'olive', 'bacon', 'cream', 'drink', 'water', 'juice', 'pizza', 'pasta', 'sushi', 'tacos', 'steak']

def rot_decode(text, shift):
    decoded = []
    for char in text:
        if char in ascii_lowercase:
            index = (ascii_lowercase.index(char) - shift) % 26
            decoded.append(ascii_lowercase[index])
        elif char in ascii_uppercase:
            index = (ascii_uppercase.index(char) - shift) % 26
            decoded.append(ascii_uppercase[index])
        else:
            decoded.append(char)
    return ''.join(decoded)

def decode(encoded_text):
    for shift in range(1, 27):
        try:
            rot_decoded = rot_decode(encoded_text, shift)
            decoded_text = base64.b64decode(rot_decoded).decode()
            if decoded_text in check:
                return decoded_text
        except Exception as e:
            continue


#################### IO ####################
from pwn import *

io = remote('lab.scist.org', 31014)

while True:
    try:
        io.recvuntil(b'bot:  ').decode()
        encoded_text = io.recvline().decode().strip()
        print(encoded_text)
        decode_text = decode(encoded_text)
        print(decode_text)
        io.sendline(decode_text.encode())
    except:
        break

io.interactive()
