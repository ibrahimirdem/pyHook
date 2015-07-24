import pythoncom, pyHook

def klavyeHareket(olay):
    # Buyuk "A" ve kucuk "a" disindaki butun klavye ha-
    #reketlerini onaylayip gerceklestirecektir. Yalniz
    #"A,a" harflerini dondurmeyecegi icin bu tuslara
    #bassak ta islemiyeceklerdir.
    return (olay.Ascii not in (ord('a'), ord('A')))

# hm adinda bir nesneye HookManager fonk. atiyoruz.
hm = pyHook.HookManager()
# KeyDown ile tusa basildiginda fonksiyonumuzu uy-
#uyguluyoruz.
hm.KeyDown = klavyeHareket
# Klavye olaylarini izlemeye aliyor.
hm.HookKeyboard()
# Windowsta gerceklesen olaylari izlemeye aliyor.
pythoncom.PumpMessages()


