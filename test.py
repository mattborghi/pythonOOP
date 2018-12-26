
class Person:
    def __init__(self,name,age,pay=0,job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

class Manager(Person):
    # Bonus to managers everytime they have a rise
    def giveRaise(self,percent,bonus=0.1):
        self.pay *= (1.0+percent+bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith',42,30000,'software')
    sue = Person('Sue Jone',45,40000,'hardware')
    #
    # print(bob.name,sue.pay)
    # print(bob.name.split()[-1])
    # sue.pay*=1.10
    # print(sue.pay)
    print('The last name of Bob is: ' + bob.lastName())
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    tom.giveRaise(.20)
    print(tom.pay)
