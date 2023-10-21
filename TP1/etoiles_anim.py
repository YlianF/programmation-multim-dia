from PIL import Image, ImageDraw
import random
import math

class Etoile:
    r: int
    g: int
    b: int
    x: int
    y: int
    rayon: int
    orientation: int


def etoiles():
    i: int = 0
    j: int = 0
    k: int = 0
    
    etoilestab: list = []

    etoiles = Image.new('RGBA',(1920, 1080), (0,0,0,0))
    draw = ImageDraw.Draw(etoiles)

    nbetoilespremierplan = random.randint(100, 150)
    nbetoilesarriereplan = random.randint(300, 350)

    # génération des étoiles a l'arriere plan
    while j < nbetoilesarriereplan:
        etoile = Etoile()

        etoile.orientation = random.choice([-1, 1])
        etoile.rayon = random.randint(1, 3)
        etoile.x = random.randint(0, 1920)
        etoile.y = random.randint(0, 1080)
        etoile.r = random.randint(100, 255)
        etoile.g = random.randint(100, 255)
        etoile.b = random.randint(100, 255)

        etoilestab.append(etoile)
        
        j = j + 1

    # génération des étoiles au premier plan
    while i < nbetoilespremierplan:
        etoile = Etoile()

        etoile.orientation = random.choice([-1, 1])
        etoile.rayon = random.randint(6, 15)
        etoile.x = random.randint(0, 1920)
        etoile.y = random.randint(0, 1080)
        etoile.r = random.randint(100, 255)
        etoile.g = random.randint(100, 255)
        etoile.b = random.randint(100, 255)

        etoilestab.append(etoile)
        
        i = i + 1


    #dessin de chaque frames
    while k < 80:
        etoiles = Image.new('RGBA',(1920, 1080), (0,0,0,0))
        draw = ImageDraw.Draw(etoiles)

        motion = k % 40
        if motion == 0:
            motion = 1

        motion = 1.3 * math.exp(-((motion-20)**2 / 100))


        for etoile in etoilestab:

            # mouvement : monte ou descend
            if (k//40) % 2 == 1 :
                etoile.y = etoile.y + etoile.orientation * etoile.rayon * motion
            else :
                etoile.y = etoile.y - etoile.orientation * etoile.rayon * motion

            draw.ellipse((
                etoile.x-etoile.rayon, 
                etoile.y-etoile.rayon, 
                etoile.x+etoile.rayon, 
                etoile.y+etoile.rayon), 
                fill=(etoile.r,etoile.g,etoile.b),
                outline=(etoile.r + 30,etoile.g + 30,etoile.b + 30),
                width=etoile.rayon//4)
        
        etoiles.save("./etoiles/etoiles" + str(k) + ".png") 
        k = k + 1
    
    etoiles.show()




if __name__=="__main__" : 
    etoiles()

# ffmpeg -framerate 25 -i etoiles%d.png -pix_fmt bgr8 etoiles.gif