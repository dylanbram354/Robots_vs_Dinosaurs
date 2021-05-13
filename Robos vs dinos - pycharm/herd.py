from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('T-Rex', 30))
        self.dinosaurs.append(Dinosaur('Raptor', 15))
        self.dinosaurs.append(Dinosaur('Triceratops', 20))