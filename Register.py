class Register:
    def __init__(self, name, value=0):
        self.name = name # Registername
        self.value = value # Register(start)wert

    @property
    def text(self):
        return self.name + ": " + hex(self.value)