# -*- coding: cp1254 -*-
import pythoncom, pyHook
# Klavye hareketi oldugunda yapılmasini
#istedigimiz olaylar icin kullanacagimiz fonks.
def klavyeHareket(olay):
    # Tusa basma anindaki zamani veriyor.
    print 'Zaman:',olay.Time
    # Tusu basildiginda olayin gerceklestigi pen-
    #cere ismi
    print 'Pencere Adi:',olay.WindowName
    # Basilan tusun Ascii kodu ve chr() fonks ile
    #onun karekter olarak anlamli bir cikti veriyor.
    print 'Ascii:', olay.Ascii, chr(olay.Ascii)
    # Burada basilan tusu veriyor yalnız buyuk kucuk
    #harf duyarliligi bulunmuyor.
    print 'Tuş:', olay.Key
    # olay.Key'i ID seklinde veriyor.
    print 'TuşID:', olay.KeyID
    print '---'

    # Diger gerceklesen eylemleri gecmek icin True
    #degerini donduruyoruz.
    return True

# hm adinda bir nesneye HookManager fonk. atiyoruz.
hm = pyHook.HookManager()
# KeyDown ile tusa basildiginda fonksiyonumuzu uy-
#uyguluyoruz.
hm.KeyDown = klavyeHareket
# Klavye olaylarini izlemete aliyor.
hm.HookKeyboard()
# Windowsta gerceklesen olaylari izlemeye aliyor.
pythoncom.PumpMessages()
