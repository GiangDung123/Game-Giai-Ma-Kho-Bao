def vigenere_encrypt(text, keyword):
    result = ""
    keyword = keyword.upper()
    k_len = len(keyword)
    k_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(keyword[k_index % k_len]) - ord('A')
            result += chr((ord(char) - base + k) % 26 + base)
            k_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(cipher_text, keyword):
    result = ""
    keyword = keyword.upper()
    k_len = len(keyword)
    k_index = 0
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(keyword[k_index % k_len]) - ord('A')
            result += chr((ord(char) - base - k) % 26 + base)
            k_index += 1
        else:
            result += char
    return result
