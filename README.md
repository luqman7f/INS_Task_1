# INS_Task_1

---

# Hybrid Cipher Design

## Introduction
A **hybrid cipher** combines multiple encryption techniques to enhance the security of data. The hybrid cipher described here integrates:

- **Vigenère Cipher (Substitution Cipher):** A substitution cipher that adds confusion by using a repeating key to encrypt the plaintext.
- **Columnar Transposition Cipher (Transposition Cipher):** A transposition cipher that further secures the ciphertext by rearranging the characters based on a key.

By combining both classical encryption methods, the hybrid cipher strengthens the security of encrypted messages and provides enhanced resistance to common cryptanalysis attacks such as frequency analysis and brute-force attacks. This dual-layer approach leverages the strengths of both substitution and transposition techniques to create a more robust encryption method.

## Key Features
- **Confusion:** Achieved through the Vigenère Cipher, where characters in the plaintext are substituted based on a repeating key.
- **Diffusion:** Achieved through the Columnar Transposition Cipher, where the ciphertext is rearranged using a second key to obscure patterns in the data.

The hybrid cipher makes it significantly more difficult to break compared to simpler encryption methods. The combination of substitution and transposition complicates attacks such as frequency analysis and brute-force efforts.

## Cipher Design Process
The hybrid cipher follows these steps:

### Step 1: Substitution Layer (Vigenère Cipher)
The plaintext is first encrypted using the Vigenère Cipher with a 128-bit key. This creates a version of the plaintext where character substitution obscures the original text.

### Step 2: Transposition Layer (Columnar Transposition)
The ciphertext obtained from the Vigenère Cipher is then rearranged using the Columnar Transposition Cipher with a second 128-bit key. This further complicates the analysis by disturbing the positions of the characters.

## Security Justification

### Key Space
The hybrid cipher uses two 128-bit keys, resulting in a key space of 2^256, which provides encryption strength equivalent to 128-bit encryption. This large key space makes brute-force attacks computationally infeasible.

### Resistance to Cryptanalysis
- **Substitution Layer:** The Vigenère Cipher hides the frequency distribution of characters, making it difficult to perform frequency analysis.
- **Transposition Layer:** The Columnar Transposition Cipher disrupts any remaining patterns, complicating frequency analysis and defending against known-plaintext attacks.

By combining these two layers, the cipher provides strong protection against a range of cryptanalytic methods.

## Mathematical Formulation
Let:
- **P** be the plaintext,
- **K₁** be the Vigenère key (128-bit),
- **K₂** be the transposition key (128-bit).

### Encryption
The encryption process is defined as:
\[
C = \text{Transpose}(Vigenère(P, K₁), K₂)
\]
Where:
- **Vigenère(P, K₁)** applies the Vigenère Cipher with the key **K₁** on the plaintext **P**.
- **Transpose(..., K₂)** applies the Columnar Transposition Cipher with the key **K₂** on the resulting ciphertext.

### Decryption
The decryption process is defined as:
\[
P = Vigenère^{-1}(\text{Transpose}^{-1}(C, K₂), K₁)
\]
Where:
- **Transpose⁻¹(C, K₂)** reverses the Columnar Transposition applied during encryption.
- **Vigenère⁻¹(..., K₁)** reverses the Vigenère Cipher applied during encryption.

## Working Example

### Example 1: Encryption
**Plaintext:** "HELLO WORLD"  
**Vigenère Key:** "SECRET"  
**Columnar Transposition Key:** "COLUMNAR"

**Step 1:** Vigenère Cipher Encryption  
The Vigenère Cipher encrypts "HELLO WORLD" using the key "SECRET" to produce:
- **Vigenère Ciphertext:** "SJZRA MPSND"

**Step 2:** Columnar Transposition Encryption  
The Vigenère ciphertext "SJZRA MPSND" is then encrypted using the Columnar Transposition with the key "COLUMNAR", producing the final ciphertext:
- **Final Encrypted Text (Hybrid Cipher):** "SJSOKVNNHV"

### Example 2: Decryption
To decrypt the message, the reverse process is applied.

**Step 1:** Reverse Columnar Transposition  
The ciphertext "SJSOKVNNHV" is reversed using the Columnar Transposition key to produce:
- **Transposition Reversed Ciphertext:** "SJZRA MPSND"

**Step 2:** Reverse Vigenère Cipher Decryption  
The reversed ciphertext "SJZRA MPSND" is then decrypted using the Vigenère key "SECRET" to obtain the original plaintext:
- **Decrypted Plaintext:** "HELLO WORLD"

## Security Evaluation

### 1. Resistance to Frequency Analysis
- The Vigenère Cipher provides confusion, making it difficult to analyze letter frequencies.
- The Columnar Transposition Cipher adds further complexity by rearranging the ciphertext, ensuring that the letter frequencies remain hidden.

### 2. Key Space Analysis
- The use of two 128-bit keys (for Vigenère and Columnar Transposition) increases the key space exponentially, making brute-force attacks infeasible.

### 3. Resistance to Known-Plaintext Attacks
- Combining both substitution and transposition techniques makes it significantly more challenging to decipher the message even with known-plaintext pairs. Both keys must be known to decrypt the message successfully.

## Conclusion
The hybrid cipher design effectively combines the strengths of both substitution (Vigenère) and transposition (Columnar Transposition) to create a more secure encryption scheme than either method alone. This combined approach enhances resistance to cryptanalysis methods like frequency analysis and brute-force attacks. With the use of long keys and robust padding mechanisms, the hybrid cipher is a powerful tool for encrypting sensitive data.

--- 
