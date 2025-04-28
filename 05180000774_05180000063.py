toplam_basarisiz=0
toplam_ortalama=0
toplam_basarili=0
toplam_ustun_basarili=0
toplam_kadin=0
toplam_erkek=0
aileyle_kalan=0
evde_kalan=0
yurtta_kalan=0
basarili_aileyle_kalan=0
basarili_yurtta_kalan=0
basarili_evde_kalan=0
az_ders_az_kredi=0
yetmis_bes_uzeri_basari=0
tum_dersleri_basarili=0
bursu_ucyuzden_fazla=0
toplam_gno=0
okul_birinci_ad=""
okul_birinci_ders_sayisi=0
okul_birinci_toplam_kredi=0
okul_birinci_gno=0 #gno yu not ortalamasını belirtmek için kullandık
okul_birincisi_burs=0
max_burs=0
max_burs_ad=""
max_burs_ders_sayisi=0
max_burs_toplam_kredi=0
max_burs_gno=0
toplam_burs=0
kadin_gno=0
erkek_gno=0
krediler_toplami=0
basarisiz_ikamet=""
sayiya_gore_basarili=0
ogrenci_sayisi=int(input("ogrenci sayisini giriniz:"))
for i in range(1,ogrenci_sayisi+1):
    ogrenci_no=int(input("ogrenci no giriniz:"))
    while(ogrenci_no<1):
        ogrenci_no = int(input("lütfen uygun değer giriniz:"))
    durum=""
    ders = 0
    basarili_ders=0
    toplam_kredi=0
    toplam_carpim=0
    basarili_kredi=0
    ad=input("ad soyad bilgisi giriniz:")
    cinsiyet=input("ogrencinin cinsiyeti: kadın/erkek (k/K/e/E karakterlerini kullanınız)")
    while(cinsiyet != "k" and cinsiyet!="K" and cinsiyet!="E" and cinsiyet!="e"):
        cinsiyet =input("lütfen uygun değer giriniz:")
    if(cinsiyet=="k"or cinsiyet=="K"):
        toplam_kadin+=1
    else:
        toplam_erkek+=1
    ikamet=input("ogrenincinin ikamet yeri:ailesiyle/yurtta/evde (A/a/Y/y/E/e karakterleri)")
    while(ikamet!="A" and ikamet!="a" and ikamet!="Y" and ikamet!="y" and ikamet!="E" and ikamet!="e"):
        ikamet = input("lütfen uygun değer giriniz:")
    kredi=int(input("ders kredisini giriniz:"))
    if (ikamet == "A" or ikamet == "a"):
        aileyle_kalan += 1
    elif (ikamet == "Y" or ikamet == "y"):
        yurtta_kalan += 1
    elif (ikamet == "e" or ikamet == "E"):
        evde_kalan += 1
    while(kredi>0):
       krediler_toplami+=kredi
       toplam_kredi+=kredi
       ders+=1
       notu=int(input("dersin notunu giriniz:"))
       while(notu<0 or notu>100):
           notu = int(input("lütfen uygun değer giriniz:"))

       toplam_carpim+=notu*kredi
       if(notu>=60):
           if (ikamet == "A" or ikamet == "a"):
               basarili_aileyle_kalan += 1
           elif (ikamet == "Y" or ikamet == "y"):
               basarili_yurtta_kalan += 1
           elif(ikamet=="e" or ikamet=="E"):
               basarili_evde_kalan += 1
           basarili_ders+=1
           basarili_kredi+=kredi
       kredi=int(input("yeni dersin kredisini giriniz"))
    if (ders == basarili_ders):
        tum_dersleri_basarili += 1
    if(basarili_ders*100/ders>=75) or (basarili_kredi*100/toplam_kredi>=75):
        yetmis_bes_uzeri_basari+=1
    if(ders<3 or toplam_kredi<10):
        az_ders_az_kredi+=1
    gno=(toplam_carpim/toplam_kredi)
    toplam_gno+= gno
    if(cinsiyet=="k"or cinsiyet=="K"):
        kadin_gno+=gno
    if(cinsiyet=="e"or cinsiyet=="E"):
        erkek_gno+=gno
    if(gno<35):
        durum="basarisiz"
        toplam_basarisiz+=1
    elif(gno>=35 and gno<60):
        durum="ortalama"
        toplam_ortalama+=1
    elif(gno>=60 and gno<85):
        durum="basarili"
        toplam_basarili+=1
    elif(gno>=85):
        durum="ustun basarili"
        toplam_basarili+=1
        toplam_ustun_basarili+=1
    if(gno<35):
        burs=0
    elif (gno >= 35 and gno < 60):
        burs=100
        toplam_burs+=burs
    elif (gno >= 60 and gno < 70):
        if(ikamet=="y" or ikamet=="Y"):
            burs=140+gno*1.2+(140+gno*1.2)*0.2
        elif(ikamet=="e" or ikamet=="E"):
            burs=140+gno*1.2+(140+gno*1.2)*0.3
        else:
            burs=140+gno*1.2
    elif(gno>=70 and gno<80):
        if (ikamet == "y" or ikamet == "Y"):
            burs =170 + gno * 1.3 + (170 + gno * 1.3) * 0.2
        elif (ikamet == "e" or ikamet == "E"):
            burs=170 + gno * 1.3 + (170 + gno * 1.3) * 0.3
        else:
            burs =170 + gno * 1.3
    elif(gno>=80 and gno<90):
        if (ikamet == "y" or ikamet == "Y"):
            burs = 190 + gno * 1.5 + (190 + gno * 1.5) * 0.2
        elif (ikamet == "e" or ikamet == "E"):
            burs=190 + gno * 1.5 + (190 + gno * 1.5) * 0.3
        else:
            burs = 190 + gno * 1.5
    elif(gno>=90):
        if (ikamet == "y" or ikamet == "Y"):
            burs = 200 + gno * 1.8 + (200 + gno * 1.8) * 0.2
        elif (ikamet == "e" or ikamet == "E"):
            burs=200 + gno * 1.8 + (200 + gno * 1.8) * 0.3
        else:
            burs = 200 + gno * 1.8
    toplam_burs += burs
    if(burs>300):
        bursu_ucyuzden_fazla+=1
    if (gno > okul_birinci_gno):
        okul_birinci_gno = gno
        okul_birinci_ad = ad
        okul_birinci_ders_sayisi = ders
        okul_birinci_toplam_kredi = toplam_kredi
        okul_birincisi_burs = burs
    if(burs>max_burs):
        max_burs=burs
        max_burs_ad=ad
        max_burs_ders_sayisi=ders
        max_burs_gno=gno
        max_burs_toplam_kredi=toplam_kredi
    print("ogrenci no:",ogrenci_no," ad soyad:",ad)
    print("toplam ders sayısı:",ders," toplam kredi:",toplam_kredi)
    print("basarili oldugu ders sayisi:",basarili_ders," basarili derslerin toplam kredisi:",basarili_kredi)
    print("basarili ders sayısı yüzdesi:%", format(basarili_ders * 100 / ders,".2f"))
    print("basarili kredi sayisi yüzdesi:%",format(basarili_kredi * 100 / toplam_kredi,".2f"))
    print("agırlıklı not ortalaması:",format(gno,".2f"))
    print("basari durumu:",durum)
    print("sonraki donem alacagı aylık burs:",format(burs,".2f"))
    print("*****************************************************************************************")

