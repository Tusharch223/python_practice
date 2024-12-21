#lists1
numbers = [1, 3, 2, 4, 4, 8, 6, 8, 9, 0, 4, 1, 5, 7, 9,]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#new
print(type(numbers))
print(numbers)

#lists
numbers = [3, 5, 2, 0, 5, 1, 6, 9, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(number)

#3
numbers = [1, 0, 2, 0, 2, 8, 9, 9, 101, 10001, 1002]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(number)
print(type(number))

#2_dlist

matrix = [
    [1, 2, 3],
    [2, 1, 3],
    [3, 6, 8]
]
matrix[0][1] = 31
print(matrix[0][1])

for row in matrix:
    print(row)
    for item in row:
        print(item)
#qq
numbers = [2, 7, 2, 8, 5, 7 ,8 ,9 ,9 ,9 ,4 ,2, 1, 6 ,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#333
numbers = (1, 2, 3, 4)
print(numbers[0])
 #unpacking(also used for lists)
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)

#dictionaries
customers = {
    "name": "tushar",
    "age": 23,
    "profession": "software engineer"
}
print(customers["profession"])
#2
customers = {
    "name": "tushar",
    "age": 23,
    "profession": "software engineer"
}

print(customers.get("birthday", "default bith date 01:01:1980"))


#functions
def greet_user():
    print('hi there! ')
    print('welcome aboard')


print("start")
greet_user()
print("finish")

#parametrs
def greet_user(name):
    print(f'hi, good morning! {name} ')
    print('what would you like to have? ')


print("start")
greet_user("tushar")
greet_user("ankit")
greet_user("sonia")
greet_user("anu")
print("finish")

#2
def Class(name):
    print(f'hi everbody, {name}')
    print('how  is everybody finding this beautiful morning?, good, huh? ')


print("start")
Class("tushar")
Class("aashi")
Class("ankita")
print("bye")