
# a=float(input("alpha"))
# b=float(input("betta"))
# c=float(input("gamma"))

# if a>0 and b>0 and c>0:
#     if a+b+c==180:
#         print("kolmnurk")
#     else:
#         print("nurgad")
# else:
#     print ("andmed ei ole oiged")


#kalkulaator



# try:
#     a=float(input("esimene arv"))
# except :
#     print("vale andmetuup")
    
# t=input("tehe")
# try:
#    b=float(input("teine arv"))
# except :
#     print("vale andmetuup")
# if t in ['+','-','/','*','**','%','//']:#''=""
#     pass
# else:
#     print("tundmatu mark")
#     try:
        



# try:
#     a = float(input("Esimene arv: "))
# except ValueError:
#     print("Vale andmete tuup")
# else:
#     t = input("Tehe: ")

#     try:
#         b = float(input("Teine arv: "))
#     except ValueError:
#         print("Vale andmete tuup")
#     else:
        
#         tulemus = "Tundmatu tehe"
#         if t == '+': tulemus = a + b
#         if t == '-': tulemus = a - b
#         if t == '*': tulemus = a * b
#         if t == '/': tulemus = a / b if b != 0 else "Jagamine nulliga pole lubatud"
#         if t == '//': tulemus = a // b if b != 0 else "Jagamine nulliga pole lubatud"
#         if t == '**': tulemus = a ** b
#         if t == '%': tulemus = a % b

#         print("Tulemus: ", tulemus)


#   TOETUS!


# grupp = input("Ruhma nimetus")
# if grupp == "TARgv23":
#     puudumised = int(input("Mittu puudumist sul on?"))
#     if puudumised < 15:
#         hinne = float(input("Mis on su keskmine hinne? Kirjuta ainult numbrit."))
#         if hinne > 3.8:
#             print("Toetus!")
#         else:
#             print("Liiga madal keskmine hinne. Toetust ei ole!")
#     else:
#         print("Toetust ei maaratakse")
        
# else:
#     print("Ruhma nimetus ei sobi")



#3. Имеется кусок ткани длиной М метров.
# От него последовательно отрезаются куски разной длины.
#  Все данные по использованию ткани заносятся в компьютер.
# Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется.



#Tekstiili müük



# m = 1000

# print("Meil on 1000 meetrit kangast.")

# while m > 0:
#     try:
#         lõikepikkus = float(input("Sisestage lõigatava kanga pikkus: "))
#         if lõikepikkus <= m:
#             m -= lõikepikkus
#             print(f"Järele jäi {m} meetrit kangast.")
#         else:
#             print("Materjali ei ole piisavalt, palun sisestage väiksem pikkus.")
#     except ValueError:
#         print("Palun sisestage numbriline väärtus pikkuse jaoks.")