if (basarili_aileyle_kalan*100/aileyle_kalan < basarili_evde_kalan*100/evde_kalan) and (basarili_aileyle_kalan*100/aileyle_kalan < basarili_yurtta_kalan*100/yurtta_kalan):
   basarisiz_ikamet = "AİLE"
elif (basarili_evde_kalan*100/evde_kalan < basarili_aileyle_kalan*100/aileyle_kalan) and (basarili_evde_kalan*100/evde_kalan < basarili_yurtta_kalan*100/yurtta_kalan):
   basarisiz_ikamet="EV"
elif(basarili_yurtta_kalan*100/yurtta_kalan < basarili_aileyle_kalan*100/aileyle_kalan)and (basarili_yurtta_kalan*100/yurtta_kalan < basarili_evde_kalan*100/evde_kalan):
   basarisiz_ikamet="YURT"

print("başarı durumlarına göre:")
print("başarısız öğrenci sayısı:",toplam_basarisiz,"yüzde:%",format(100*toplam_basarisiz/ogrenci_sayisi,".2f"))
print("ortalama öğrenci sayısı:",toplam_ortalama,"yüzde:%",format(100*toplam_ortalama/ogrenci_sayisi,".2f"))
print("başarılı öğrenci sayısı:",(toplam_basarili-toplam_ustun_basarili),"yüzde:%",format(100*(toplam_basarili-toplam_ustun_basarili)/ogrenci_sayisi,".2f"))
print("üstün başarılı öğrenci sayısı:",toplam_ustun_basarili,"yüzde:%",format(100*toplam_ustun_basarili/ogrenci_sayisi,".2f"))
print("kadınlar için ağırlıklı not ortalamalarının ortalaması:", format(kadin_gno / toplam_kadin, ".2f"))
print("erkekler için ağırlıklı not ortalamalarının ortalaması:",format(erkek_gno/toplam_erkek,".2f"))
print("tüm öğrenciler için not ortalamalarının ortalaması:",format(toplam_gno/ogrenci_sayisi,".2f"))
print("derslerin toplam kredilerin ortalaması:",format(krediler_toplami/ogrenci_sayisi,".2f"))
print("O dönem aldığı derslerin sayısı 3’ten az veya toplam kredisi 10’dan az olan öğrencilerin sayısı:",az_ders_az_kredi," yüzde:%",format(100*az_ders_az_kredi/ogrenci_sayisi,".2f"))
print("O dönem aldığı derslerin sayısına veya toplam kredisine göre başarı yüzdesi 75 ve üstünde olan öğrencilerin sayısı:",yetmis_bes_uzeri_basari, " ve yüzdesi:%",format(yetmis_bes_uzeri_basari*100/ogrenci_sayisi,".2f"))
print("Sonraki dönem alacağı burs miktarı 300 TL’den fazla olan öğrencilerin sayısı:",bursu_ucyuzden_fazla)
print("O dönem okul birincisi olan öğrencinin adı soyadı:",okul_birinci_ad,"  o dönem aldığı derslerin sayısı ve toplam kredisi:",okul_birinci_ders_sayisi,"/",okul_birinci_toplam_kredi," o dönemki ağırlıklı not ortalaması:",format(okul_birinci_gno,".2f"),"sonraki dönem alacağı aylık burs mitarı:",format(okul_birincisi_burs,".2f"))
print("Sonraki dönem en çok aylık burs alacak olan öğrencinin adı soyadı",max_burs_ad,"  o dönem aldığı derslerin sayısı ve toplam kredisi:",max_burs_ders_sayisi,"-",max_burs_toplam_kredi," o dönemki ağırlıklı not ortalaması:",format(max_burs_gno,".2f"),"sonraki dönem alacağı aylık burs mitarı:",format(max_burs,".2f"))
print("Tüm öğrencilere sonraki dönem her ay ödenecek toplam burs miktarı:",format(toplam_burs,".2f"))
print("Başarılı öğrencilerin yüzdesinin en düşük olduğu ikamet yeri:",basarisiz_ikamet)











