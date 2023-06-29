#arbitrary argu *d = create tuple and store values in it.

def test(a,b,c,*d):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)
    
test(10,20,30, 40,50,60,70,80)    #*d = create tuple of all the values after abc.  

#arbitrary argu 8*e = create dictionary and store keys and its values.

def test(a,b,c,*d,**e):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d,"E: ",e)
    
test(10,20,30, 40,50,60,70,80,x=10,y=20,z=30)    #*d = create tuple of all the values after abc & create dictionary after abcd.  

 