x= input('please enter a number')
any_float=type(41.0)
any_string=type('a')
if type(x)==any_float or type(x)==any_string:
    x=float(x)
    x=int(x)
total_odd = 0
total_even = 0
for i in range(1,x+1,2):
    total_odd+= i

for i in range(0,x+1,2):
    total_even+=i
average_even=total_even/(x)
    
print('total odd=', total_odd)
print('average of even numbers=', average_even)

