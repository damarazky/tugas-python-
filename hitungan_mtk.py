n = 2006
p = 20


def uy():
    print("Ini Hasil Nya Bre....")


while True:
    print("==========")
    print("1. Ditambah menggunakan tanda +")
    print("2. Dikurangi menggunakan tanda -")
    print("3. Dikali menggunakan tanda *")
    print("4. Dibagi menggunakan tanda /")
    print("5. Sisa Bagi menggunakan tanda %")
    print("0. akan menonaktifkan system")

    print("secara default nilai n di akan dihitung dengan nilai p")
    print("==========")

    test = input("Silahkan ketik (+,-,*,/,%) : \n ")

    if test == "+":
        uy()
        print(f"{n + p}")
    elif test == "-":
        uy()
        print(f"{n - p}")
    elif test == "*":
        uy()
        print(f"{n * p}")
    elif test == "/":
        uy()
        print(f"{n / p}")
    elif test == "%":
        uy()
        print(f"{n % p}")
    elif test == "0":
        print("Terimakasih...")
        break
