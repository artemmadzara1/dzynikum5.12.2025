def task_number_1(n):
    result=["Четное" if g %2==0 else "Нечетное" for g in range(0,n)]
    return result
def task_number_2(x):
    result=["FizzBuzz" if j % 15 ==0 else "Fizz" if j % 3==0 else "Buzz" if j %5==0 else j for j in x ]
    return result
def tusk_number_3(x):
    result=[numbers if numbers >10 else 0 for numbers in x]
    return result
def task_number_4(x):
    result ={j:("even" if j % 2==0 else "odd") for j in range(1,x+1)}
    return result
def task_number_5(x):
    result =[len(j) if len(j)<=5 else 5 for j in x]
    return result
def task_number_6(x):
    result=[j if j >=0 else 0 for j in x]
    return result
def task_number_7(x):
    result=[j**2 if j >0 else 0 for j in x]
    return result
def task_number_8(x):
    result =[j**2 if j % 2 ==0 else j**3 for j in x]
    return result
def task_number_9(x):
    result=["High" if j >50 else "Medium" if j >=20 and j <=50 else "Low" for j in x]
    return result

