#integers and strings using list
def sequence(s):
    for l in s:
        print(l)
l1=[1,2,3,4,5,5]
sequence(l1)


l2=["ef","df","fs"]
sequence(l2)

#func dictionaries
def dict_func(t):
    for key, value in t.items():
        print(key,value)
        print(t[key])
k={1:"4er",2:"wef",3:"edf"}
dict_func(k)

#If you do not know how many arguments will be passed into your function, add a * before the parameter name.
#This way, the function will receive a tuple of arguments and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
