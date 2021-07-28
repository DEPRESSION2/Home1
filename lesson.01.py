# class Rectangle:
# 	length = 1
# 	height = 1

# 	def square(self):
# 		return self.length * self.height


# rect = Rectangle()
# rect.length = 3
# rect.height = 8

# rect1 = Rectangle()

# print(rect.square())
# print(rect1.square())

# class Student:
# 	def __init__(self, name):
# 		self.name = name


# 	def greeting(self):
# 		print(f"Hi! I am {self.name}")

# st1 = Student('Anna')
# st2 = Student('Oleg')

# st1.greeting()
# st2.greeting()




# class Parent:
# 	name = 'Ivanivanova'

# 	def greeting(self):
# 		print(f'Hi! I am {self.name} and I am {self.__class__.__name__}')


# class Child(Parent):
# 	pass


# 	def greeting(self):
# 		super().greeting()
# 		print("Dich")



# par = Parent()
# par.greeting()
# child = Child()
# print(Child.name)
# child.greeting()

class Element:
        

	def agg_state(self, t):
		if temp < self.melting:
			return("замерзание")
		elif temp >= self.evaporation:
			return("испарение")
		else:
			return("плавление")

	def convert(self, t, te):
		if te == 'C':
			return t
		elif te == 'F':
			return t * 9 / 5 + 32
		elif te == 'K':

			return t + 273

class Iron(Element):
	melting = 1538         
	evaporation = 2862





iron = Iron()
temp = int(input("Введите данные: "))
te = input("Введите шкалу температуры (C, F, K): ")
t = iron.convert(temp, te)
print(iron.agg_state(temp))











		


		













