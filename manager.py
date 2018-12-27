from person import Person
# adding inheritance
class Manager(Person):
    # Bonus to managers everytime they have a rise
    def giveRaise(self,percent,bonus=0.1):
        self.pay *= (1.0+percent+bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith',42,30000,'software')
    sue = Person('Sue Jone',45,40000,'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    db = [bob, sue, tom]

    # give a 10% raise to all of the employees in the db
    for elem in db:
        # Clear example of polymorphism. The manager gets a 10% + 10%. Instead of just 10%
        print('BEFORE:' + elem.lastName() + '-> %0.0f' % elem.pay)
        before = elem.pay
        elem.giveRaise(0.1)
        print('AFTER:' + elem.lastName() + '-> %0.0f' % elem.pay)
        print('DIFF: %0.0f%%' % ((elem.pay/before - 1.0) * 100) )
