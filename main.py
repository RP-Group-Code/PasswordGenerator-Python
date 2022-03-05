import random

# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*(':;)_-+=|"

while 1:
    kata = input("Masukan Password Yang Diinginkan : ")
    panjang_pass = kata.count("")
    hitung_pass = int(input("Berapa Jumlah Password Yang Anda Inginkan? = "))
    for x in range(0, hitung_pass):
        password = ""
        password_char = random.choice(kata)
        password = password + password_char
        for x in range(0,panjang_pass):
            password_char = random.choice(kata)
            password      = password + password_char
        print("Pasword Anda : ", password)
