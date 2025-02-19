alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_autokey(keyword: str, plaintext: str) -> str:
    """Generates the autokey by appending the plaintext to the keyword."""
    new_plaintext = ''
    for c in plaintext:
        if c in alphabet:
            new_plaintext += c
        else:
            new_plaintext += c
    return (keyword + new_plaintext)[:len(new_plaintext)]

def encrypt_autokey(plaintext: str, keyword: str) -> str:
    """Encrypts a message using the Autokey Cipher."""
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()
    autokey = generate_autokey(keyword, plaintext)
    
    ciphertext = ''
    p = 0
    k = 0
    while p < len(plaintext):
        if plaintext[p] not in alphabet:
            ciphertext += plaintext[p]
            p += 1
        if p >= len(plaintext):
            break
        if autokey[k] not in alphabet:
            k += 1
        new_index = (alphabet.index(plaintext[p]) + alphabet.index(autokey[k])) % 26
        ciphertext += alphabet[new_index]
        p += 1
        k += 1
    
    print(ciphertext)
    return ciphertext

def decrypt_autokey(ciphertext: str, keyword: str) -> str:
    """Decrypts a message encrypted with the Autokey Cipher."""
    keyword = keyword.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    
    plaintext = ''
    autokey = keyword  # Initially, autokey starts as just the keyword
    
    c = 0
    k = 0
    while c < len(ciphertext):
        if ciphertext[c] not in alphabet:
            plaintext += ciphertext[c]
            c += 1
        if c >= len(ciphertext):
            break
        if autokey[k % len(autokey)] not in alphabet:
            k += 1
        p_index = (alphabet.index(ciphertext[c]) - alphabet.index(autokey[k % len(autokey)])) % 26
        plaintext_char = alphabet[p_index]
        plaintext += plaintext_char
        autokey += plaintext_char  # Extend autokey with recovered plaintext
        k += 1
        c += 1
    
    return plaintext

# Example usage:
plaintext = "bbctf{DOYOUTHINKBIGBROTHERISLISTENING}"
keyword = "free"
ciphertext = encrypt_autokey(plaintext, keyword)
decrypted_text = decrypt_autokey(ciphertext, keyword)

print("Plaintext:", plaintext)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)

