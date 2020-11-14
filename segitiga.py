def soal1(): #piramida
    a = int(input("masukan angka mu cok?"))
    b = 1
    while a > 0:
        a = a- 1
        print(" "*a,"*"*b)
        b = b + 2
def soal2(): #sigitaga sama kaki hadap kanan
    a = int(input("masukan angka lagi sayang?"))
    b = 0
    while 0 < a :
        b = b+1
        print("*"*b)
        a = a - 1
    while b > 0 :
        b = b - 1
        print("*"*b)
def soal3(): #jajarenjang
    a = int(input ("masukan angka meri"))
    b = 1
    while a > 0:
        a = a- 1
        print(" "*a,"*"*b)
        b = b + 2
    b= b - 2
    while b > 0 :
        b = b - 2
        a = a + 1
        print (" "*a,"*"*b)
def soal4(): #lovekamu
    print(" ","*"*4,"","*"*4," ")
    a = 12
    b = 0
    while a > 0:
        print(" "*b,"*"*a)
        a = a - 2
        b = b +1
        
soal1()
soal2()
soal3()
soal4()