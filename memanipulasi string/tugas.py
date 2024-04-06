
def data(): #fungsi
    nama_karyawan =str(input('Nama Karyawan : '))
    jabatan_karyawan = ['Design', 'Programmer', 'Resource']
    print ('pilih jabatan karyawan')
    pilih_jabatan_karyawan = str(input(jabatan_karyawan).title())

    status_perkawinan = ['YA','TIDAK']
    print ('sudah menikah?')
    pilih_status_perkawinan = str(input(status_perkawinan).upper())


    if pilih_jabatan_karyawan == 'Design':
        gaji = 5000000
    elif pilih_jabatan_karyawan == 'Programmer':
        gaji = 10000000
    elif pilih_status_perkawinan == 'Resource':
        gaji = 5000000

    if pilih_status_perkawinan == 'YA':
        tunjangan = gaji * (20/100)
    else:
        tunjangan = 0

    gaji_kotor = gaji + tunjangan
    pajak = gaji_kotor * (10/100)
    gaji_pokok = gaji_kotor - pajak

    print('nama : ', nama_karyawan)
    print(f'gaji pokok : {gaji:,}')
    print(f'tunjangan : {tunjangan:,}')
    print(f'gaji kotor : {gaji_kotor:,}')
    print(f'pajak penghasilan : {pajak:,}')
    print(f'gaji bersih : {gaji_pokok:,}')

data()