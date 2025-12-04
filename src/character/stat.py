class stat:
    #constuctor
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def increase(self, amount: int):
        self.value += amount

    def decrease(self, amount: int):
        self.value -= amount

    def __str__(self):
        return f"{self.name}: {self.value}"

    #setter and getter
    def get_value(self):
        return self.value

    def set_value(self, value: int):
        self.value = value