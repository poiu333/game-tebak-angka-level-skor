# 🎮 Tebak Angka

Game tebak angka berbasis terminal yang dibuat dengan Python. Setiap level, tantangan makin besar — batas angka dan jumlah kesempatan ikut naik!

---

## Fitur

- Level bertingkat — makin tinggi level, makin lebar range angkanya
- Sistem skor — dapat poin lebih banyak di level tinggi
- Hint otomatis — dikasih tau kalau tebakan terlalu kecil atau terlalu besar
- Validasi input — angka non-numerik tidak akan crash game

---

## Cara Main

```bash
python tebak_angka.py
```

Tidak perlu install library tambahan — hanya pakai modul bawaan Python.

---

## Cara Kerja

| Level | Range Angka | Kesempatan |
|-------|-------------|------------|
| 1     | 1 – 67      | 11         |
| 2     | 1 – 77      | 12         |
| 3     | 1 – 87      | 13         |
| ...   | +10 per level | +1 per level |

**Skor** dihitung dari `10 × level` setiap kali berhasil menebak dengan benar.

---

## Contoh Output

```
gas tebak angka 1-67
masukan angka: 30
kesempatan tersisa: 10
kekecilan
masukan angka: 50
kesempatan tersisa: 9
kebesaran
masukan angka: 40
kesempatan tersisa: 8
hoki! 40 adalah angka yang benar
skor kamu: 10
level 2 - tebak angka baru 1-77!
```

---

## Persyaratan

- Python 3.6 ke atas

---

## Struktur File

```
tebak_angka.py   # file utama, jalankan ini
README.md        # dokumentasi ini
```

---

## Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan belajar.
