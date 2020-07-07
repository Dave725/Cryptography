import string

alphabet = list(string.ascii_lowercase)
calphabet = list(string.ascii_uppercase)
with open('Vigenere_dec.txt', 'r') as f:
    dec_text = f.read()
with open('Vigenere_enc.txt', 'r') as f:
    enc_text = f.read()


def key_generation(length, keyword):
    i = 0
    while True:
        if length == i:
            i = 0
        if len(keyword) == length:
            break
        keyword += keyword[i]
        i += 1
    return keyword.lower()


def Vigenere(text, word, decryption=0):
    keyw = key_generation(len(text), word)
    neg = 1
    finish_text = ''
    if decryption:
        neg = -1
    for i in range(len(text)):
        ind = alphabet.index(keyw[i])
        if text[i] in alphabet:
            finish_text += alphabet[(alphabet.index(text[i]
                                                    ) + ind*neg + 26) % 26]
        elif text[i] in calphabet:
            finish_text += calphabet[(calphabet.index(text[i]
                                                      ) + ind*neg + 26) % 26]
        else:
            finish_text += text[i]

    return finish_text


print(Vigenere(enc_text, 'covid', decryption=1))
