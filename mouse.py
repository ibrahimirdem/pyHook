# -*- coding: cp1254 -*-
import pythoncom, pyHook
# Mouse hareketi oldugunda yapılmasini
#istedigimiz olaylar icin kullanacagimiz fonks.
def mouseHareket(olay):
    # Burada mouse ile yapilan islemi mesaj olarak
    #bize veriyor. Mesela; "mouse move" mesaji fare-
    #nin hareket ettirildigi anlamina gelir.
    print 'Mesaj Adı:',olay.MessageName
    # Olayin gerceklestigi zamani verir bize.
    print 'Zaman:',olay.Time
    # Olay hangi pencere uzerinde gerceklesiyorsa
    #onun adini veriyor.
    print 'Pencere Adi:',olay.WindowName
    # Herhangi bir gerceklesen mouse olayinda fare-
    #nin konumunu veriyor.
    print 'Koordinat:',olay.Position
    print '---'

    # Diger gerceklesen eylemleri gecmek icin True
    #degerini donduruyoruz.
    return True

# hm adinda bir nesneye HookManager fonk. atiyoruz.
hm = pyHook.HookManager()
# Tum fare olaylarını kontrol etmek icin hm.MouseAll
#'i kullaniyoruz. Olusan hareketler mouseHareket fonk.
#'da islem goruyor.
hm.MouseAll = mouseHareket
# Mouse olaylarini izlemeye aliyor.
hm.HookMouse()
# Windowsta gerceklesen olaylari izlemeye aliyor.
pythoncom.PumpMessages()
