# TIM 2
# adul seher
# dina
# imron
# cecep kirian
# kamal

# record
print("Penerapan record\n")

mahasiswa = {
    "nama": "Usep gerengesng",
    "usia": 199,
    "kelas": "IF 15 D",
    "IPS": 4.90
}


print("Nama: ", mahasiswa["nama"], "\nKelas: ", mahasiswa["usia"], "\nIPS: ", mahasiswa["IPS"], "\nUsia: ", mahasiswa["usia"])

mahasiswa['usia'] = 877

print("Usia setelah ulang tahun ke-x: ", mahasiswa["usia"])

print("anjais\n\n")

# stack
# antrean di spbu
stack = []
stack.append('cecep dawegan')
stack.append('kamal barangbang')
stack.append('abdul tapas')
stack.append('dina akar')
stack.append('imron baralak')

print("antrian saat ini: ", len(stack), stack)

selesaiMengisi = stack.pop()
print('selesa mengisi: ', selesaiMengisi, '\npanjang antrian: ', len(stack), stack)

selesaiMengisi = stack.pop()
print('selesa mengisi: ', selesaiMengisi, '\npanjang antrian: ', len(stack), stack)

selesaiMengisi = stack.pop()
print('selesa mengisi: ', selesaiMengisi, '\npanjang antrian: ', len(stack), stack)

selesaiMengisi = stack.pop()
print('selesa mengisi: ', selesaiMengisi, '\npanjang antrian: ', len(stack), stack)

selesaiMengisi = stack.pop()
print('selesa mengisi: ', selesaiMengisi, '\npanjang antrian: ', len(stack), stack)

def apakah_kosong():
    return stack == []
print(apakah_kosong())