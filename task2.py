from PIL import Image

KEY = 111

img = Image.open("img.png")
pixels = img.load()
width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        r = r ^ KEY
        g = g ^ KEY
        b = b ^ KEY
        pixels[x, y] = (r, g, b)
      
img.save("new-img.png")
print("Done!")
