#
class Animal():
    '''
    parent class that englobes main
    characters of other child classes
    '''

    def __init__(self, species, age, diet, foot, mother):
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.mother = mother
        self.childrens = []

    def set_species(self, species):
        '''
        method that defines the species
        '''
        self.species = species

    def set_age(self, age):
        '''
        method that defines age
        '''
        self.age = age

    def set_diet(self, diet):
        '''
        method that defines age
        '''
        self.diet = diet

    def set_foot(self, foot):
        '''
        method that defines the number of foot
        '''
        self.foot = foot

    def set_mother(self, mother):
        '''
        method that defines mother
        '''
        self.mother = mother

    def __str__(self):
        '''
        method that does a print of what we want to show
        '''
        return "Species: " + self.species + " - " + " Age: " + str(self.age) + " years old" + " - " + "diet: " + self.diet + " number of foot : " + str(self.foot) + " - " + "parent : " + self.mother

    def add_children(self, child):
        '''
        method that adds children into a list
        '''
        self.childrens.append(child)

    def remove_children(self, child):
        '''
        method that removes children from list
        '''
        self.childrens.remove(child)


def get_parent(child):
    '''takes child in entry and returns his mother'''
    local = globals().keys()
    for i in local:
        # Problem with is instance: to ask !,problem with function get_parent ! but idea is there
        if isinstance(i, Animal):
            if child in i.childrens:
                return i.mother


cat1 = Animal("Cat", 5, "Carnivore", 4, "Mother Cat A")
cat1.add_children("Kitten1")
cat1.add_children("Kitten2")
# print(cat1.childrens)
# print(family.mother)
# print(family.father)
# print(cat1.mother)


cat2 = Animal("Cat", 5, "Carnivore", 4, "Kitten2")
cat2.add_children("Kitten3")
cat2.add_children("Kitten4")
cat2.add_children("Kitten5")
cat2.add_children("Kitten6")
# print(cat2.childrens)
# print(cat2.get_parent)


dog1 = Animal("Dog", 10, "Carnivore", 4, "Mother Dog A")
dog1.add_children("Puppy1")
dog1.add_children("Puppy2")
dog1.add_children("Puppy3")
# print(dog1.childrens)


dog2 = Animal("Dog", 10, "Carnivore", 4, "Puppy3")
dog2.add_children("Puppy4")
dog2.add_children("Puppy5")
# print(dog2.childrens)
# print(dog2.get_parent)

dog3 = Animal("Dog", 10, "Carnivore", 4, "Puppy5")
dog3.add_children("Puppy6")
# dog3.add_children("Puppy7")
print(isinstance('cat1', Animal))
print(get_parent("Puppy5"))
