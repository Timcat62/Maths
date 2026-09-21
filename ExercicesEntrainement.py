#Exercice 1
from cmath import pi

def volume_cone(r, h):
    print("Le volume du cône est : " + str((1/3) * pi * r**2 * h))
    return (1/3) * pi * r**2 * h


#Exercice 2
def pair_impair(n):
    if n % 2 == 0:
        print("PAIR")
        return "PAIR"
    else:
        print("IMPAIR")
        return "IMPAIR"

#Exercice 3
def combien_divisible_par_2(n):
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    print("Le nombre est divisible par 2, " + str(count) + " fois.")
    return count

#Exercice 4
def hauteurParcourue(nombreMarches, hauteurMarche):
    print("pour " + str(nombreMarches) + " marches de " + str(hauteurMarche) + " cm, il parcourt " + str(5 * 7 * 2 * nombreMarches * hauteurMarche / 100) + " m par semaine.")


#TESTS

volume_cone(3, 5)
pair_impair(4)
combien_divisible_par_2(8)
hauteurParcourue(10, 20)