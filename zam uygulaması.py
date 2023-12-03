#çalışanların maaşı 3000Tl'den  yüksek olan %10 zam, maaşı 3000Tl'den düşük 
#olanlara %20 zam yapma uygulaması

maaslar = [1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x*10/100 + x)
def maas_alt(x):
    print(x*20/100 + x)
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)