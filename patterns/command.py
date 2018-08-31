class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()


def show_1():
    print(1)


def show_2():
    print(2)


def show_3():
    print(3)


C = MacroCommand([show_1, show_2, show_3])
C()
