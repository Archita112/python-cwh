# basic calculator using python

class Calculator:
    def add_numbers(self, x, y):
        return x+y
    
    def substract_numbers(self, x, y):
        return x-y
    
    def multiply_numbers(self, x, y):
        return x*y
    
    def dividing_numbers(self, x, y):
        return x/y
    
calc = Calculator()

result_1 = calc.add_numbers(2, 3)
print(result_1)

result_2 = calc.dividing_numbers(2, 2)
print(result_2)

result_3 = calc.multiply_numbers(2, 3)
print(result_3)

result_4 = calc.substract_numbers(2, 2)
print(result_4)