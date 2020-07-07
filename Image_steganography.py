import PIL

orig = PIL.Image.open('original.png').convert('RGB')
hidden = PIL.Image.open('with hidden message.png').convert('RGB')
width, height = orig.size

def stega (original, text):
	pass

def anti_stega (original, crypted):
	finished_text = ''
	for x in range(width):
		for y in range(height):
			rgb1, rgb2 = original.getpixel((x, y)), crypted.getpixel((x, y))
			r1, g1, b1, r2, g2, b2 = rgb1[0], rgb1[1], rgb1[2], rgb2[0], rgb2[1], rgb2[2]
			asc = 100 * (r2 - r1) + 10 * (g2 - g1) + (b2 - b1)
			finished_text += chr(asc)
	return finished_text
