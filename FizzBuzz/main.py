# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz
i=100
for k in range(0,i):
    if k%3==0 and k%5==1:
        print("fizz" + k)
    if k%5==0 and k%3==1:
        print("Buzz" + k)
    if k%5==0 and k%3==0:
        print("FizzBuzz" + k)
