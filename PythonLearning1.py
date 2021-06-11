# Class Attributes, Methods, and Properties 1
class ShippingContainer:
    # ATTRIBUTE
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # We have to "call" the class by name or we will get local variable error
        self.serial = ShippingContainer.next_serial # self.serial = self.next_serial (Avoid this - not as clear)
        ShippingContainer.next_serial += 1

c4 = ShippingContainer("ESC", ["Electronics"])
print(c4.serial)

c5 = ShippingContainer("ESC", ["Pharmaceuticals"])
print(c5.serial)