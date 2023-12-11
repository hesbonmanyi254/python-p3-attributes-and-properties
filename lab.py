# lab.py

class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

# Create an instance of the Human class
guido = Human("Guido")

# Access attributes using getattr
my_attr = "name"
attribute_value = getattr(guido, my_attr, False)
print(attribute_value)
