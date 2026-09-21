# 1.a. Une fonction affine peut s'écrire sous la forme f(x) = ax + b
# b. a et b sont des constantes, a est le coefficient directeur et b est l'ordonnée à l'origine.
# c. Lorsque A(1 ; -3) et B(4 ; 3), on peut en déterminer une fonction affine dont la courbe passe par ces deux points. Ici, la fonction est f(x) = 2x + -5.
# d./e./f./g. Pour déterminer l'équation de la droite passant par les points A(xA, yA) et B(xB ; yB), on peut utiliser la formule du coefficient directeur : a = (yB - yA) / (xB - xA). Ensuite, on peut utiliser l'un des points pour trouver b en substituant les valeurs dans l'équation f(x) = ax + b.
# On peut alors en faire un algorithme.
def equation_droite(xA, yA, xB, yB):
    a = int((yB - yA) / (xB - xA))
    b = int(yA - a * xA)
    print("f(x) = " + str(a) + "x + " + str(b))

# 2.a. Une équation du second degré peut s'écrire sous la forme f(x) = ax² + bx + c
# b. les solutions possibles d'une équation du second degré sont données par la formule : x = (-b ± √(b² - 4ac)) / (2a)
# c./d./e.
def resol_eq_second_degre(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        print("Les solutions sont : x1 = " + str(x1) + " et x2 = " + str(x2))
    elif delta == 0:
        x = -b / (2*a)
        print("La solution est : x = " + str(x))
    else:
        print("Il n'y a pas de solution réelle")

resol_eq_second_degre(1, -3, 2)