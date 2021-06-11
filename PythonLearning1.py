# Class Attributes, Methods, and Properties 1
class ShippingContainer:

    next_serial = 1337

    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
       
c4 = ShippingContainer("ESC", ["Electronics"])
print(c4.serial)

c5 = ShippingContainer("ESC", ["Pharmaceuticals"])
print(c5.serial)

print(ShippingContainer.next_serial)