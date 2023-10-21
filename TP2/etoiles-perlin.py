from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import random
from perlin_noise import PerlinNoise

class Etoile:
    r: int
    g: int
    b: int
    x: int
    y: int
    rayon: int


def etoiles():
    i: int = 0
    etoile = Etoile()


    noise = PerlinNoise(octaves=1, seed=1412)

    etoiles = Image.new('RGBA',(800, 600), (0,0,0,0))
    (largeur, longueur) = etoiles.size

    for x in range(largeur) :
        for y in range(longueur) :
            noisepix = noise([x/largeur, y/longueur]) + 1
            r = int((noisepix) * 10)
            g = int((noisepix) * 10)
            b = int((noisepix) * 50)
            etoiles.putpixel((x,y), (r, g, b))


    draw = ImageDraw.Draw(etoiles)
    nbetoiles = random.randint(200, 250)

    while i < nbetoiles:
        etoile.rayon = random.randint(1, 3)
        etoile.x = random.randint(0, 800)
        etoile.y = random.randint(0, 600)
        etoile.r = 175
        etoile.g = 175
        etoile.b = 175
        
        draw.ellipse((
            etoile.x-etoile.rayon, 
            etoile.y-etoile.rayon, 
            etoile.x+etoile.rayon, 
            etoile.y+etoile.rayon), 
            fill=(etoile.r,etoile.g,etoile.b) )

        i = i + 1
    
    
    etoiles.show()




if __name__=="__main__" : 
    etoiles()

