from Animal import Animal
import os

class Model():
    def __init__(self, filename):
        self.filename = filename
        self.file=open(self.filename, "r+")
        self.dico_animaux = {}

    def read_file(self):
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a

    def save(self, dict_animal):
        self.file.write("\n"+dict_animal["species"]+","+dict_animal["age"]+","+dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"])



    def delete_animal(self,Value):
        with open("a.txt") as f:
            with open("out.txt", "w") as f1:
                for line in f:
                    if Value not in line:
                        f1.write(line)
        os.replace("out.txt" ,self.filename)


    def close(self):
        self.file.close()

    def get_attributes(self)->[]:
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def get_names(self) -> []:
        last = []
        #get last key of the dict no matter what is it
        last_key = list(self.dico_animaux.keys())[-1]
        for key in self.dico_animaux:
            last.append(key)
        return last

    def edit_animal(self,value):
        with open("a.txt") as f:
            for line in f:
                if value in line:
                    line = line.strip()
                    tab = line.split(",")
                    return tab

    def update_animal(self,dict_animal,Value):
        val = ""
        with open("a.txt") as f:
            with open("new.txt", "w") as f1:
                for line in f:
                    if Value in line:
                        for keys in dict_animal :
                            val = val + dict_animal[keys] + ","
                        val = val[0:-1] + "\n  "
                        f1.write(val)
                    else:
                        f1.write(line)
        os.replace("new.txt",self.filename)
















if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()