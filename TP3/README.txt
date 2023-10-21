créer l'image docker : 
docker load -i export_image/image

instancier l'image : 
docker run -it -v C:/[chemin]/TP3/mon_code:/code image-cpp

générer l'image (se placer dans le container, dans /code/) : 
make tex
./tex


docker exec -it gracious_pasteur /bin/bash