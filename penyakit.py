import tkinter as tk
from tkinter import messagebox

# DATA GEJALA
gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

# RULE PENYAKIT 
penyakit = {
    "Tonsilitis": ["G37","G12","G5","G27","G6","G21"],
    "Sinusitis Maksilaris": ["G37","G12","G27","G17","G33","G36","G29"],
    "Sinusitis Frontalis": ["G37","G12","G27","G17","G33","G36","G21","G26"],
    "Sinusitis Edmoidalis": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
    "Sinusitis Sfenoidalis": ["G37","G12","G27","G17","G33","G36","G29","G7"],
    "Abses Peritonsiler": ["G37","G12","G6","G15","G2","G29","G10"],
    "Faringitis": ["G37","G5","G6","G7","G15"],
    "Kanker Laring": ["G5","G27","G6","G15","G2","G19","G1"],
    "Deviasi Septum": ["G37","G17","G20","G8","G18","G25"],
    "Laringitis": ["G37","G5","G15","G16","G32"],
    "Kanker Leher & Kepala": ["G5","G22","G8","G28","G3","G11"],
    "Otitis Media Akut": ["G37","G20","G35","G31"],
    "Contact Ulcers": ["G5","G2"],
    "Abses Parafaringeal": ["G5","G16"],
    "Barotitis Media": ["G12","G20"],
    "Kanker Nafasoring": ["G17","G8"],
    "Kanker Tonsil": ["G6","G29"],
    "Neuronitis Vestibularis": ["G35","G24"],
    "Meniere": ["G20","G35","G14","G4"],
    "Tumor Syaraf Pendengaran": ["G12","G34","G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34","G9"],
    "Vertigo Postular": ["G24"]
}

# INISIALISASI GUI 
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit THT")
root.geometry("620x600")

# JUDUL APLIKASI
tk.Label(root, text="SISTEM PAKAR DIAGNOSA PENYAKIT THT",
         font=("Arial", 14, "bold")).pack(pady=10)

# FRAMEE SCROLL
frame_canvas = tk.Frame(root)
frame_canvas.pack(fill="both", expand=True)

canvas = tk.Canvas(frame_canvas)
scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

#KONFIGURASI SCROLL 
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#CHECKBOX GEJALA
check_vars = {}

tk.Label(scrollable_frame, text="Pilih Gejala:",
         font=("Arial", 12, "bold")).pack(anchor="w")

for kode, nama in gejala.items():
    var = tk.IntVar()
    tk.Checkbutton(scrollable_frame, text=f"{kode} - {nama}",
                   variable=var).pack(anchor="w")
    check_vars[kode] = var

# FUNGSI DIIAGNOSA
def diagnosa():
    dipilih = [k for k, v in check_vars.items() if v.get() == 1]

    # Validasi minimal gejala
    if len(dipilih) < 2:
        messagebox.showwarning("Peringatan", "Pilih minimal 2 gejala!")
        return

    hasil = {}
    for nama_penyakit, rule in penyakit.items():
        cocok = sum(1 for g in rule if g in dipilih)
        hasil[nama_penyakit] = cocok / len(rule)

    terbaik = max(hasil, key=hasil.get)
    nilai_terbaik = hasil[terbaik]

    # Validasi minimal kecocokan
    if nilai_terbaik < 0.5:
        messagebox.showinfo("Hasil Diagnosa", "Gejala tidak cukup untuk menentukan penyakit.")
        return

    messagebox.showinfo(
        "Hasil Diagnosa",
        f"Penyakit: {terbaik}\nTingkat Kecocokan: {int(nilai_terbaik*100)}%"
    )

# FUGSI RESET
def reset():
    for var in check_vars.values():
        var.set(0)
frame_tombol = tk.Frame(root)
frame_tombol.pack(pady=10)

# FRAME TOMBOL
tk.Button(frame_tombol, text="Reset", bg="red", fg="white",
          command=reset).pack(side="left", padx=10)

tk.Button(frame_tombol, text="Diagnosa", bg="green", fg="white",
          command=diagnosa).pack(side="left", padx=10)

# JALANKAN APLIKASI
root.mainloop()