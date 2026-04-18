# Sistem Pakar Diagnosa Penyakit THT

## Deskripsi
Aplikasi ini merupakan sistem pakar berbasis GUI yang digunakan untuk mendiagnosa penyakit THT (Telinga, Hidung, Tenggorokan) berdasarkan gejala yang dipilih oleh pengguna. Sistem akan mencocokkan gejala yang dipilih dengan basis pengetahuan, kemudian menampilkan penyakit dengan tingkat kecocokan tertinggi dalam bentuk persentase.

## Teknologi
- Python
- Tkinter (GUI)

## Metode yang Digunakan
Metode yang digunakan adalah Forward Chaining, yaitu:
- Mengambil input berupa gejala dari pengguna
- Mencocokkan dengan rule pada basis pengetahuan
- Menghitung tingkat kecocokan
- Menampilkan hasil diagnosa

## Fitur Aplikasi
- Menampilkan daftar gejala (G1 – G37)
- Pemilihan gejala menggunakan checkbox
- Tombol diagnosa untuk menentukan penyakit
- Tombol reset untuk mengulang input
- Validasi minimal gejala
- Output berupa nama penyakit dan persentase kecocokan

## Cara Menjalankan
1. Pastikan Python sudah terinstall
2. Jalankan file:
   ```bash
   python main.py

## Contoh Output
Penyakit: Faringitis
Tingkat Kecocokan: 60%

## Identitas
NAMA : BUNGA BUDI AMBAR WATI
NIM : H1D024006
PRAKTIKUM KECERDASAN BUATAN
SHIFT KRS : G
SHIFT SEKARANG : F
