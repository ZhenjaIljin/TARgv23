#1Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitav sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitav sind Mati! Ma olen N aastat vana.”


#print("Tere maailm!")
 #   nimi = input("Mis sinu nimi on?")
 #   print("Tere, maailm! Tervitan sind{0}!".format(nimi))
 #   vanus=int(input("Kui vana sa oled?"))
  #  print("Tere,maailm! Tervitan sind{0}! Sa oled {1}aastat vana!".format(nimi,vanus))
#2

##a) vanus = 18
#b) eesnimi = "Jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.



# print ("vanus =18")


# print("eesnimi = ""Jaak")

# print( "pikkus =16.5")
# print("kas_kaib_koolis")



#3

#Kirjuta enda mängu koodis laual olevate kommide arv muutujasse. Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
# kommide_arv=int(input("Laual olevate kommide arv : "))
# print("Laua peal on {0}".format(kommide_arv))
# mitu=int(input("Mittu kommi sa soovid süüa: "))
# kommide_arv-=mitu
# print("Nüüd laua peal on ", kommide_arv)

#4

#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

# from math import pi
# C=float(input("ümbermõõt: "))
# d=round(C/pi,2)
# print("Läbimõõt:{0}".format(round(d,2)))
#5.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
from math import hypot
from math import sqrt
from msvcrt import kbhit


# a=float(input("Esimine kaatet"))
# b=float(input("Teine kaatet"))
# d=sqrt(a**2+b**2)
# d1=hypot(a,b)
# print("d=",d)
# print("d1=",d1)
#6
#Leidke järgnevast näiteprogrammist semantiline viga:

# try:
#     aeg = float(input("Mitu tundi kulus sõiduks? "))
#     teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#     kiirus = teepikkus/aeg
#     print("Sinu kiirus oli "+str(kiirus)+"km/h")

# except :
#     print("Andmetetüübi viga!")


#7.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
# print("Sisestage viis täisarvu.")
# num1 = int(input("Sisesta esimene number: "))
# num2 = int(input("Sisesta teine number: "))
# num3 = int(input("Sisesta kolmas number: "))
# num4 = int(input("Sisesta neljas number: "))
# num5 = int(input("Sisesta viies number: "))
# keskmine = (num1 + num2 + num3 + num4 + num5) / 5
# print("Sisestatud numbrite keskmine on: ", keskmine)
#8.
# konn= """
#    @..@
#   (----)
#  ( \__/ )
#  ^^ "" ^^
# """

# print   (konn) 
#9.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
# a=5
# b=7
# c=8
# p=a+b+c
# print (p)
#10.
#Pitsa

 #   Võtsite P sõbraga suure pitsa hinnaga 12,90€
  #  Jätate teenindajale 10% jootraha
   # Koosta programm, mis leiab kui palju peab igaüks maksma

pitsa_hind = 12.90

jootraha_protsent = 10

jootraha = pitsa_hind * (jootraha_protsent / 100)

kogumaksumus = pitsa_hind + jootraha

maksumus_inimese_kohta = kogumaksumus / 2

print("Igaüks peab maksma{0}".format(maksumus_inimese_kohta))