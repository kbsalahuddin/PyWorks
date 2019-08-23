class Enemy:
    def __init__(self,x):
        # __init__(self,parameter1)=oop constructor
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()