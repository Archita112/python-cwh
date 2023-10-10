# making of the list
# number_list = [1, 6, 4, 8, 2, 10]

# using reverse method
# number_list.reverse()
# print(number_list)

#using sort method
# number_list.sort()
# print(number_list)

# Write a program to store seven fruits in a list entered by the user.
# f1 = input("Enter fruit number 1:")
# f2 = input("Enter fruit number 2:")
# f3 = input("Enter fruit number 3:")

# fruit_basket = [f1, f2, f3]
# print(fruit_basket)

# Write a program to accept the marks of 6 students and display them in a sorted manner.
# s1 = input("Enter your marks student 1:")
# s2 = input("Enter your marks student 2:")
# s3 = input("Enter your marks student 3:")
# s4 = input("Enter your marks student 4:")
# s5 = input("Enter your marks student 5:")
# s6 = input("Enter your marks student 6:")

# marks_of_students = [s1, s2, s3, s4, s5, s6]
# marks_of_students.sort()
# print(marks_of_students)

# Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)
# a.count('0')
# print(a.count(0))

# Write a program to sum a list with 4 numbers.
# sum_list = [1, 2, 4, 5]
# n = len(sum_list)
# sum_of_sum_list = sum_list[0] + sum_list[1] + sum_list[2] + sum_list[3]
# print(sum_of_sum_list)

# Check that a tuple cannot be changed in Python.
b = (2, 3, 4, 5, 6)
# b.append(10)
print(b)
new_tuple = b + (8,)
print(new_tuple)