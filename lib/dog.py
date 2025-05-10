APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name  # Uses name setter
        self.breed = breed  # Uses breed setter

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1-25 chars"""
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(name) <= 25):
            raise ValueError("Name must be between 1 and 25 characters.")
        self._name = name

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, breed, raise_exception=True):
        if breed not in APPROVED_BREEDS:
            if raise_exception:
                raise ValueError("Breed must be in list of approved breeds.")
            else:
                print("Breed must be in list of approved breeds.")
            self._breed = None
        else:
            self._breed = breed