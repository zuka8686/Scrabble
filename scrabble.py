vardnica={
    'a' : 1,
    'ā' : 1,
    'b' : 3, 
    'c' : 4,
    'č' : 3,
    'd' : 3, 
    'e' : 1,
    'ē' : 5,
    'f' : 4, 
    'g' : 3,
    'ģ' : 5,
    'h' : 4,
    'i' : 1,
    'ī' : 1,
    'j' : 3, 
    'k' : 2,
    'ķ' : 3,
    'l' : 2, 
    'ļ' : 3,
    'm' : 2,
    'n' : 2, 
    'ņ' : 4,
    'o' : 2,
    'p' : 2,
    'r' : 1,
    's' : 1,
    'š' : 3, 
    't' : 1,
    'u' : 2,
    'ū' : 1, 
    'v' : 3,
    'z' : 2,
    'ž' : 3 
    }

vards = input("Ievadiet savu vārdu: ")

def parbaudit(word):
    summa = 0
    for burts in word:
        if burts in vardnica.keys():
            summa+=vardnica[burts]
    return summa

rezultats = parbaudit(vards)

print(f"Par šo vārdu jums ir {rezultats} punkti")