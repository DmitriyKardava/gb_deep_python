from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def animal_action(self):
        pass


class Bird(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def animal_action(self):
        print(f"The bird {self.name} can fly")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def animal_action(self):
        print(f"The dog {self.name} can woof")


class Fish(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def animal_action(self):
        print(f"The fish {self.name} can swim")


class AnimalsFactory:

    @staticmethod
    def create_animal(animal_type, name, age):
        match animal_type:
            case "bird":
                return Bird(name, age)
            case "dog":
                return Dog(name, age)
            case "fish":
                return Fish(name, age)
            case _:
                return False


if __name__ == "__main__":
    my_dog = AnimalsFactory.create_animal("dog", "Max", 10)
    my_cat = AnimalsFactory.create_animal("cat", "Gav", 3)
    print(my_dog.animal_action())
    print(my_cat.animal_action())
