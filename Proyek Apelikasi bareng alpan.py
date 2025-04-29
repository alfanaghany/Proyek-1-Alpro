import csv
import os

DATA_FILE = 'mahasiswa.csv'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(mahasiswa_list):
    with open(DATA_FILE, mode='w', newline='') as file:
        fieldnames = ['Nama', 'NIM', 'Kelas', 'No_Telp', 'Jenis_Kelamin']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mahasiswa_list)

def tambah_data():
    nama = input("Masukkan Nama Mahasiswa: ")
    nim = input("Masukkan NIM: ")
    kelas = input("Masukkan Kelas: ")
    no_telp = input("Masukkan No. Telp: ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")

    mahasiswa = {
        'Nama': nama,
        'NIM': nim,
        'Kelas': kelas,
        'No_Telp': no_telp,
        'Jenis_Kelamin': jenis_kelamin
    }

    mahasiswa_list = load_data()
    mahasiswa_list.append(mahasiswa)
    save_data(mahasiswa_list)
    print("Data berhasil ditambahkan!\n")

def lihat_data():
    mahasiswa_list = load_data()
    if not mahasiswa_list:
        print("Data kosong.\n")
        return
    for idx, mhs in enumerate(mahasiswa_list, start=1):
        print(f"{idx}. {mhs['Nama']} - {mhs['NIM']} - {mhs['Kelas']} - {mhs['No_Telp']} - {mhs['Jenis_Kelamin']}")
        info_nim(mhs['NIM'])
    print()

def edit_data():
    mahasiswa_list = load_data()
    lihat_data()
    idx = int(input("Masukkan nomor data yang ingin diedit: ")) - 1
    if 0 <= idx < len(mahasiswa_list):
        print("Kosongkan isian jika tidak ingin mengubah field.")
        nama = input(f"Nama ({mahasiswa_list[idx]['Nama']}): ") or mahasiswa_list[idx]['Nama']
        nim = input(f"NIM ({mahasiswa_list[idx]['NIM']}): ") or mahasiswa_list[idx]['NIM']
        kelas = input(f"Kelas ({mahasiswa_list[idx]['Kelas']}): ") or mahasiswa_list[idx]['Kelas']
        no_telp = input(f"No.Telp ({mahasiswa_list[idx]['No_Telp']}): ") or mahasiswa_list[idx]['No_Telp']
        jenis_kelamin = input(f"Jenis Kelamin ({mahasiswa_list[idx]['Jenis_Kelamin']}): ") or mahasiswa_list[idx]['Jenis_Kelamin']

        mahasiswa_list[idx] = {
            'Nama': nama,
            'NIM': nim,
            'Kelas': kelas,
            'No_Telp': no_telp,
            'Jenis_Kelamin': jenis_kelamin
        }
        save_data(mahasiswa_list)
        print("Data berhasil diperbarui!\n")
    else:
        print("Nomor data tidak valid.\n")

def hapus_data():
    mahasiswa_list = load_data()
    lihat_data()
    idx = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
    if 0 <= idx < len(mahasiswa_list):
        mahasiswa_list.pop(idx)
        save_data(mahasiswa_list)
        print("Data berhasil dihapus!\n")
    else:
        print("Nomor data tidak valid.\n")

def info_nim(nim):
    try:
        if len(nim) < 12:
            raise ValueError("Panjang NIM tidak valid")

        fakultas_kode = nim[0:3]
        prodi_kode = nim[3:5]
        angkatan_kode = nim[5:7]
        nomor_urut = nim[7:]

        tahun = '20' + angkatan_kode

        fakultas_dict = {
            '707': 'Fakultas Ilmu Terapan',
            '708': 'Fakultas Teknik Elektro',
            '709': 'Fakultas Industri Kreatif',
            # Tambahkan lainnya jika perlu
        }

        prodi_dict = {
            '08': 'Teknologi Rekayasa Multimedia',
            '11': 'Teknik Informatika',
            '12': 'Sistem Informasi',
            # Tambahkan lainnya jika perlu
        }

        fakultas = fakultas_dict.get(fakultas_kode, 'Fakultas Tidak Diketahui')
        prodi = prodi_dict.get(prodi_kode, 'Prodi Tidak Diketahui')

        print(f"   -> Angkatan: {tahun}, Prodi: {prodi}, Fakultas: {fakultas}, No. Urut: {nomor_urut}")
    except Exception as e:
        print(f"   -> Informasi NIM tidak valid: {e}")


def menu():
    while True:
        print("=== Aplikasi Data Mahasiswa TELU ===")
        print("1. Lihat Data Mahasiswa")
        print("2. Tambah Data Mahasiswa")
        print("3. Edit Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")

        if choice == '1':
            lihat_data()
        elif choice == '2':
            tambah_data()
        elif choice == '3':
            edit_data()
        elif choice == '4':
            hapus_data()
        elif choice == '5':
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()
