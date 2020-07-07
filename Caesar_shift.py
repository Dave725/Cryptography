import string

alphabet = list(string.ascii_lowercase)
calphabet = list(string.ascii_uppercase)
with open('Caesar_dec.txt', 'r') as f:
    dec_text = f.read()
with open('Caesar_enc.txt', 'r') as f:
    enc_text = f.read()


def caesar(text, key, decryption=0):
    if decryption:
        key *= -1
    finished_text = ''
    for char in text:
        if char in alphabet:
            finished_text += alphabet[(alphabet.index(char) + key + 26) % 26]
        elif char in calphabet:
            finished_text += calphabet[(calphabet.index(char) + key + 26) % 26]
        else:
            finished_text += char
    return finished_text


def freq_analysis():
    occurence = []
    for char in alphabet:
        count = enc_text.lower.count(char)
        occurence.append(count)
    freq, freqi = 0, 0
    for i, n in enumerate(occurence):
        if n > freq:
            freq = n
            freqi = i
    return alphabet[freqi]


print(caesar(enc_text, 9, decryption=1))
