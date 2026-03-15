import random

def tebak_angka():
    level = 1
    max_angka = 67
    secret_number = random.randint(1, max_angka)
    nyoba = 10 + level
    skor = 0

    print("gas tebak angka 1-67")

    while True:
        try:
            tebakan = int(input("masukan angka: "))
            nyoba -= 1
            print(f"kesempatan tersisa: {nyoba}")

            if nyoba == 0 and tebakan != secret_number:
                print(f"maaf kesempatan habis, angka yang benar adalah {secret_number}")
                break

            if tebakan < secret_number:
                print("kekecilan")
            elif tebakan > secret_number:
                print("kebesaran")
            else:
                print(f"hoki! {secret_number} adalah angka yang benar")
                skor += 10 * level
                print(f"skor kamu: {skor}")
                level += 1
                max_angka = 67 + (level - 1) * 10
                secret_number = random.randint(1, max_angka)
                nyoba = 10 + level
                print(f"level {level} - tebak angka baru 1-{max_angka}!")

        except ValueError:
            print("input tidak valid, coba lagi")

if __name__ == "__main__":
    tebak_angka()