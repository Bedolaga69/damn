class Human:
    age = 0
    def speak(self):
        print("привет")

    def getAge(self):
        return self.age

vova = Human
vova.arg = 10
print(type(vova))
print(vova.arg)
print(vova.getAge())
vova.speak()


