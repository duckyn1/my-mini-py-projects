
class SoftItems:
    def __init__(self, name):
        self.name = name
    def lay(self):
        print(f"You laying on {self.name}")
    def hug(self):
        print(f"You hugging {self.name}")
    def throw(self):
        print(f"You throwing {self.name}")

class Pillow(SoftItems):
    def punch(self):
        print(f"You punching {self.name}")

class MiniPillow(Pillow):
    def sleep(self):
        print(f"You sleeping on {self.name}")

class Reverse(MiniPillow):
    def reverse(self):
        print(f"You reversing {self.name}")

mini = MiniPillow("cutie")
reverse = Reverse("venom")

mini.lay()
reverse.throw()
