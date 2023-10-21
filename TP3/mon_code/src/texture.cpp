#include <math.h>
#include "texture.hpp"

#include <iostream>
using namespace std;



RVB Damier::getColor(Point3D p, float u, float v){
	float taille_carre = 2;

    int i = (floor(u / taille_carre));
    int j = (floor(v / taille_carre));

    if ((i + j) % 2 == 0) {
        return RVB(0, 0, 0);
    }
    else {
        return RVB(1, 1, 1);
    }
}

inline int calcul_modulo(int i, int n) {
    return (n + (i % n)) % n;
}

RVB Bitmap::getColor(Point3D p, float u, float v){

    float calculU = calcul_modulo(static_cast<int>(u / scale * map.Largeur()), map.Largeur());
    float calculV = calcul_modulo(static_cast<int>(v / scale * map.Hauteur()), map.Hauteur());

    RVB color = map.MapRVB(calculU, calculV);

    return color;
}




RVB Color::getColor(Point3D p, float u, float v){
	return objet->Couleur();
}