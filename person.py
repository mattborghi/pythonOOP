
class Person:
    # self refers to the newly created instance object
    def __init__(self,name,age,pay=0,job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    # Adding behavior
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)


# Run this part of the code only when the file is run as a script not when it's imported
if __name__ == '__main__':
    pass
    # print(bob.name,sue.pay)
    # print(bob.name.split()[-1])
    # sue.pay*=1.10
    # print(sue.pay)
    # print('The last name of Bob is: ' + bob.lastName())
