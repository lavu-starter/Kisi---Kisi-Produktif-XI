import tkinter as tk
from tkinter import messagebox

# =======================
# Data Soal dan Skor
# =======================
soal = [
    "1. Saya merasa wajar memanfaatkan kelemahan sistem untuk keuntungan pribadi.",
    "2. Jika teman dekat meminta saya membantu menutupi kesalahan mereka, saya akan melakukannya.",
    "3. Saya selalu merasa perlu memeriksa apakah laporan keuangan orang lain akurat, meskipun bukan tanggung jawab saya.",
    "4. Saya cenderung menyembunyikan informasi penting jika itu menguntungkan saya.",
    "5. Saya percaya bahwa kebaikan kecil dapat dibenarkan meski secara formal salah.",
    "6. Saya akan mempertimbangkan menerima hadiah dari orang yang bisa memengaruhi keputusan saya.",
    "7. Saya mudah tergoda untuk mengubah hasil pekerjaan orang lain demi keuntungan pribadi.",
    "8. Saya berusaha melaporkan perilaku tidak jujur meskipun berisiko bagi hubungan pribadi.",
    "9. Saya percaya bahwa kejujuran lebih penting daripada mendapatkan keuntungan.",
    "10. Saya merasa nyaman memanfaatkan peluang ilegal jika tidak ada yang tahu.",
    "11. Saya sering menilai motif orang lain sebelum mempercayai informasi mereka.",
    "12. Saya mampu menahan diri dari godaan untuk mengambil hal yang bukan hak saya.",
    "13. Saya percaya bahwa memanipulasi fakta untuk terlihat lebih baik bisa diterima.",
    "14. Saya sering merasa cemas jika orang lain mengetahui kesalahan kecil saya.",
    "15. Saya percaya bahwa integritas diri lebih penting daripada keuntungan sementara.",
    "16. Saya sering menutupi kesalahan kecil agar reputasi saya tetap baik.",
    "17. Saya cenderung memikirkan konsekuensi jangka panjang dari tindakan saya.",
    "18. Saya bersedia menolak tawaran yang menguntungkan jika ada unsur ketidakjujuran.",
    "19. Saya kadang merasa bahwa 'sedikit berbohong' tidak berbahaya.",
    "20. Saya sering mengevaluasi diri sendiri untuk memastikan tindakan saya adil.",
    "21. Saya merasa bersalah jika memanfaatkan kesalahan orang lain untuk keuntungan.",
    "22. Saya percaya bahwa aturan harus diikuti meskipun tidak ada yang mengawasi.",
    "23. Saya mudah mengabaikan aturan jika saya merasa tidak ada yang dirugikan.",
    "24. Saya sering memikirkan dampak sosial dari setiap keputusan saya.",
    "25. Saya percaya bahwa menahan informasi yang bisa merugikan orang lain adalah salah.",
    "26. Saya merasa sulit mengatakan 'tidak' pada permintaan teman meski salah.",
    "27. Saya mengutamakan keadilan dan kebenaran dalam tindakan sehari-hari.",
    "28. Saya percaya bahwa setiap orang memiliki tanggung jawab atas kejujuran mereka sendiri.",
    "29. Saya cenderung memanfaatkan situasi ambigu demi keuntungan pribadi.",
    "30. Saya selalu mencoba bertindak dengan integritas, meskipun tidak ada yang melihat."
]

reverse_items = [1,2,4,5,6,7,10,13,16,19,23,29]  # indeks dimulai 0

# =======================
# Fungsi Skor
# =======================
def get_score(jawaban, index):
    if index in reverse_items:
        if jawaban == 'S':
            return 0
        elif jawaban == 'N':
            return 1
        else:  # TS
            return 2
    else:
        if jawaban == 'S':
            return 2
        elif jawaban == 'N':
            return 1
        else:  # TS
            return 0

# =======================
# GUI Tkinter
# =======================
class TesKejujuranGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tes Kejujuran HOTS 30 Butir")
        self.root.geometry("800x300")

        self.current_index = 0
        self.total_score = 0
        self.answers = [tk.StringVar() for _ in range(len(soal))]

        self.soal_label = tk.Label(root, text=soal[self.current_index], wraplength=750, font=("Arial", 12))
        self.soal_label.pack(pady=20)

        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack()

        self.btn_s = tk.Radiobutton(self.frame_buttons, text="Setuju (S)", variable=self.answers[self.current_index], value="S")
        self.btn_s.grid(row=0, column=0, padx=10)
        self.btn_n = tk.Radiobutton(self.frame_buttons, text="Netral (N)", variable=self.answers[self.current_index], value="N")
        self.btn_n.grid(row=0, column=1, padx=10)
        self.btn_ts = tk.Radiobutton(self.frame_buttons, text="Tidak Setuju (TS)", variable=self.answers[self.current_index], value="TS")
        self.btn_ts.grid(row=0, column=2, padx=10)

        self.btn_next = tk.Button(root, text="Next", command=self.next_question)
        self.btn_next.pack(pady=20)

    def next_question(self):
        jawaban = self.answers[self.current_index].get()
        if jawaban == "":
            messagebox.showwarning("Peringatan", "Silakan pilih jawaban sebelum lanjut!")
            return

        # Tambahkan skor
        self.total_score += get_score(jawaban, self.current_index)

        self.current_index += 1
        if self.current_index >= len(soal):
            self.show_result()
            return

        # Update label soal
        self.soal_label.config(text=soal[self.current_index])

        # Update radiobutton variable
        self.btn_s.config(variable=self.answers[self.current_index])
        self.btn_n.config(variable=self.answers[self.current_index])
        self.btn_ts.config(variable=self.answers[self.current_index])

    def show_result(self):
        # Interpretasi
        if self.total_score >= 50:
            interpretasi = "Kecenderungan Integritas Tinggi"
        elif self.total_score >= 35:
            interpretasi = "Kecenderungan Integritas Sedang"
        else:
            interpretasi = "Ada Kecenderungan Risiko Sifat Koruptif"

        messagebox.showinfo("Hasil Tes", f"Total Skor: {self.total_score} dari 60\n{interpretasi}")
        self.root.destroy()

# =======================
# Jalankan GUI
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    app = TesKejujuranGUI(root)
    root.mainloop()
