# this is a comment 
class testclass:
    def __init__(self,_name):
        self.MyName = _name
    
    def printname(self):
        print(self.MyName)

if __name__=="__main__":
    tc = testclass("jimmy")
    tc.printname()
    k=input("press close to exit") 
    tc = None


