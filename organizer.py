import os
import shutil

print("Program Pengorganisir File Dimulai...")

# mengambil path folder yang file nya berantakan
path_folder = input("📂 Masukkan path lengkap ke folder yang ingin dirapikan: ")

# os.listdir() akan memberikan daftar semua nama file dan folder di dalam path_folder
list_file = os.listdir(path_folder)

# Cek apakah path yang diberikan valid
if not os.path.isdir(path_folder):
    print(
        f"Error: Folder '{path_folder}' tidak ditemukan. Mohon periksa kembali path-nya."
    )
else:
    # os.listdir() akan memberikan kita daftar semua nama file dan folder di dalam path_folder
    list_file = os.listdir(path_folder)

    # Loop untuk setiap nama file di dalam daftar
    for nama_file in list_file:
        # Buat path lengkap dari file sumber
        path_sumber_file = os.path.join(path_folder, nama_file)

        # Lewati jika item adalah sebuah folder, bukan file
        if os.path.isdir(path_sumber_file):
            continue

        # os.path.splitext() memisahkan nama dan ekstensi -> ('gambar_liburan', '.jpg')
        # Ambil bagian kedua [1] dan ubah ke huruf kecil .lower()
        ekstensi = os.path.splitext(nama_file)[1].lower()

        # Lewati jika tidak ada ekstensi (ini biasanya folder)
        if ekstensi == "":
            continue

        # Tentukan folder tujuan berdasarkan ekstensi
        folder_tujuan = ""
        if ekstensi in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
            folder_tujuan = "Gambar"
        elif ekstensi in [".svg"]:
            folder_tujuan = "Gambar Vektor"
        elif ekstensi in [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"]:
            folder_tujuan = "Dokumen"
        elif ekstensi in [".mp4", ".mov", ".avi", ".mkv"]:
            folder_tujuan = "Video"
        elif ekstensi in [".mp3", ".wav", ".flac"]:
            folder_tujuan = "Musik"
        elif ekstensi in [".zip", ".rar", ".7z"]:
            folder_tujuan = "Arsip"
        else:
            folder_tujuan = "Lainnya"

        # os.path.join() menggabungkan path secara cerdas
        # Buat path lengkap untuk folder tujuan
        path_tujuan_folder = os.path.join(path_folder, folder_tujuan)
        if not os.path.exists(path_tujuan_folder):
            os.makedirs(path_tujuan_folder)
            print(f"Folder '{folder_tujuan}' dibuat.")

        # Pindahkan file
        path_tujuan_file = os.path.join(path_tujuan_folder, nama_file)
        shutil.move(path_sumber_file, path_tujuan_file)
        print(f"Memindahkan '{nama_file}' ke folder '{folder_tujuan}'.")

    print("\nProses Selesai! Folder sudah rapi.")
