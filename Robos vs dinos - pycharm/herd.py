from dinosaur import Dinosaur
import random

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('T-Rex', 30))
        self.dinosaurs.append(Dinosaur('Raptor', 15))
        self.dinosaurs.append(Dinosaur('Triceratops', 20))

    def create_herd_custom_amount(self, amount):
        self.dinosaurs = []
        i = 1
        while i <= amount:
            self.dinosaurs.append(Dinosaur(f'Dinosaur {i}', random.randint(15, 35)))
            i += 1
