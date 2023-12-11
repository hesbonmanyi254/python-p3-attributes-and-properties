# access.py

class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

# Define an instance of the Human class
guido = Human("Guido")

# Using getattr with guido
my_attr = "name"
attribute_value = getattr(guido, my_attr, False)
print(attribute_value)





class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        print(f"Setting age to { age }")
        self._age = age

    age = property(get_age, set_age,)