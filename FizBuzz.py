
for i in range(101):
    if i==0:
        continue
    elif i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else: 
        print(i)


for j in range(100):
    i=j+1
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else: 
        print(i)