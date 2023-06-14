class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        if isinstance(first_name, str) and len(first_name) != 0:
            self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"


    def print_house_words(self):
        print(self.house_words)

    
    def die(self):
        self.is_alive = False


character = Stark("Arya")
print(character.__dict__)
print(character.is_alive)
character.print_house_words()
character.die()
print(character.is_alive)
print(character.__doc__)
