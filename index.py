# > Inputs
x = input("Enter a number: ") 
y = str(x[::-1]) 

# > condiciones 
if x == y: 
    print("\"x\" is inversely equal to \"x\"") 
    print(x + " == " + y) 
elif not x.isnumeric(): 
    print("That not are number bro :( [...]") 
else: 
    print("\"Y\" is not inversely equal to \"X\"") 
    print(x + " != " + y)
