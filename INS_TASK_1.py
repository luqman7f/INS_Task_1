# Vigenère Cipher (Substitution)
def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces for encryption
    
    key_index = 0
    for char in plaintext:
        if char in alphabet:
            char_index = alphabet.find(char)
            key_char = key[key_index % len(key)]
            key_index_value = alphabet.find(key_char)
            new_index = (char_index + key_index_value) % len(alphabet)
            ciphertext += alphabet[new_index]
            key_index += 1
        else:
            ciphertext += char  # Non-alphabet characters are not encrypted
    
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    
    key_index = 0
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.find(char)
            key_char = key[key_index % len(key)]
            key_index_value = alphabet.find(key_char)
            new_index = (char_index - key_index_value) % len(alphabet)
            plaintext += alphabet[new_index]
            key_index += 1
        else:
            plaintext += char  # Non-alphabet characters are not decrypted
    
    return plaintext


# Columnar Transposition Cipher (Transposition)
def columnar_transposition_encrypt(plaintext, key):
    # Removing spaces and capitalizing the plaintext
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    # Create a dictionary with key as column index
    sorted_key = sorted(list(set(key)), key=lambda x: key.index(x))
    columns = {char: [] for char in sorted_key}

    # Fill columns with plaintext
    index = 0
    for char in plaintext:
        columns[sorted_key[index % len(sorted_key)]].append(char)
        index += 1
    
    # Construct the ciphertext by reading columns
    ciphertext = "".join("".join(columns[char]) for char in sorted_key)
    
    return ciphertext


def columnar_transposition_decrypt(ciphertext, key):
    # Remove spaces and capitalize
    key = key.upper()
    sorted_key = sorted(list(set(key)), key=lambda x: key.index(x))
    num_columns = len(sorted_key)
    num_rows = len(ciphertext) // num_columns
    
    # Create a 2D array to hold the ciphertext
    matrix = [''] * num_rows
    index = 0
    for char in ciphertext:
        matrix[index % num_rows] += char
        index += 1
    
    # Reconstruct the plaintext from the matrix
    plaintext = "".join("".join(matrix[i]) for i in range(num_rows))
    
    return plaintext


# Hybrid Cipher (Vigenère + Columnar Transposition)
def hybrid_encrypt(plaintext, key1, key2):
    # Apply Vigenère Cipher (Substitution)
    vigenere_encrypted = vigenere_encrypt(plaintext, key1)
    
    # Apply Columnar Transposition Cipher (Transposition)
    final_encrypted = columnar_transposition_encrypt(vigenere_encrypted, key2)
    
    return final_encrypted


def hybrid_decrypt(ciphertext, key1, key2):
    # Apply Reverse Columnar Transposition Cipher
    transposition_decrypted = columnar_transposition_decrypt(ciphertext, key2)
    
    # Apply Reverse Vigenère Cipher (Substitution)
    final_decrypted = vigenere_decrypt(transposition_decrypted, key1)
    
    return final_decrypted


# Test Example
plaintext = "HELLO WORLD"
key1 = "SECRET"
key2 = "COLUMNAR"

# Encrypt the plaintext
encrypted_text = hybrid_encrypt(plaintext, key1, key2)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the ciphertext back to plaintext
decrypted_text = hybrid_decrypt(encrypted_text, key1, key2)
print(f"Decrypted Text: {decrypted_text}")
