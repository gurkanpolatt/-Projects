import random
Chars = "asdfghjklşizxcvbnmqwertyuıopASDFGHJKLŞİZXCVBNM123456789!@/*+-$½&()"

password_len = int(input("Şifre kaç karakterli olsun : "))
password_count  = int(input("Kaç adet şifre olsun : "))
for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(Chars)
        password      = password + password_char
    print("Random şifreniz : " , password)
              