class A:
   def  __init__(self, attr):
        self.attr = attr
        
        
class B(A):
    def f(self):
        return self.attr
    
    
print(B("test").f())
