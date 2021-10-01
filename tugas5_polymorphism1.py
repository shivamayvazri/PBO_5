class Theropods:
    def __init__(self, nama, panggil):
        self.nama = nama
        self.panggil = panggil

    def makan(self):
        print("Aku adalah jenis dinosaurus Karnivora. Namaku", self.nama, "atau kalian bisa juga memanggilku", self.panggil)

class Sauropods:
    def __init__(self, nama, panggil):
        self.nama = nama
        self.panggil = panggil

    def makan(self):
        print("Aku adalah jenis dinosaurus Herbivora. Namaku", self.nama, "atau kalian bisa juga memanggilku", self.panggil)

dino1 = Theropods("Tyrannosaurus", "T-Rex")
dino2 = Sauropods("Brontosaurus", "Bro")
dino3 = Theropods("Velociraptor", "Raptor")

for dino in (dino1, dino2, dino3):
    print("\n")
    dino.makan()