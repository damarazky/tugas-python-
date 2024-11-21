print("menurutmu saya sekarang jomblo apa tidak ? \n")

print("iya apa tidak ?")

n = input().lower()

t = True
f = False


def jawaban(jomblo):
    if jomblo:
        print("iyaa nih jomblo, kok tau yaa")
    else:
        print("salahhh, saya jomblo wehh")


if n == "iya":
    jawaban(t)
elif n == "tidak":
    jawaban(f)