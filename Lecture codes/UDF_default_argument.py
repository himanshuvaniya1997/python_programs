#without default argument.
def test(a,b,c,d):
    print("without default argu: ","A: ",a,"B: ",b,"C: ",c,"D: ",d)
    
test(10, 20, 30, 40)    
    
    
#with default arguments.
#1
def test(a,b,c,d=10):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)
    
test(10, 20, 30, 40)
test(10,20,30)      

#2
def test(a,b,c=20,d=10):   #default argu always right to left possible.
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)
    
test(10, 20, 30, 40)
test(10,20,30) 
test(10,20)  

#gives default argu in b and d at a fun call time.

def test(a=40,b=30,c=20,d=10):   
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)
    
test(b=100,d=200)   #its keyword arguments.














