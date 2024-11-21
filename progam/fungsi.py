# fungsi untuk app.py

def letak_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=========================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")


def kontak_baru():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {"nama": nama, "email": email, "telepon": telepon}
    return kontak


def hapus_kontak(daftar_kontak):
    telepon = input("No telepon yang akan dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = 1
            break

    if index == -1:
        print("Data kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data")


def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yang_dicari.lower()) != -1:
            print("=========================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
