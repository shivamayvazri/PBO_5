class Burung:
    def intro(self):
        print("Di dunia ini ada beberapa tipe yang berbeda dari spesies burung")

    def terbang(self):
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang")

class Elang(Burung):
    def terbang(self):
        print("Elang dapat terbang")

class BurungUnta(Burung):
    def terbang(self):
        print("Burung Unta tidak dapat terbang")

obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

obj_burung.intro()
obj_burung.terbang()

print("\n")

obj_elang.intro()
obj_elang.terbang()

print("\n")

obj_burung_unta.intro()
obj_burung_unta.terbang()