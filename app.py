# this is a comment 
class testclass:
    def __init__(self,_name):
        self.MyName = _name
    
    def printname(self):
        print(self.MyName)
    
    def getname(self):
        return self.MyName

if __name__=="__main__":
    tc = testclass("jimmy")
    print("class name is %",tc.getname())
    k=input("press close to exit") 
    tc = None


