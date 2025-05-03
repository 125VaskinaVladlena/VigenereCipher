import unittest
from VigenereCipher import VigenereCipher

class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("LEMON")
    
    def test_encrypt(self):
        plaintext = "ATTACKATDAWN"
        expected_ciphertext = "LXFOPVEFRNHR"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)
    
    def test_decrypt(self):
        ciphertext = "LXFOPVEFRNHR"
        expected_plaintext = "ATTACKATDAWN"
        self.assertEqual(self.cipher.decrypt(ciphertext), expected_plaintext)

    def test_ignore_non_alpha(self):
        plaintext = "Attack at dawn! 123"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_key_shorter_than_text(self):
        cipher2 = VigenereCipher("KEY")
        plaintext = "HELLOWORLD"
        ciphertext = cipher2.encrypt(plaintext)
        decrypted = cipher2.decrypt(ciphertext)
        self.assertEqual(decrypted, "HELLOWORLD")

if __name__ == "__main__":
    unittest.main()