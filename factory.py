class Animal:
    def speak(self):
        pass

class dog(Animal):
    def speak(self):
        print("hav hav")

class cat(Animal):
    def speak(self):
        print("Miyav")

class sheap(Animal):
    def speak(self):
        print("Mee")

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return dog()
        elif animal_type == "cat":
            return cat()
        elif animal_type == "sheap":
            return sheap()
        else:
            print("Bilinmeyen hayvan türü.")

animal = AnimalFactory.create("dog")
animal.speak()
other_animal = AnimalFactory.create("Cow")

"""
Hayvan nesnesi oluşturma kararını ve 
işlemini ayrı bir yapıya taşıyarak nesne oluşturmayı merkezi hale getirdim
"""