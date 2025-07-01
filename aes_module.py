from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

BLOCK_SIZE = 16

def pad(text):
    pad_len = BLOCK_SIZE - len(text) % BLOCK_SIZE
    return text + chr(pad_len) * pad_len

def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

def encrypt(plain_text, key_bytes):
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    padded_text = pad(plain_text)
    encrypted = cipher.encrypt(padded_text.encode())
    # Trả về base64 string
    return base64.b64encode(iv + encrypted).decode()

def decrypt(cipher_text, key_bytes):
    data = base64.b64decode(cipher_text)
    iv = data[:16]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data[16:])
    return unpad(decrypted.decode())
