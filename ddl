class   person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show(self,end="\n"):
            person.show(self,end)
            print(self.name,self.age,self.gender)
    def display(self):
        print(self.name,self.age,self.gender)

class student(person):
    pass

s=student("sachin",20,"male")
s.show()
