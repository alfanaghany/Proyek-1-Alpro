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

        gelar_kode = nim[0]
        fakultas_kode = nim[1:3]
        prodi_kode = nim[3:5]
        angkatan_kode = nim[5:7]
        nomor_urut = nim[7:]

        tahun = '20' + angkatan_kode

        gelar_dict = {
            '7': 'D4',
            '6': 'D3',
            '1': 'S1',
            '2': 'S2',
            '3': 'S3',
        }

        fakultas_dict = {
            '01': {
                'nama': 'Fakultas Teknik Elektro',
                'prodi': {
                    '01': 'Teknik Fisika',
                    '02': 'Teknik Telekomunikasi',
                    '03': 'Teknik Biomedis',
                    '04': 'Teknik Sistem Energi',
                    '05': 'Teknik Elektro',
                    '06': 'Teknik Komputer',
                }
            },
            '02': {
                'nama': 'Fakultas Rekayasa Industri',
                'prodi': {
                    '01': 'Sistem Informasi',
                    '02': 'Teknik Industri',
                    '03': 'Teknik Logistik',
                    '04': 'Manajemen Rekayasa',
                }
            },
            '03': {
                'nama': 'Fakultas Informatika',
                'prodi': {
                    '01': 'Teknologi Informasi',
                    '02': 'Rekayasa Perangkat Lunak',
                    '03': 'Informatika',
                    '04': 'PJJ Informatika',
                    '05': 'Sains Data',
                }
            },
            '04': {
                'nama': 'Fakultas Ekonomi Dan Bisnis',
                'prodi': {
                    '01': 'Manajemen',
                    '02': 'Akuntansi',
                    '03': 'Manajemen Bisnis Rekreasi',
                    '04': 'Administrasi Bisnis',
                    '05': 'Bisnis Digital',
                }
            },
            '05': {
                'nama': 'Fakultas Komunikasi Ilmu Sosial',
                'prodi': {
                    '01': 'Ilmu Komunikasi',
                    '02': 'Hubungan Masyarakat'
                }
            },
            '06': {
                'nama': 'Fakultas Industri Kreatif',
                'prodi': {
                    '11': 'Desain Komunikasi Visual',
                    '12': 'Desain Interior',
                }
            },
            '07': {
                'nama': 'Fakultas Ilmu Terapan',
                'prodi': {
                    '08': 'Teknologi Rekayasa Multimedia',
                    '09': 'TR Perangkat Lunak',
                    '10': 'TR Jaringan Telekomunikasi Digital',
                }
            }
        }

        gelar = gelar_dict.get(gelar_kode, 'Gelar Tidak Diketahui')
        fakultas_data = fakultas_dict.get(fakultas_kode)

        if fakultas_data:
            nama_fakultas = fakultas_data['nama']
            nama_prodi = fakultas_data['prodi'].get(prodi_kode, 'Prodi Tidak Diketahui')
        else:
            nama_fakultas = 'Fakultas Tidak Diketahui'
            nama_prodi = 'Prodi Tidak Diketahui'

        print(f"   -> Angkatan: {tahun}")
        print(f"   -> Gelar   : {gelar}")
        print(f"   -> Prodi   : {nama_prodi}")
        print(f"   -> Fakultas: {nama_fakultas}")
        print(f"   -> No. Urut: {nomor_urut}")
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
