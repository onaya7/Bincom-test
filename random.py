# BINARY GEN TO DECIMAL
from random import randint

class Binary:
    def generator(self):
        numbers = []
        for i in range(4):
            numbers.append(str(randint(0, 1)))
        return "".join(numbers)

    def clean_binary(self, binary):
        val = ""
        for idx, i in enumerate(binary):
            if i == "0":
                pass
            elif i == "1":
                val = binary[idx:]
                break
        return val

    def convert_binary(self, binary):
        cleaned = self.clean_binary(binary)
        decimal = 0
        for val in cleaned:
            decimal = (decimal * 2) + int(val)
        return decimal

    def generate(self):
        gen = self.generator()
        return gen, self.convert_binary(gen)


binary, base10 = Binary().generate()
print(f"Binary of {base10} is {binary}")