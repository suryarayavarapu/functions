#addition in function
def add_1(*a):
    total=0
    for i in a:
        total=total+i
    return total
print(add_1(1,2,3,4,5))
print(add_1(10,20,30,40,50))
print(add_1(100,200,300))
print("/n")
#maximum value
def max_of(*a):
    max_value=a[0]
    for v in range(len(a)-1):
        if a[v]>a[v+1]:
            max_value=a[v]
        else:
            max_value=a[v+1]
    print("----------")
    return max_value
print(max_of(43,23,55,22,456,3,5335,34))
print(max_of(32,23,45,33,1,99,102,33))
print("-----------------")
def my_function(username, **details):#if *details is posstional arguments, it take tuples, but we given key,value 
#we need to provide **details
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("emil123", age = "25", city = "Oslo", hobby = "coding")