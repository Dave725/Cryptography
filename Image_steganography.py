import PIL
from PIL import Image

orig = PIL.Image.open('original.png').convert('RGB')
hidden = PIL.Image.open('with hidden message.png').convert('RGB')
width, height = orig.size
with open('Steganography_dec.txt', 'r') as f:
    dec_text = f.read()


def stega(original, text):
    rval, gval, bval, j = [], [], [], 0

    for i in text:
        n = str(ord(i))

        if len(n) == 1:
            bval.append(n)
            rval.append('0')
            gval.append('0')
        elif len(n) == 2:
            bval.append(n[1])
            rval.append('0')
            gval.append(n[0])
        elif len(n) == 3:
            bval.append(n[2])
            rval.append(n[0])
            gval.append(n[1])

    for x in range(width):
        for y in range(height):
            rgb = original.getpixel((x, y))
            r, g, b = rgb[0], rgb[1], rgb[2]
            if r > 246:
                r = 246
            if g > 246:
                g = 246
            if b > 246:
                b = 246
            if j == len(rval):
                return original
            r += int(rval[j])
            g += int(gval[j])
            b += int(bval[j])
            original.putpixel((x, y), (r, g, b))
            j += 1

    return original


hidden_message = stega(orig, dec_text)


def anti_stega(original, crypted):
    finished_text = ''
    for x in range(width):
        for y in range(height):
            rgb1, rgb2 = original.getpixel((x, y)), crypted.getpixel((x, y))
            r1, g1, b1, r2, g2, b2 = rgb1[0], rgb1[1], rgb1[2], rgb2[0], rgb2[1], rgb2[2]
            asc = 100 * (r2 - r1) + 10 * (g2 - g1) + (b2 - b1)
            finished_text += chr(asc)
    return finished_text


print(anti_stega(orig, hidden))
