"""
This is the sample program to work with class in python.
"""
class Human:
    def __init__(self,n,o,l):
        self.name = n
        self.occupation = o
        self.language = l

    def do_work(self):
        if self.occupation == "tester":
            print (self.name,"is a tester.")
        elif self.occupation == "developer":
            print(self.name,"is a developer")
        else:
            print("Invalid occupation. Class supports only two occupations: tennis player and actor.")


    def speaks(self):
        print (self.name,"speaks ",self.language)


ritesh = Human("Ritesh Singh","developer","Hindi")
ritesh.do_work()
ritesh.speaks()

dundobundo = Human("Dundo Bundo","tester","German")
dundobundo.do_work()
dundobundo.speaks()