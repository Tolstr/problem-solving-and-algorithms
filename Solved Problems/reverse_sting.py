#Varian 1
mystring= "respublica"
def func():
    output=""
    for i in mystring:
        output=i+output
        print(output)
func()

#Variant 2
def with_counter():
    indexx = 0
    output = ""
    for _ in mystring:
        indexx=indexx-1
        output=output+mystring[indexx]
        #print(mystring[9])
    print(output)
with_counter()

#Variant 3

def func(mystring="respublica"):
    return mystring[::-1]
print(func(mystring))

#Variant 4

def func(mystring="respublica"):
    mystring=list(mystring)
    print(mystring)
    mystring.reverse()
    print(mystring)
print(func(mystring))

# Operating System List
systems = list(mystring)
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)

#Variant 5

def func(mystring="respublica"):
    cntr = 0
    output=[]
    indexx= 0
    total_letters=len(mystring)
    while cntr < total_letters:
        indexx = indexx-1
        cntr = cntr+1
        output.append(mystring[indexx])
    print(output)
    print("".join(output))
func()







