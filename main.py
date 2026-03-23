###Easy

#Exercise 1

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"The user {name} is {age} years old")

#Exercise 2

num = int(input("Enter a number: "))
check = int(input("Enter another number: "))
if num % check == 0:
    print(f"{check} devides evenly into {num}.")
else:
    print("Not what we are aiming for!")


#Exercise 3

def first_and_last(lst):
    new_lst = []
    if len(lst) < 2:
        return lst
    new_lst.append(lst[0])
    new_lst.append(lst[-1])
    return new_lst

#Exercise 4

def is_inside(lst, n):
    for a in lst:
        if a == n:
            return True
    return False

