from PIL import Image, ImageDraw
import random

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

    fond = Image.open("etoiles_statiques.png")
    etoiles = Image.new('RGBA',(800, 600), (0,0,0,0))
    draw = ImageDraw.Draw(etoiles)

    nbetoiles = random.randint(70, 150)

    while i < nbetoiles:
        etoile.rayon = random.randint(5, 15)
        etoile.x = random.randint(0, 800)
        etoile.y = random.randint(0, 600)
        etoile.r = random.randint(0, 255)
        etoile.g = random.randint(0, 255)
        etoile.b = random.randint(0, 255)
        
        draw.ellipse((
            etoile.x-etoile.rayon, 
            etoile.y-etoile.rayon, 
            etoile.x+etoile.rayon, 
            etoile.y+etoile.rayon), 
            fill=(etoile.r,etoile.g,etoile.b) )

        i = i + 1
    
    composite = Image.alpha_composite(fond, etoiles)
    
    composite.show()




if __name__=="__main__" : 
    etoiles()