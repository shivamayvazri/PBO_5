class Dinosaurus:
    def intro(self):
        print("Dahulu kala, banyak sekali jenis-jenis dinosaurus yang pernah ada di bumi.")

    def makan(self):
        print("Dinosaurus selalu dikira sebagai pemakan daging atau karnivora, tetapi faktanya tidak semua dinosaurus pemakan daging. Ada juga dinosaurus yang herbivora atau pemakan tumbuhan")

class Tyrannosaurus(Dinosaurus):
    def makan(self):
        print("Tyrannosaurus Rex atau T-Rex adalah karnivora atau dinosaurus pemakan daging.")

class Brontosaurus(Dinosaurus):
    def makan(self):
        print("Brontosaurus adalah salah satu dinosaurus pemakan tumbuhan atau herbivora.")

class Stegosaurus(Dinosaurus):
    def makan(self):
        print("Stegosaurus juga termasuk ke dalam dinosaurus pemakan tumbuhan atau herbivora.")

class Velociraptor(Dinosaurus):
    def makan(self):
        print("Velociraptor termasuk ke dalam dinosaurus pemakan daging atau karnivora seperti T-Rex.")

obj_dino = Dinosaurus()
obj_tyranno = Tyrannosaurus()
obj_bro = Brontosaurus()
obj_stego = Stegosaurus()
obj_velo = Velociraptor()

obj_dino.intro()
obj_dino.makan()

print("\n")

obj_tyranno.intro()
obj_tyranno.makan()

print("\n")

obj_bro.intro()
obj_bro.makan()

print("\n")

obj_stego.intro()
obj_stego.makan()

print("\n")

obj_velo.intro()
obj_velo.makan()