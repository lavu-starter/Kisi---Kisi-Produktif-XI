import tkinter as tk
from tkinter import messagebox

# =======================
# Soal HOTS Kemandirian Finansial
# =======================
soal = [
    "1. Anda menerima bonus mendadak yang cukup besar. Anda memiliki kebutuhan jangka pendek, utang kecil, dan tujuan tabungan jangka panjang. Bagaimana Anda membagi uang tersebut?",
    "2. Anda ingin membeli gadget terbaru, tapi membeli sekarang akan mengurangi tabungan darurat Anda. Apa yang Anda lakukan?",
    "3. Teman menawarkan peluang investasi dengan janji keuntungan besar tapi risiko tidak jelas. Pilih strategi Anda:",
    "4. Pendapatan tetap tapi sering ada pengeluaran tak terduga. Apa langkah Anda?",
    "5. Modal terbatas, ingin mulai usaha sampingan tapi risiko kehilangan sebagian tabungan ada. Pilihan Anda?",
    "6. Anda sering tergoda belanja online saat stres. Strategi terbaik?",
    "7. Bulanan pengeluaran melebihi pemasukan, dan Anda tidak ingin berutang. Tindakan?",
    "8. Ada opsi investasi aman tapi hasil kecil, atau risiko tinggi tapi peluang besar. Pilihan?",
    "9. Anda merencanakan membeli kendaraan baru, tapi harga naik tiap bulan. Pilihan Anda?",
    "10. Kerja sampingan menjanjikan tambahan penghasilan, tapi bisa mengganggu pekerjaan utama/ kesehatan. Pilihan?"
]

pilihan = [
    ["A. Prioritaskan kebutuhan jangka pendek, sisanya ditabung",
     "B. Bayar utang dulu, sisanya dibagi tabungan dan kebutuhan",
     "C. Membagi rata untuk semua: kebutuhan, utang, tabungan"],

    ["A. Tunda pembelian sampai tabungan darurat cukup",
     "B. Beli sekarang, bisa dicicil",
     "C. Beli sebagian sekarang, sisanya nanti"],

    ["A. Meneliti dan mengevaluasi risiko sebelum memutuskan",
     "B. Mengabaikan saran teman dan tidak berinvestasi",
     "C. Ikut berinvestasi karena janji keuntungan tinggi"],

    ["A. Membuat dana darurat dan menyesuaikan pengeluaran bulanan",
     "B. Mengandalkan pinjaman atau bantuan jika terjadi pengeluaran mendadak",
     "C. Mengurangi tabungan sementara untuk menutup pengeluaran"],

    ["A. Mulai usaha kecil yang aman, evaluasi progres sebelum meningkatkan modal",
     "B. Menunda usaha sampai modal cukup tanpa risiko",
     "C. Gunakan seluruh tabungan untuk memulai usaha"],

    ["A. Menetapkan batas pengeluaran dan membuat daftar kebutuhan",
     "B. Mengizinkan diri belanja sesekali untuk mengurangi stres",
     "C. Menghindari semua belanja online tanpa pengecualian"],

    ["A. Evaluasi dan kurangi pengeluaran tidak penting",
     "B. Cari sumber pendapatan tambahan segera",
     "C. Tetap bayar semua kebutuhan walau akhirnya berutang"],

    ["A. Investasi aman untuk stabilitas jangka panjang",
     "B. Sebagian kecil untuk risiko tinggi, sisanya aman",
     "C. Semua untuk risiko tinggi demi potensi keuntungan besar"],

    ["A. Menunggu sambil menabung lebih banyak agar aman",
     "B. Membeli sekarang karena takut harga naik",
     "C. Cari alternatif kendaraan lebih murah atau cicilan"],

    ["A. Evaluasi risiko dan alokasi waktu sebelum memutuskan",
     "B. Ambil pekerjaan sampingan sepenuhnya untuk tambahan penghasilan",
     "C. Tolak pekerjaan sampingan untuk fokus kesehatan dan pekerjaan utama"]
]

# =======================
# Skor: nilai tertinggi menunjukkan kemandirian finansial lebih baik
# =======================
# Pilihan A biasanya paling mendukung kemandirian finansial, B sedang, C kurang
skor = [
    [2, 3, 1],  # soal 1, A=2, B=3, C=1 → nanti bisa diatur interpretasi
    [2, 1, 1],
    [2, 1, 0],
    [2, 0, 1],
    [2, 1, 0],
    [2, 1, 0],
    [2, 1, 0],
    [2, 1, 0],
    [2, 1, 0],
    [2, 1, 0]
]

# =======================
# GUI Tkinter
# =======================
class KemandirianFinansialGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tes HOTS Kemandirian Finansial")
        self.root.geometry("900x400")

        self.current_index = 0
        self.total_score = 0

        # Label soal
        self.soal_label = tk.Label(root, text="", wraplength=850, font=("Arial", 12))
        self.soal_label.pack(pady=20)

        # Frame tombol pilihan
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack()

        self.current_answer = tk.StringVar(value="")  # kosong awalnya
        self.radio_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(self.frame_buttons, text="", variable=self.current_answer, value=i)
            rb.grid(row=0, column=i, padx=20)
            self.radio_buttons.append(rb)

        # Tombol Start & Next
        self.btn_start = tk.Button(root, text="Start Tes", command=self.start_test)
        self.btn_start.pack(pady=10)

        self.btn_next = tk.Button(root, text="Next", command=self.next_question, state="disabled")
        self.btn_next.pack(pady=10)

        # Label progres
        self.progres_label = tk.Label(root, text="")
        self.progres_label.pack(pady=10)

    def start_test(self):
        self.btn_start.config(state="disabled")
        self.btn_next.config(state="normal")
        self.show_question()

    def show_question(self):
        self.current_answer.set("")
        self.soal_label.config(text=soal[self.current_index])
        for i, rb in enumerate(self.radio_buttons):
            rb.config(text=pilihan[self.current_index][i])
        self.progres_label.config(text=f"Soal {self.current_index + 1} / {len(soal)}")

    def next_question(self):
        answer = self.current_answer.get()
        if answer == "":
            messagebox.showwarning("Peringatan", "Silakan pilih jawaban sebelum lanjut!")
            return

        self.total_score += skor[self.current_index][int(answer)]
        self.current_index += 1

        if self.current_index >= len(soal):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        # Interpretasi sederhana
        if self.total_score >= 18:
            interpretasi = "Tingkat Kemandirian Finansial Tinggi"
        elif self.total_score >= 12:
            interpretasi = "Tingkat Kemandirian Finansial Sedang"
        else:
            interpretasi = "Tingkat Kemandirian Finansial Rendah"

        messagebox.showinfo("Hasil Tes", f"Total Skor: {self.total_score}\n{interpretasi}")
        self.root.destroy()

# =======================
# Jalankan GUI
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    app = KemandirianFinansialGUI(root)
    root.mainloop()
