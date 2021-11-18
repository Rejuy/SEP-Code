# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import random


class Aescrypt():
    def __init__(self, key):
        self.key = self.add16(key)

    def add16(self, par):
        if type(par) == str:
            par = par.encode()
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def encode(self, text):
        text = self.add16(text)
        self.aes = AES.new(self.key, AES.MODE_ECB)
        self.encrypt_text = self.aes.encrypt(text)
        return base64.encodebytes(self.encrypt_text).decode().strip()

    def decode(self, text):
        text = base64.decodebytes(text.encode())
        self.aes = AES.new(self.key, AES.MODE_ECB)
        self.decrypt_text = self.aes.decrypt(text)
        self.decrypt_text = self.decrypt_text.strip(b"\x00")
        return self.decrypt_text.decode()


passwd = "109486109286019284609"
coder = Aescrypt(passwd)

if __name__ == '__main__':
    flag = True
    k = 2
    if k == 1:
        for i in range(10000):
            t = str(i)
            print("======")
            print("Original text", t)
            en_text = coder.encode(t)
            print("Encode: ", en_text)
            de_text = coder.decode(en_text)
            print("Decode ", de_text)
            if t != de_text:
                flag = False
                break
        print(flag)
    elif k == 2:
        for i in range(100):
            string = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 24))
            de_text = coder.decode(string)
            print("Decode", de_text)
