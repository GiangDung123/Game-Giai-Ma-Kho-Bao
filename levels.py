from caesar import caesar_encrypt
from vigenere import vigenere_encrypt
from rsa_module import generate_keys, rsa_encrypt
from aes_module import encrypt as aes_encrypt
from Crypto.Random import get_random_bytes

def get_levels():
    # Tạo cặp khóa RSA và AES key
    pub_key, priv_key = generate_keys()
    aes_key = get_random_bytes(16)

    return [
        {
            'name': 'Caesar Cipher',
            'cipher': caesar_encrypt("Cong cha nhu nui Thai Son", 3),
            'answer': "Cong cha nhu nui Thai Son",
            'type': 'caesar',
            'shift': 3
        },
        {
            'name': 'Vigenère Cipher',
            'cipher': vigenere_encrypt("Uong nuoc nho nguon", "KHOA"),
            'answer': "Uong nuoc nho nguon",
            'type': 'vigenere',
            'keyword': "KHOA"
        },
        {
            'name': 'RSA',
            'cipher': rsa_encrypt(pub_key, "Tich duc de lai doi sau"),
            'answer': "Tich duc de lai doi sau",
            'type': 'rsa',
            'private_key': priv_key
        },
        {
            'name': 'AES',
            'cipher': aes_encrypt("An qua nho ke trong cay", aes_key),
            'answer': "An qua nho ke trong cay",
            'type': 'aes',
            'key': aes_key
        }
    ]
