# program manajemen kontak

import fungsi

daftar_kontak = []
daftar_kontak.append(
    {
        "nama": "Damar Azky",
        "email": "damarazky@gmail.com",
        "telepon": "0821146173...",
    }
)


# menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        fungsi.letak_kontak(daftar_kontak)

    elif menu == "2":
        kontak = fungsi.kontak_baru()
        daftar_kontak.append(kontak)

    elif menu == "3":
        fungsi.hapus_kontak(daftar_kontak)

    elif menu == "4":
        fungsi.cari_kontak(daftar_kontak)

    else:
        print("Menu tidak tersedia")


print("program selesai berjalan, sampai jumpa")
