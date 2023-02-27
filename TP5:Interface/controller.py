from vue import Application
from model import Model

class Controller() :
    def __init__(self):

        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)

        self.view.view_window()

    def display(self, value):
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        self.model.save(dict_animal)

    def delete_animal(self,Value):
        self.model.delete_animal(Value)

    def get_model_entries(self):
        return self.model.get_attributes()

    def get_last_attr(self):
        return self.model.get_names()

    def edit_animal(self,value):
        return self.model.edit_animal(value)

    def update_animal(self,dict_animal,Value):
        self.model.update_animal(dict_animal,Value)


    def quit_window(self):
        print("App closed")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()