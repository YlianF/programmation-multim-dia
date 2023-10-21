import math
from PIL import Image
from random import randint
from perlin_noise import PerlinNoise

if __name__=="__main__" : 

    compt: float = 1
    coef: float = 1

    largeur : int = 500
    longueur : int = 500

    noise = PerlinNoise(octaves=5, seed=1412)

    while compt < 2 :
        img = Image.new('RGBA', (500,500), (0,0,0,0)) 
        for x in range(largeur) :
            for y in range(longueur) :
                noisepix = 1 # (noise([ x/largeur, y/longueur ]) + 0.5) * coef
                r = 255 - int(math.sin((y / 50 + x / 50) * noisepix))
                g = 255 - int(math.sin((y / 50 + x / 50) * noisepix) * 200)
                b = 255 - int(math.sin((y / 50 + x / 50) * noisepix) * 255)
                img.putpixel((x, y), (r, g, b))

        img.save("./perlin/perlin" + str(compt) + ".png")
        coef = coef + 0.2
        compt = compt + 1

    img.show()

# ffmpeg -framerate 25 -i perlin%d.png -pix_fmt bgr8 perlin.gif