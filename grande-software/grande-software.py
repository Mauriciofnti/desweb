# Observe que em Python usamos a classe "Enum" do módulo "enum" em vez de "enumeração" 
# "Enum" é um tipo de dados embutido em Python. É usado para criar um conjunto finito de constantes.
# "Enum" é uma coleção de nomes e valores simbólicos. É um atalho para enumeração e pode ser importado do módulo "enum"
# Uma das grandes vantagens de usar "enums" é que ele limita os possíveis valores 
# que você pode fornecer a um método... sem mais erros ortográficos ou problemas de maiúsculas e minúsculas
from enum import Enum

# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON 
# e evitar todas essas comparações de strings completamente
class GuitarSpec:
    def __init__(self, builder, model, typeG, backWood, topWood, numStrings):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
        self.numStrings = numStrings

    def getBuilder(self):
        return self.builder

    def getTypeG(self):
        return self.typeG

    def getModel(self):
        return self.model

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def getNumStrings(self):
        return self.numStrings

    def matches(self, otherSpec):
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model and self.model.lower() != otherSpec.getModel().lower():
            return False
        if self.typeG != otherSpec.getTypeG():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        if self.numStrings != otherSpec.getNumStrings():
            return False
        return True


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

#Cada "enum" toma o lugar de uma das propriedades de uma guitarra
class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "eletric"


# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON 
# e evitar todas essas comparações de strings completamente
class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"
#Classe Guitar
class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood, numStrings):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.numStrings = numStrings

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood

    def getNumStrings(self):
        return self.numStrings
#Classe Inventory
class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars
    
# Testando o Sistema

# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)
    
    #spec2 = GuitarSpec(Builder.MARTIN, "D-18", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("122784", 5495.95, spec2)
    #inventory.addGuitar("76531", 6295.95, Builder.MARTIN, "OM-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("70108276", 2295.95, Builder.GIBSON, "Les Paul", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("77023", 6275.95, Builder.MARTIN, "D-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
 

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.getSpec()
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:\n{guitarSpec.getBackWood().value} na traseira e laterais,\n{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()