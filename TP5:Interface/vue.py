from tkinter import *



class Application(Tk):
    def __init__(self, controller):
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.last_attribute = self.controller.get_last_attr()
        self.creer_widgets()

    def creer_widgets(self):
        self.list = Label(self, text="A list of animals")
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add", command=self.add_animal)
        self.bouton_delete_animal = Button(self,text="Delete",command=self.delete_animal)



        self.listbox = Listbox(self, bg="grey")

        list_of_the_names = self.controller.get_last_attr()

        for x in list_of_the_names :
            self.listbox.insert(1,x)


        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        self.bouton_edit_animal = Button(self,text = "Edit",command=self.edit_animal)
        self.bouton_update = Button(self,text = "Update",command=self.update_info)


        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.list.pack()


        self.listbox.pack()
        self.bouton_delete_animal.pack()
        self.bouton_edit_animal.pack()
        self.bouton_update.pack()
        self.bouton.pack()

    def quit_window(self):
        self.controller.quit_window()

    def display_something(self):
        self.controller.display(self.search.get())

    def display_label(self, value):
        self.label1['text'] = value

    def update_info(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        for x in self.listbox.curselection():
            Value = self.listbox.get(x)
        self.controller.update_animal(dict_animal,Value)

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        self.controller.add_animal(dict_animal)

    def delete_animal(self):
       for x in self.listbox.curselection():
            Value = self.listbox.get(x)
       self.controller.delete_animal(Value)

    def edit_animal(self):
        for x in self.listbox.curselection():
            value = self.listbox.get(x)
            L = self.controller.edit_animal(value)
        var = len(self.attributes)
        for i in range(0,var):
            self.entries[self.attributes[i]].insert(0, L[i])

    def view_window(self):
        self.title("Ma Première App :-)")
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.view_window()