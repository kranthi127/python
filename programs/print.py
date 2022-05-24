print("my frist python program")

# to input the string we use input keyword
n=input('enter the n value')
print(n)
#multiple inputs at single time 
cash,pin=input('enter cash and then pin').split(',')
print(cash,pin)
#to print in the fromatted format
print('cash{} pin{}'.format(cash,pin))
#printing formats 
print('kranthi is good boy ',sep="@" ,end='\n')
print('hi')
#to get the type of the input variable we type
m=100
print(type(m))
#always the varable received from the input is string we need to convert required type
n=int(input("entet the value"))
print(type(n))


