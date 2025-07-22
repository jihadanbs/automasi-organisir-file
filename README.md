"# automasi-organisir-file"

# Pengorganisir File Otomatis dengan Python 📂

Sebuah skrip Python sederhana untuk merapikan folder yang berantakan secara otomatis dengan memindahkan file ke dalam sub-folder berdasarkan kategorinya (Gambar, Dokumen, Video, dll).

Proyek ini dibuat sebagai contoh program automasi level pemula yang praktis dan mudah dipahami.

---

## ✨ Fitur

- **Klasifikasi Otomatis**: Mengidentifikasi tipe file berdasarkan ekstensinya (e.g., `.jpg`, `.pdf`, `.mp3`).
- **Pembuatan Folder Dinamis**: Secara otomatis membuat folder kategori (`Gambar`, `Dokumen`, `Video`, dll.) jika belum ada.
- **Dukungan Berbagai Tipe File**: Mengorganisir gambar, dokumen, video, musik, dan arsip. File yang tidak dikenali akan dimasukkan ke folder `Lainnya`.
- **Mudah Dikonfigurasi**: Cukup ubah satu variabel untuk menargetkan folder mana pun yang ingin dirapikan.
- **Tanpa Dependensi Eksternal**: Hanya menggunakan library standar Python (`os` dan `shutil`), tidak perlu instalasi tambahan.

---

## 🚀 Cara Penggunaan

Ikuti langkah-langkah berikut untuk menjalankan skrip ini di komputermu.

### 1. Dapatkan Skripnya

**Opsi A: Clone Repository (Jika menggunakan Git)**

```bash
git clone [https://github.com/NAMA_USER_KAMU/NAMA_REPO_KAMU.git](https://github.com/NAMA_USER_KAMU/NAMA_REPO_KAMU.git)
cd NAMA_REPO_KAMU
```

> Ganti `NAMA_USER_KAMU` dan `NAMA_REPO_KAMU` dengan milikmu.

**Opsi B: Unduh Manual**
Unduh file `organizer.py` langsung dari repository GitHub ini.

### 2. Konfigurasi Skrip

Buka file `organizer.py` dengan teks editor favoritmu. Cari baris di bawah ini:

```python
# --- PENGATURAN ---
# GANTI DENGAN PATH LENGKAP MENUJU FOLDER YANG MAU DIRAPIKAN DI KOMPUTER KAMU!
path_folder = r'GANTI_DENGAN_PATH_FOLDER_MILIKMU' # <-- EDIT BAGIAN INI
```

Ganti nilai `r'GANTI_DENGAN_PATH_FOLDER_MILIKMU'` dengan path lengkap ke folder yang ingin kamu rapikan.

- **Contoh di Windows:** `r'C:\Users\Paino\Downloads'`
- **Contoh di macOS/Linux:** `'/Users/Paino/Downloads'`

Simpan perubahan pada file tersebut.

### 3. Jalankan Skrip

1.  Buka Terminal atau Command Prompt.
2.  Arahkan ke direktori tempat kamu menyimpan file `organizer.py`.
3.  Jalankan perintah berikut:
    ```bash
    python organizer.py
    ```

Skrip akan berjalan dan mulai memindahkan file. Kamu akan melihat status prosesnya langsung di terminal.

---

## 📋 Persyaratan

- **Python 3.x**

Tidak ada library eksternal yang perlu diinstal. Semua modul yang digunakan (`os` dan `shutil`) adalah bagian dari library standar Python.

---

## 💡 Pengembangan Selanjutnya

Merasa tertantang? Berikut beberapa ide untuk mengembangkan skrip ini lebih lanjut:

- [ ] Membuat antarmuka pengguna grafis (GUI) menggunakan `Tkinter` atau `PyQt`.
- [ ] Menambahkan fungsionalitas untuk membaca path folder dari argumen command-line (`sys.argv`).
- [ ] Membuat file log untuk mencatat semua file yang dipindahkan dan kapan proses itu terjadi.
- [ ] Mengizinkan pengguna untuk mengkustomisasi kategori folder dan ekstensinya melalui file konfigurasi (misalnya `config.json`).
