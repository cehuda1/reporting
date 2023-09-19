def menu():
    print('\nAutomation Reporting Generator\n')
    print("1. SQL Injection                 4. IDOR (Isecure Direct Object Reference)   7. Broken Authentication")
    print("2. XSS (Site Cross Scripting)    5. HTML Injection                           8. Broken Access Control")
    print("3. RCE (Remote Code Execution)   6. Security Misconfiguration                9. XXE (XML External Entities)")
    pilihan = input("\n[+] Pilih Report: ")

    if pilihan == "1":
        content_1()
    elif pilihan == "2":
        content_2()
    elif pilihan == "3":
        content_3()
    elif pilihan == "4":
        content_4()
    elif pilihan == "5":
        content_5()
    elif pilihan == "6":
        content_6()
    elif pilihan == "7":
        content_7()
    elif pilihan == "8":
        content_8()
    elif pilihan == "9":
        content_9()
    else:
        print("Input salah")
        keluar = input("Kembali ke menu? (y/n): ")
        if keluar.lower() == "y":
            menu()
        elif keluar.lower() == "n":
            exit()
        else:
            print("Input tidak valid. Keluar.")
            exit()


def content_1():
    print("\n              ..::SQL Injection Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    loc = input('Lokasi Temuan (contoh: form/parameter): ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_1 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,
    
Saya berharap Anda dalam keadaan baik. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis pada situs web {t_domain} melalui salah satu {loc} pada website. Kerentanan ini berhubungan dengan SQL injection dan berpotensi memungkinkan penyerang untuk mendapatkan akses super admin pada sistem melalui kerentanan tersebut.

Detail Temuan Kerentanan: 
Pada saat menganalisis situs web {t_domain} , saya menemukan adanya kerentanan yang signifikan terkait dengan SQL injection pada salah satu {loc}. Melalui parameter ini, seorang penyerang dapat menyuntikkan kode SQL berbahaya. Ini dapat memungkinkan penyerang untuk mengubah perilaku kueri dan berpotensi mendapatkan akses tidak sah ke dalam sistem.
    
Dampak dan Potensi: 
Kerentanan ini, jika dieksploitasi dengan berhasil, dapat memberikan penyerang potensi akses sebagai super admin pada sistem. Hal ini berpotensi menyebabkan kerugian serius, termasuk akses yang tidak sah dan penuh terhadap sistem, data, dan fungsionalitas.
    
    
Bukti Konsep: 
Saya telah mempersiapkan bukti konsep yang sudah disaring untuk menggambarkan kerentanan ini. Saya akan menahan diri untuk tidak membagikannya langsung melalui email guna mencegah penyalahgunaan. Sebagai gantinya, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.
    
Cuplikan :
    gambar.png
    gambar.png
    gambar.png
    
Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini.
Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan yang kritis ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.
    
berikut saya lampirkan beberapa file sebagai bukti temuan.
    
Hormat Saya,
    
{sender}
{job}
Email: {email}
Telepom: {telp}\n'''

    print(content_template_1)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_1)
            print('sukses')
            break
        else:
            break


def content_2():
    print("\n              ..::XSS (Site Cross Scripting::..)")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title : ')
    telp = input('Telepon: ')
    email = input('Email: ')
    loc = input('Lokasi Temuan (contoh: form/parameter): ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_2 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Site Cross Scripting (XSS) pada situs web {t_domain} melalui salah satu {loc} di situs tersebut. Kerentanan ini berhubungan dengan injeksi skrip lintas situs (XSS) dan berpotensi memungkinkan penyerang untuk menjalankan kode skrip berbahaya pada peramban pengguna.

Detail Temuan Kerentanan:
Ketika saya menganalisis situs web {t_instansi}, saya menemukan kerentanan yang signifikan terkait dengan Site Cross Scripting (XSS) pada salah satu {loc}. Melalui {loc} ini, seorang penyerang dapat menyisipkan kode skrip yang berbahaya. Hal ini dapat memungkinkan penyerang untuk menjalankan skrip berbahaya pada peramban pengguna, yang dapat menyebabkan pengguna rentan terhadap serangan dan pengambilan informasi pribadi.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang akses untuk menjalankan kode skrip berbahaya pada peramban pengguna yang mengakses situs. Hal ini berpotensi menyebabkan kerugian serius, termasuk pencurian informasi sensitif, penyalahgunaan akun, dan potensi kerusakan pada reputasi situs web.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang sudah disaring untuk menggambarkan kerentanan ini. Saya akan menahan diri untuk tidak membagikannya langsung melalui email guna mencegah penyalahgunaan. Sebagai gantinya, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan:

    Gambar Bukti Konsep 1
    Gambar Bukti Konsep 2
    Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_2)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_2)
            print('sukses')
            break
        else:
            break


def content_3():
    print("\n              ..::RCE (Remote Code Execution) Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    loc = input("Lokasi Temuan (parameter/form)")
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_3 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Remote Code Execution (RCE) pada situs web {t_domain} melalui salah satu {loc} di situs tersebut. Kerentanan ini berhubungan dengan kemungkinan pengeksekusian kode jarak jauh yang berpotensi memungkinkan penyerang untuk mengendalikan sistem secara tidak sah.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan Remote Code Execution (RCE) pada salah satu {loc}. Melalui {loc} ini, seorang penyerang dapat menyuntikkan kode berbahaya yang, jika dieksekusi, dapat memberikan akses dan kontrol penuh ke dalam sistem. Hal ini berpotensi mengakibatkan penyalahgunaan yang serius dan pencurian data sensitif.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang kemampuan untuk menjalankan kode jarak jauh pada sistem target. Hal ini dapat menyebabkan akses yang tidak sah dan penuh ke dalam sistem, yang berpotensi mengakibatkan pencurian data, kerusakan sistem, dan risiko serius terhadap keamanan informasi.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_3)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_3)
            print('sukses')
            break
        else:
            break


def content_4():
    print("\n              ..::IDOR (Insecure Direct Object Reference)::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    loc = input('Lokasi Temuan (parameter/form): ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_4 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Insecure Direct Object Reference (IDOR) pada situs web {t_domain} melalui salah satu {loc} di situs tersebut. Kerentanan ini berhubungan dengan akses yang tidak sah terhadap objek-objek dalam sistem yang dapat dimanipulasi oleh penyerang.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan Insecure Direct Object Reference (IDOR) pada salah satu {loc}. Melalui {loc} ini, seorang penyerang dapat memanipulasi referensi objek dalam sistem dan mengakses objek-objek yang seharusnya tidak dapat diakses secara langsung. Hal ini berpotensi mengakibatkan akses yang tidak sah ke data sensitif dan operasi yang berpotensi merusak.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang kemampuan untuk mengakses objek-objek dalam sistem yang seharusnya tidak dapat diakses olehnya. Hal ini dapat menyebabkan pencurian data, penyalahgunaan objek, kerusakan sistem, dan risiko serius terhadap keamanan informasi.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_4)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_4)
            print('sukses')
            break
        else:
            break


def content_5():
    print("\n              ..::HTML Injection Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    loc = input('Lokasi Temuan (parameter/form): ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_5 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan HTML Injection pada situs web {t_domain} melalui salah satu {loc} di situs tersebut. Kerentanan ini berhubungan dengan kemampuan penyerang untuk menyisipkan kode HTML berbahaya ke dalam halaman web, yang dapat dieksekusi oleh peramban pengguna.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan HTML Injection pada salah satu {loc}. Melalui {loc} ini, seorang penyerang dapat menyisipkan kode HTML berbahaya yang, jika dieksekusi, dapat mengubah tampilan halaman web atau bahkan mencuri informasi pengguna. Hal ini berpotensi mengakibatkan risiko keamanan dan privasi yang serius.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang kemampuan untuk memanipulasi tampilan halaman web dan mengakses informasi yang seharusnya tidak dapat diakses olehnya. Hal ini dapat mengakibatkan penyalahgunaan informasi, penipuan, dan risiko terhadap pengguna situs.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_5)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_5)
            print('sukses')
            break
        else:
            break


def content_6():
    print("\n              ..::Security Misconfiguration Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    # loc = input('Lokasi Temuan (contoh: form/parameter): ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_6 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Security Misconfiguration pada situs web {t_domain}. Kerentanan ini berhubungan dengan konfigurasi sistem yang tidak tepat yang dapat memungkinkan penyerang untuk mengeksploitasi celah keamanan.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan Security Misconfiguration. Kerentanan ini disebabkan oleh konfigurasi sistem yang tidak tepat, yang memungkinkan akses yang tidak sah atau potensial terhadap data dan fungsionalitas yang seharusnya terlindungi. Ini dapat menyebabkan risiko keamanan yang serius bagi sistem dan data yang disimpan.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang akses yang tidak sah ke dalam sistem atau data yang seharusnya terlindungi. Hal ini berpotensi menyebabkan pencurian data, penyalahgunaan fungsionalitas, atau kerusakan sistem yang dapat memengaruhi kinerja situs web dan keamanan informasi.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_6)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_6)
            print('sukses')
            break
        else:
            break


def content_7():
    print("\n              ..::Broken Authentication Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    # loc = input('Lokasi Temuan (contoh: form/parameter): ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_7 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Broken Authentication pada situs web {t_domain}. Kerentanan ini berhubungan dengan masalah autentikasi yang tidak aman yang dapat memungkinkan penyerang untuk mendapatkan akses yang tidak sah ke dalam sistem.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan Broken Authentication. Kerentanan ini dapat memungkinkan penyerang untuk mencoba teknik autentikasi yang tidak sah atau memanipulasi mekanisme autentikasi yang ada untuk mendapatkan akses yang tidak sah. Hal ini berpotensi menyebabkan penyalahgunaan akun, pencurian data, dan risiko keamanan yang serius.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang kemampuan untuk mendapatkan akses yang tidak sah ke dalam sistem atau akun pengguna. Hal ini dapat mengakibatkan pencurian data sensitif, penyalahgunaan akun, atau akses yang tidak sah ke informasi penting dalam sistem.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_7)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_7)
            print('sukses')
            break
        else:
            break


def content_8():
    print("\n              ..::Broken Access Control Report::..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    loc = input('Lokasi Temuan (contoh: form/parameter): ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_8 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan Broken Access Control pada situs web {t_domain}. Kerentanan ini berhubungan dengan masalah kontrol akses yang dapat memungkinkan penyerang untuk mengakses sumber daya yang seharusnya tidak dapat diakses olehnya.

Detail Temuan Kerentanan:
Saat saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan Broken Access Control. Kerentanan ini terkait dengan salah satu {loc} yang memungkinkan akses yang tidak sah ke sumber daya yang seharusnya terbatas. Hal ini berpotensi mengakibatkan penyalahgunaan, akses ilegal, dan potensi kerusakan terhadap data atau operasi sistem.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang akses yang tidak sah ke sumber daya yang seharusnya hanya dapat diakses oleh entitas yang sah. Hal ini dapat mengakibatkan pencurian data, modifikasi yang tidak sah, dan risiko serius terhadap keamanan informasi.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''
    print(content_template_8)
    print('----------------------------------------------------------------------------------------\n')

    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_8)
            print('sukses')
            break
        else:
            break


def content_9():
    print("\n              ..::XXE (XML External Entities):..")
    t_instansi = input('Nama Perusahaan: ')
    t_domain = input('Domain: ')
    sender = input('Nama Pengirim: ')
    job = input('Title/Posisi: ')
    email = input('Email: ')
    loc = input('Lokasi Temuan (contoh: form/parameter): ')
    telp = input('Telepon: ')
    print('----------------------------------------------------------------------------------------\n')
    content_template_9 = f'''Halo Tim Keamanan {t_instansi} yang Terhormat,

Saya berharap semuanya baik-baik saja. Saya ingin memberitahukan temuan kerentanan keamanan yang kritis terkait dengan XML External Entities (XXE) pada situs web {t_domain} melalui salah satu {loc} di situs tersebut. Kerentanan ini berhubungan dengan potensi pengepakan entity XML eksternal yang dapat dimanfaatkan oleh penyerang.

Detail Temuan Kerentanan:
Ketika saya menganalisis situs web {t_domain}, saya menemukan kerentanan yang signifikan terkait dengan XML External Entities (XXE) pada salah satu {loc}. Melalui {loc} ini, seorang penyerang dapat memanipulasi entity XML eksternal yang, jika dieksploitasi, dapat menghasilkan akses yang tidak sah dan memungkinkan penyerang untuk membaca, mengubah, atau menghapus data sensitif.

Dampak dan Potensi:
Kerentanan ini, jika berhasil dieksploitasi, dapat memberikan penyerang kemampuan untuk memanipulasi XML eksternal yang digunakan oleh sistem. Hal ini dapat menyebabkan akses yang tidak sah ke dalam sistem, pencurian data sensitif, kerusakan sistem, dan risiko serius terhadap keamanan informasi.

Bukti Konsep:
Saya telah menyiapkan bukti konsep yang telah difilter untuk menggambarkan kerentanan ini. Saya akan menahan diri dari berbagi bukti tersebut melalui email guna mencegah potensi penyalahgunaan. Sebagai alternatif, saya menyarankan kita untuk menjadwalkan panggilan atau pertemuan di mana saya dapat mendemonstrasikan kerentanan ini secara bertanggung jawab.

Cuplikan Bukti Konsep:
- Gambar Bukti Konsep 1
- Gambar Bukti Konsep 2
- Gambar Bukti Konsep 3

Tolong beri tahu saya waktu yang cocok bagi Anda, dan saya akan dengan senang hati memberikan informasi lebih lanjut serta membantu dalam menangani masalah ini. Terima kasih atas perhatian Anda terhadap masalah ini. Saya siap mendukung tim Anda dalam menyelesaikan masalah keamanan ini. Jika Anda memerlukan informasi tambahan atau bantuan, jangan ragu untuk menghubungi saya.

Hormat Saya,

{sender}
{job}
Email: {email}
Telepon: {telp}\n'''

    print(content_template_9)
    print('----------------------------------------------------------------------------------------\n')
    while True:
        pilihan = input("Apakah ingin menyimpan file? (y/n): ")
        if pilihan == 'y':
            nama_file = input("Nama File: ")
            with open(nama_file, 'w') as file:
                file.write(content_template_9)
            print('sukses')
            break
        else:
            break


menu()
