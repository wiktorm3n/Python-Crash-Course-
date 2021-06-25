class Employee():
    def __init__(self,first,last,annual):
        self.first = first
        self.last = last
        self.annual = annual
    def give_raise(self,different_raise = ''):
        self.annual += 5000
        if different_raise != '':
            self.annual += different_raise
     