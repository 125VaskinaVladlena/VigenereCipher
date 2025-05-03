class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet_size = len(self.alphabet)
    
    def _format_text(self, text):
        return ''.join([c for c in text.upper() if c in self.alphabet])
    
    def _generate_full_key(self, text):
        key = self.key
        full_key = (key * (len(text) // len(key) + 1))[:len(text)]
        return full_key

    def encrypt(self, plaintext):
        plaintext = self._format_text(plaintext)
        full_key = self._generate_full_key(plaintext)
        
        ciphertext = []
        for p, k in zip(plaintext, full_key):
            p_index = self.alphabet.index(p)
            k_index = self.alphabet.index(k)
            c_index = (p_index + k_index) % self.alphabet_size
            ciphertext.append(self.alphabet[c_index])
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):
        ciphertext = self._format_text(ciphertext)
        full_key = self._generate_full_key(ciphertext)
        
        plaintext = []
        for c, k in zip(ciphertext, full_key):
            c_index = self.alphabet.index(c)
            k_index = self.alphabet.index(k)
            p_index = (c_index - k_index + self.alphabet_size) % self.alphabet_size
            plaintext.append(self.alphabet[p_index])
        return ''.join(plaintext)