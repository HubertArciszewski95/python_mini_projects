class Chicken:

    total_eggs = 0

    @classmethod
    def display_total_eggs(cls):
        return f"You have {cls.total_eggs} eggs in chicken choop"

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return f"Chicken {self.name} lay {self.eggs} eggs"


c1 = Chicken(name="Alice", species="Green leg")
c2 = Chicken(name="Arthur", species="Black tail")

print(Chicken.display_total_eggs())  # 0

print(c1.lay_egg())  # 1
print(Chicken.display_total_eggs())  # 1

print(c2.lay_egg())  # 1
print(c2.lay_egg())  # 2
print(Chicken.display_total_eggs())  # 3
