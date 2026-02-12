def greet():
    print("hello world")
print(greet())#greet execute then print prints the return value of greet
greet()


def hello():
    print("hi")
    return 1
hello()
print(hello())# here return availbel inside the function

print("-------------")
#function set to another variable
def hello():
    print("hi")
    return 1
msg=hello()
print(msg)
print("-------------")
#inside return statement can also string
def hello():
    return "hell0"#follow strin rules i.e., dont miss the quotes for string
msg=hello()
print(msg)



def add_of_2(a,b):
    sum =a + b
    return sum
addition= add_of_2(2,3)
print(addition)

def full_name(name):
    complete_name=name+" Rayavarapu"
    print(name,"kiran")
    return complete_name
print(full_name("surya"))