from Caesar_shift import caesar
import string

alphabet = list(string.ascii_lowercase)
calphabet = list(string.ascii_uppercase)
with open('Vigenere_dec.txt', 'r') as f:
	dec_text = f.read()
with open('Vigenere_enc.txt', 'r') as f:
	enc_text = f.read()

def key_generation(word):
	key = []
	return key

def Vigenere(text, word, decryption = 0):
	key = key_generation(word)
	if decryption:
		key = [26-i for i in key]
	finished_text = caesar(text,key, decryption)
	return finished_text
