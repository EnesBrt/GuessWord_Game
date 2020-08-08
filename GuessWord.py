""" Python game :
Le but de ce programme est de deviner un mot """

print("Bienvenue sur GuessWord ! Le but du jeu est de deviner les ou le bon mot qui est dans la liste. ")

mot = []

while True :

    try :

        nb = int(input("entez le nombre de mot que vous souhaitez : "))
        break

    except ValueError :

        print("saisissez uniquement des nombres.")


for add in range(nb) :

    while True : 

        try :

            add = input("entrez un mot à deviner : ")
            if add.isalpha():
                break

            
        
        except TypeError :

            print("saisissez uniquement des chaines de charactères")

    mot += [add]

while True :

    print("quel sont les ou le mot contenue dans la liste ?")

    while True :

        try :

            ask = input("taper un mot : ")
            if add.isalpha():
                break
        
           

        except TypeError :

            print("saisissez uniquement des chaines de charactères")

    if ask in mot :
        mot.remove(ask)
        print("bien !")
        num = len(mot)
        print("il reste", num, "mot à trouvé")
        if len(mot) == 0 :
            print("Vous avez deviner tout les mots !")
            break
        
    else :
        
        print("rater ! Recommence.")
        
     

