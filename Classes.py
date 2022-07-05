"""import math

class Person():
    name = 'Jhon'
    age = 18
    height = 176

    def Say_Hello(self):
        print('Hello')

    def Show_Data(self):
        print(self.name, self.age, self.height)

    def Say_Hello_To(self, name):
        print(f'Hello, {name}!')


a = Person()
a.name = "Tim"

b = Person()
b.name = 'Tom'

c = Person()

a.Show_Data()
b.Show_Data()
c.Show_Data()

class Triangle():
    def __init__(self, x=20, y=20, z=20):
        self.a = x
        self.b = y
        self.c = z

        self.P = self.a + self.b + self.c
        self.name = 'First'
        self.p = self.P/2

    def Count_P(self):
        print(f'P = {self.P}')
    def Count_S(self):
        print(f'S = {self.p*math.sqrt((self.p - self.a)*(self.p - self.b)*(self.p - self.c))}')


t1 = Triangle()
t1.Count_P()
t1.Count_S()

t2 = Triangle(z=10)
t2.Count_P()
t2.Count_S()

t3 = Triangle(10,10,10)
t3.Count_P()
t3.Count_S()
"""

class Car:
    def __init__(self, V_dvig, H_power, weight):
        self.weight = weight
        self.V_dvig = V_dvig
        self.H_powe = H_power

    def Print_Data(self):
        print(f"W: {self.weight}, HP: {self.H_powe}, VD: {self.V_dvig}")

class Truck(Car):
    def __init__(self, V_dvig, H_power, weight, Gruz):
        super().__init__(V_dvig,H_power,weight)
        self.gruz = Gruz

    def Print_Data(self):
        print(f"W: {self.weight}, HP: {self.H_powe}, VD: {self.V_dvig}, Gruz: {self.gruz}")



car1 = Car(2, 215, 2000)
car1.Print_Data()

Truck1 = Truck(8, 300, 5000, 4000)
Truck1.Print_Data()