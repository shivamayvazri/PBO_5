class kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Meow, perkenalkan nama saya", self.nama, "umur saya", self.umur, "tahun")

class dog:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Guk..gukk.., perkenalkan nama saya", self.nama, "umur saya", self.umur, "tahun")

kucing1 = kucing("tom", 3)
dog1 = dog("spike", 3)

for hewan in (kucing1, dog1):
    hewan.bersuara()