# projet TKD-Scoring system
# programme jury 2:
# programme : permet au arbitre de saisir les points au cour d'un combat taekwondo
#           : envoyer les resultats saisie par les arbitres sous forme d'un fichier .
head = 3
headRot = 5
fist = 1
body = 2
bodyRot = 3


def switchCases(kick):
    """cette fonction retourne

            Args:
                kick:chaîne carractere (type de frape)

            Retourne:
                pointkick:entier correspond au point marquer.
        """
    if kick == "H":
        pointKick = head
    elif kick == "HR":
        pointKick = headRot
    elif kick == "F":
        pointKick = fist
    elif kick == "B":
        pointKick = body
    elif kick == "BR":
        pointKick = bodyRot
    
    return pointKick
    return kick


def getInfo(player, pointKick):
    """cette fonction retourne  le contenu d'un fichier type ".txt"

                Args:
                    player:carractere type player A ou B
                    pointkick:entier correspond au point marquer

                Retourne:
                    juruinfo :fichier type ".txt" contenent :jurie2 ,type player(A,B) ,pointkick.
            """
    info = "jury_2" + ";" + "player " + player + ";" + str(pointKick)+";"+str(kick)
    juryInf2 = open("juryInf2.txt", "w+")
    juryInf2.write(info)
    juryInf2.close()

    return juryInf2


print("H: pour head \n HR : pour head rotation \n F: pour fist \n B : pour body \n BR : pour body rotation\n ")
kick = input()
if kick.islower():
    kick=kick.upper()
while kick !="H" and kick !="HR" and kick !="F" and kick !="B"and kick !="BR":
    print("voir menu !!!")
    print("H: pour head \n HR : pour head rotation \n F: pour fist \n B : pour body \n BR : pour body rotation\n ")
    kick = input()
    if kick.islower():
        kick=kick.upper()

print("player A or B \n ")
player = input()
if player.islower():
    player=player.upper()
while player !="A" and player !="B":
    print("player A ou B !!!")
    player = input()
    if player.islower():
        player=player.upper()

print(getInfo(player, switchCases(kick)))


