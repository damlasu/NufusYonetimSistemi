import sqlite3

def csvdenalma():
    kisiListe = []
    try:
        dosya = open("kisiler.csv", "r")
        for prsn in dosya:
            kisiListe.append(prsn.strip().split(";"))
        dosya.close()
    except:
        print("Dosya oluşturuldu")

    for i in kisiListe:
        imlec.execute("""INSERT INTO kisiler VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
        '{}', '{}', '{}', '{}')""".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]))

def csvkayit():
    imlec.execute("""SELECT DISTINCT * FROM kisiler""")
    kisiListe = []
    for i in imlec:
        kisiListe.append(i)
    dosya=open("kisiler.csv","w")
    kaydet=[]
    for insan in kisiListe:
        kaydet.append(";".join(insan) + "\n")
    dosya.writelines(kaydet)
    dosya.close()

def ekleme():
    kimlikno = input("Eklemek istediğiniz kişinin kimlik numarasını giriniz:")
    imlec.execute("""SELECT DISTINCT * FROM kisiler WHERE kimlikno = '{}'""".format(kimlikno))
    veri = imlec.fetchall()
    sorgu = []
    for i in veri:
        sorgu.append(i)
    if len(sorgu) == 0:
        ad = input("Eklemek istediğiniz kişinin ADINI giriniz:")
        soyad = input("Eklemek istediğiniz kişinin SOYADINI giriniz:")
        babaAdi = input("Eklemek istediğiniz kişinin BABA ADINI giriniz:")
        anneAdi = input("Eklemek istediğiniz kişinin ANNE ADINI giriniz:")
        dogumYeri = input("Eklemek istediğiniz kişinin DOGUM YERİNİ giriniz:")
        medeniDurum = input("Eklemek istediğiniz kişinin MEDENİ DURUMUNU giriniz:")
        kanGrubu = input("Eklemek istediğiniz kişinin KAN GRUBUNU giriniz:")
        kutukSehir = input("Eklemek istediğiniz kişinin KUTUK SEHRİNİ giriniz:")
        kutukIlce = input("Eklemek istediğiniz kişinin KUTUK ILCESI giriniz:")
        ikametgahSehir = input("Eklemek istediğiniz kişinin IKAMETGAH SEHRİNİ giriniz:")
        ikametgahIlce = input("Eklemek istediğiniz kişinin IKAMETGAH ILCESI giriniz:")

        imlec.execute("""INSERT INTO kisiler VALUES ('{}', '{}', '{}', '{}', '{}', 
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(kimlikno, ad, soyad, babaAdi, anneAdi,
                                                                        dogumYeri,medeniDurum, kanGrubu, kutukSehir, kutukIlce,
                                                                        ikametgahSehir, ikametgahIlce))
        print(f"{kimlikno} kimlik numaralı {ad} kisi veri tabanına eklendi.")
        db.commit()
    else:
        print("Bu kişi veri tabanında mevcut.")

def dbListele():
    print('KİMLİK NO'.ljust(10), '  ADI'.ljust(10), 'SOYADI'.ljust(10), 'BABA ADI'.ljust(10), 'ANNE ADI'.ljust(11),
          'DOGUM YERI'.ljust(11), 'MEDENI DURUM'.ljust(15), 'KAN GRUBU'.ljust(13), 'KUTUK SEHRI'.ljust(15),
          'KUTUK ILCE'.ljust(15),'IKAMETGAH SEHRİ'.ljust(20),'IKAMETGAH ILCE'.ljust(10))
    print('--------- ---------  ---------  --------- -----------  -----------  ------------   ---------- '
          '    -----------     -----------     ---------------     ---------------')
    imlec.execute("""SELECT DISTINCT * FROM kisiler""")
    for veri in imlec:
        print(veri[0].ljust(10),veri[1].ljust(10),veri[2].ljust(10),veri[3].ljust(10),veri[4].ljust(11),
              veri[5].ljust(11),veri[6].ljust(15),veri[7].ljust(13),veri[8].ljust(15),veri[9].ljust(15),
              veri[10].ljust(20),veri[11].ljust(10))

def arama():
    kimlikno=input("Bulmak istediğiniz/aradığınız kişinin kimlik numarasını giriniz:")
    imlec.execute("""SELECT DISTINCT * FROM kisiler WHERE kimlikno = '{}'""".format(kimlikno))
    veri = imlec.fetchall()
    sorgu=[]
    for i in veri:
        sorgu.append(i)
        yazdirma(i)
    if len(sorgu)==0:
        print("Aradığınız kişi veri tabanımızda bulunamadı.")
        ekle=input("Kişiyi eklemek ister misiniz?(evet/hayır)")
        if ekle.lower()=="evet":
            ekleme()
            csvkayit()

def yazdirma(arg):
    print('KİMLİK NO'.ljust(10), '  ADI'.ljust(10), 'SOYADI'.ljust(10), 'BABA ADI'.ljust(10), 'ANNE ADI'.ljust(11),
          'DOGUM YERI'.ljust(11), 'MEDENI DURUM'.ljust(15),'KAN GRUBU'.ljust(13), 'KUTUK SEHRI'.ljust(15),
          'KUTUK ILCE'.ljust(15), 'IKAMETGAH SEHRİ'.ljust(20), 'IKAMETGAH ILCE'.ljust(10))
    print('--------- ---------  ---------  --------- -----------  -----------  ------------   ---------- '
          '    -----------     -----------     ---------------     ---------------')
    print(arg[0].ljust(10), arg[1].ljust(10),arg[2].ljust(10), arg[3].ljust(10),arg[4].ljust(11),
            arg[5].ljust(11),arg[6].ljust(15), arg[7].ljust(13),arg[8].ljust(15),
            arg[9].ljust(15),arg[10].ljust(20), arg[11].ljust(10))

def guncelleme():
    kimlikno=input("Güncellemek istediğiniz kişinin kimlik numarasını giriniz:")

    set=input("Hangi bilgiyi güncelleyeceksiniz\n1.Kimlik Numarası\t2.Adı\t3.Soyadı\t4.Baba Adı\n"
              "5.Anne Adı\t6.Dogum Yeri\t7.Medeni Durum\t8.Kan Grubu\n"
              "9.Kütük Sehri\t10.Kütük İlçe\t11.İkametgah Şehir\t12.İkametgah İlçe\n->Seçiminiz::")
    if set=="1":set="KimlikNo"
    elif set == "2": set = "Adı"
    elif set == "3": set = "Soyadı"
    elif set == "4": set = "Baba_adı"
    elif set == "5": set = "Anne_adı"
    elif set == "6": set = "Doğum_yeri"
    elif set == "7": set = "Medeni_durumu"
    elif set == "8": set = "Kan_grubu"
    elif set == "9": set = "Kütük_Şehir"
    elif set == "10": set = "Kütük_İlçe"
    elif set == "11": set = "İkametgah_Şehir"
    elif set == "12": set = "İkametgahİlçe"
    komut = "UPDATE kisiler SET {} = ? WHERE kimlikno = ?".format(set)
    imlec.execute("""SELECT DISTINCT * FROM kisiler WHERE kimlikno = '{}'""".format(kimlikno))
    veri = imlec.fetchall()
    sorgu=[]
    for search in veri:
        sorgu.append(search)
    if len(sorgu) == 0:
        print("Güncellemek istediğiniz kişi veri tabanımızda bulunamadı.")
    else:
        yeniverigirisi = input(f"Yeni {set} bilgisini giriniz:")
        imlec.execute(komut,(yeniverigirisi, kimlikno))
        db.commit()
        dbListele()


def silme():
    komut = "DELETE FROM kisiler WHERE kimlikno = ?"
    kimlikno = input("Silmek istediğiniz kişinin kimlik numarasını giriniz:")
    imlec.execute("""SELECT DISTINCT * FROM kisiler WHERE kimlikno = '{}'""".format(kimlikno))
    veri = imlec.fetchall()
    sorgu = []
    for i in veri:
        sorgu.append(i)
    if len(sorgu)==0:
        print("Silmek istediğiniz kişi veri tabanımızda bulunamadı.")
    else:
        imlec.execute(komut, (kimlikno,))
        db.commit()
        print("Yeni veri tabanı;")
        dbListele()



db = sqlite3.connect('kisiler.db')
imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kisiler(KimlikNo, Adı, Soyadı, Baba_adı, Anne_adı, Doğum_yeri, Medeni_durumu, Kan_grubu,"
              "Kütük_Şehir, Kütük_İlçe, İkametgah_Şehir, İkametgahİlçe)")



imlec.execute("""SELECT DISTINCT * FROM kisiler""")
veri = imlec.fetchall()
elemansay=0
for i in veri:
    elemansay=elemansay+1
csvdenalma()
kisisayisi=db.total_changes
if elemansay==0 :
    print("Veri tabanında şu an eleman yoktur.")
    if kisisayisi!=0:
        print(f"Veri tabanında, csv dosyasından da içe aktarılan kisilerle birlike {kisisayisi} eleman vardır.")
        dbListele()
else:
    dbListele()
    if kisisayisi==0:
        print(f"Veri tabanında şu an {elemansay} eleman vardır.")
    else:
        print(f"Veri tabanında, csv dosyasından da içe aktarılan kisilerle birlike {kisisayisi} eleman vardır.")
while True:
    print("Lütfen yapmak istediğiniz işlemi seçiniz \n"
          "0. Çıkış \n"
          "1. Kişi Eklme\n"
          "2. Kişi Listeleme\n"
          "3. Kişi Arama\Sorgulama\n"
          "4. Kişi Güncelleme\n"
          "5. Kişi Silme\n")
    islev = input("Seçiminiz: ")
    if islev not in ["0", "1", "2", "3", "4", "5"]:
        print("Hatalı giriş !!!")
    elif islev == "0":
        print("Çıkış seçildi")
        db.close()
        exit(0)
    elif islev == "1":
        ekleme()
        csvkayit()
    elif islev == "2":
        dbListele()
    elif islev == "3":
        arama()
    elif islev == "4":
        guncelleme()
        csvkayit()
    elif islev == "5":
        silme()
        csvkayit()

