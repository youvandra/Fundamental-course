pesan = "Halo Dunia"
nama = "Youvandra Febrial"
usia = 17

print (pesan)
print ("Nama saya", nama)
print ("Umur saya", usia)

if usia < 17:
    print("Belum punya ktp yaa?")
elif usia >= 17 & usia <= 20:
    print ("Semangat belajar dan cari kerja")
elif usia >=21:
    print("Sibuk cari kerja sama cari calon suami")

for i in range(0,3):
    print("Saya tegaskan nama saya", nama)

tahun = 2018
while usia > 0:
    print("Saat usiaku", usia ,"tahun, itu pada Tahun", tahun)
    tahun = tahun - 1
    usia = usia - 1

daftar_nama = ('arab','youvan','pandra','sikasep')
print(daftar_nama)

for dn in daftar_nama:
    print("Nama panggilan saya", dn, "Nama asli saya", nama)