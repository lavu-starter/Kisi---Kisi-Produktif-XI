import tkinter as tk
from tkinter import messagebox

# Pertanyaan tes kejujuran
pertanyaan = [
    "Jika menemukan uang di lantai sekolah, saya akan mengembalikannya ke guru.",
    "Saya bersedia mengakui kesalahan meskipun teman-teman saya tidak tahu.",
    "Jika saya bisa menyontek tanpa ketahuan, saya tetap memilih untuk tidak menyontek.",
    "Saya setuju bahwa mengambil barang milik teman tanpa izin itu salah.",
    "Saya merasa senang saat mendapatkan penghargaan tanpa usaha yang adil."
]

# Nilai jawaban
nilai_jawaban = {
    1: 5,  # Sangat Setuju
    2: 4,  # Setuju
    3: 3,  # Netral
    4: 2,  # Tidak Setuju
    5: 1   # Sangat Tidak Setuju
}

class TesKejujuran:
    def __init__(self, master):
        self.master = master
        self.master.title("Tes Kejujuran Siswa")
        self.master.geometry("600x400")
        self.skor = 0
        self.index = 0
        self.jawaban_var = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text=pertanyaan[self.index], wraplength=550, font=("Arial", 12))
        self.label.pack(pady=20)

        # Radio buttons untuk jawaban
        self.radio_frame = tk.Frame(self.master)
        self.radio_frame.pack(pady=10)
        self.radio_buttons = []
        options = ["1. Sangat Setuju", "2. Setuju", "3. Netral", "4. Tidak Setuju", "5. Sangat Tidak Setuju"]
        for i, text in enumerate(options, 1):
            rb = tk.Radiobutton(self.radio_frame, text=text, variable=self.jawaban_var, value=i, font=("Arial", 11))
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

    def next_question(self):
        jawaban = self.jawaban_var.get()
        if jawaban == 0:
            messagebox.showwarning("Peringatan", "Silakan pilih jawaban terlebih dahulu!")
            return

        # Hitung skor
        if self.index == 4:  # pertanyaan negatif
            self.skor += 6 - nilai_jawaban[jawaban]
        else:
            self.skor += nilai_jawaban[jawaban]

        self.index += 1
        self.jawaban_var.set(0)

        if self.index < len(pertanyaan):
            self.label.config(text=pertanyaan[self.index])
        else:
            self.show_result()

    def show_result(self):
        if self.skor >= 20:
            hasil = "Tingkat kejujuran: Tinggi ✅"
        elif self.skor >= 15:
            hasil = "Tingkat kejujuran: Sedang ⚠️"
        else:
            hasil = "Tingkat kejujuran: Perlu perhatian ❌"

        messagebox.showinfo("Hasil Tes", f"Skor Kejujuran Anda: {self.skor}/25\n{hasil}\n\nCatatan: Tes ini hanya indikator awal.")
        self.master.destroy()

# Jalankan aplikasi
root = tk.Tk()
app = TesKejujuran(root)
root.mainloop()
