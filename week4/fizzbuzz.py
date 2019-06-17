

class Fizzbuzzer:

    def __init__(self, start=0):
        self.number = int(start)

    def next(self):
        self.number += 1
        if self.number % 15 == 0:
            return "fizzbuzz"
        elif self.number % 5 == 0:
            return "buzz"
        elif self.number % 3 == 0:
            return "fizz"
        else:   
            return self.number

buzzer = Fizzbuzzer(11)
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
