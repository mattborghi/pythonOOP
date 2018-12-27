from person import Person
# adding inheritance
class Manager(Person):
    # Bonus to managers everytime they have a rise
    def giveRaise(self,percent,bonus=0.1):
        Person.giveRaise (self, percent+bonus)
    # initialize the manager from the employee
    # and let the class handle the job type
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    before = tom.pay
    tom.giveRaise(0.1)
    print('Using aumentating method:')
    print( 'Salary increased by %0.0f %%' % ((tom.pay/before -1)*100) )
