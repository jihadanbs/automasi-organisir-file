# automasi-organisir-file

## Pengorganisir File Otomatis dengan Python 📂

Sebuah skrip Python untuk merapikan folder yang berantakan secara otomatis dengan memindahkan file ke dalam sub-folder berdasarkan kategorinya (Gambar, Dokumen, Video, dll).

Proyek ini dibuat sebagai contoh program automasi level pemula yang praktis dan mudah dipahami.

---

## ✨ Fitur

- **Interaktif**: Skrip akan menanyakan folder mana yang ingin dirapikan setiap kali dijalankan, sehingga tidak perlu mengubah kode.
- **Klasifikasi Otomatis**: Mengidentifikasi tipe file berdasarkan ekstensinya (e.g., `.jpg`, `.pdf`, `.svg`).
- **Pembuatan Folder Dinamis**: Secara otomatis membuat folder kategori (`Gambar`, `Gambar Vektor`, `Dokumen`, dll.) jika belum ada.
- **Dukungan Berbagai Tipe File**: Mengorganisir gambar, dokumen, video, musik, dan arsip. File yang tidak dikenali akan dimasukkan ke folder `Lainnya`.
- **Tanpa Dependensi Eksternal**: Hanya menggunakan library standar Python (`os` dan `shutil`), tidak perlu instalasi tambahan.

---

## 🚀 Cara Penggunaan

### 1. Dapatkan Skrip

**Opsi A: Clone Repository (Git)**

```bash
git clone [https://github.com/jihadanbs/automasi-organisir-file.git](https://github.com/jihadanbs/automasi-organisir-file.git)
cd automasi-organisir-file
```

**Opsi B: Unduh Manual**
Unduh file `organizer.py` langsung dari repository GitHub ini.

### 2. Jalankan Skrip

1.  Buka Terminal atau Command Prompt.
2.  Arahkan ke direktori tempat Anda menyimpan file `organizer.py`.
3.  Jalankan perintah berikut:
    ```bash
    python organizer.py
    ```
4.  Skrip akan bertanya. **Salin dan tempel (copy-paste) path folder** yang ingin Anda rapikan, lalu tekan **Enter**.
    ```
    📂 Masukkan path lengkap ke folder yang ingin dirapikan: C:\Users\Anda\Downloads
    ```
5.  Skrip akan berjalan dan mulai memindahkan file. Anda akan melihat status prosesnya langsung di terminal.

---

## 🗓️ Menjadwalkan Skrip Agar Berjalan Otomatis

Untuk menjalankan skrip secara otomatis (misalnya setiap hari), kita **tidak bisa menggunakan skrip interaktif**. Buat salinan dari `organizer.py` dan beri nama `organizer_scheduled.py`, lalu ubah agar path foldernya ditentukan langsung di dalam kode (non-interaktif).

**Isi `organizer_scheduled.py`:**

```python
import os
import shutil

# --- PENGATURAN UNTUK PENJADWALAN ---
# GANTI DENGAN PATH FOLDER YANG SELALU INGIN DIRAPIKAN, MISALNYA FOLDER DOWNLOADS
path_folder = r'C:\Users\Anda\Downloads' # <-- EDIT BAGIAN INI
# ------------------------------------

print(f"Menjalankan pengorganisir otomatis untuk: {path_folder}")

if not os.path.isdir(path_folder):
    print(f"Error: Folder '{path_folder}' tidak ditemukan.")
else:
    list_file = os.listdir(path_folder)
    for nama_file in list_file:
        path_sumber_file = os.path.join(path_folder, nama_file)
        if os.path.isdir(path_sumber_file):
            continue
        ekstensi = os.path.splitext(nama_file)[1].lower()
        if ekstensi == "":
            continue

        # Logika pemindahan file... (sama seperti skrip utama)
        folder_tujuan = "Lainnya"
        if ekstensi in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]: folder_tujuan = "Gambar"
        elif ekstensi in [".svg"]: folder_tujuan = "Gambar Vektor"
        elif ekstensi in [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"]: folder_tujuan = "Dokumen"
        elif ekstensi in [".mp4", ".mov", ".avi", ".mkv"]: folder_tujuan = "Video"
        elif ekstensi in [".mp3", ".wav", ".flac"]: folder_tujuan = "Musik"
        elif ekstensi in [".zip", ".rar", ".7z"]: folder_tujuan = "Arsip"

        path_tujuan_folder = os.path.join(path_folder, folder_tujuan)
        if not os.path.exists(path_tujuan_folder):
            os.makedirs(path_tujuan_folder)

        path_tujuan_file = os.path.join(path_tujuan_folder, nama_file)
        shutil.move(path_sumber_file, path_tujuan_file)

    print("Proses Selesai!")
```

Setelah Anda memiliki `organizer_scheduled.py`, ikuti langkah di bawah ini.

### Untuk Pengguna Windows (Task Scheduler)

1.  Buka **Task Scheduler** dari Start Menu.
2.  Di panel kanan, klik **Create Basic Task...**.
3.  Beri nama (misal: `Rutin Rapikan Downloads`) dan klik **Next**.
4.  Pilih pemicu, misalnya **Daily**, lalu atur waktunya (misal: jam 8 malam). Klik **Next**.
5.  Pilih **Start a program**. Klik **Next**.
6.  Di bagian **Program/script**, isi dengan **path lengkap ke `python.exe` Anda**. (Cari dengan `where python` di cmd).
7.  Di bagian **Add arguments (optional)**, isi dengan **path lengkap ke file `organizer_scheduled.py` Anda**, diapit kutip dua.
    - _Contoh Program_: `C:\Python39\python.exe`
    - _Contoh Argumen_: `"C:\Users\Jihadanbs\Documents\code\automasi-organisir-file\organizer_scheduled.py"`
8.  Klik **Next** lalu **Finish**.

### Untuk Pengguna macOS/Linux (Cron)

1.  Buka **Terminal**.
2.  Ketik `crontab -e` dan tekan Enter.
3.  Tambahkan baris baru di paling bawah dengan format: `menit jam * * * /path/ke/python /path/ke/skrip_terjadwal.py`.
    - Untuk menemukan path python, ketik `which python3` di terminal.
    - Untuk menjalankan setiap hari jam 8 malam (20:00), formatnya adalah `0 20 * * *`.
4.  **Contoh baris lengkap:**
    ```bash
    0 20 * * * /usr/bin/python3 /Users/jihadanbs/automasi-organisir-file/organizer_scheduled.py
    ```
5.  Simpan dan keluar (di editor nano: **Ctrl+O**, **Enter**, lalu **Ctrl+X**).

---

## 📋 Persyaratan

- **Python 3.x**

---

## 💡 Pengembangan Selanjutnya

Merasa tertantang? Berikut beberapa ide untuk mengembangkan skrip ini lebih lanjut:

- [ ] Membuat antarmuka pengguna grafis (GUI) menggunakan `Tkinter` atau `PyQt`.
- [ ] Membuat file log untuk mencatat semua file yang dipindahkan dan kapan proses itu terjadi.
- [ ] Mengizinkan pengguna untuk mengkustomisasi kategori folder dan ekstensinya melalui file konfigurasi eksternal (misalnya `config.json`).
