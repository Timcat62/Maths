# a. Une fonction affine peut s'écrire sous la forme f(x) = ax + b
# b. a et b sont des constantes, a est le coefficient directeur et b est l'ordonnée à l'origine.
# c. Lorsque A(1 ; -3) et B(4 ; 3), on peut en déterminer une fonction affine dont la courbe passe par ces deux points. Ici, la fonction est f(x) = 2x + -5.
# d./e./f./g. Pour déterminer l'équation de la droite passant par les points A(xA, yA) et B(xB ; yB), on peut utiliser la formule du coefficient directeur : a = (yB - yA) / (xB - xA). Ensuite, on peut utiliser l'un des points pour trouver b en substituant les valeurs dans l'équation f(x) = ax + b.
# On peut alors en faire un algorithme.
def equation_droite(xA, yA, xB, yB):
    a = int((yB - yA) / (xB - xA))
    b = int(yA - a * xA)
    print("f(x) = " + str(a) + "x + " + str(b))

