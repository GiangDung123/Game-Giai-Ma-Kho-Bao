from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def rsa_encrypt(public_key_bytes, plaintext):
    public_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_bytes = cipher.encrypt(plaintext.encode())
    # Base64 encode để lưu trữ dễ dàng
    return base64.b64encode(encrypted_bytes).decode()

def rsa_decrypt(private_key_bytes, cipher_text_b64):
    private_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_bytes = cipher.decrypt(base64.b64decode(cipher_text_b64))
    return decrypted_bytes.decode()
