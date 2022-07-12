import random

# some_list = [0 for i in range(7)]
# some_list = [i * 3 for i in "hello world"]
# some_list = [ord(i) for i in "hello world"]
# some_list = [random.randint(10, 150) for i in range(20)]
# some_list_even = [i for i in some_list if i % 2 == 0]
# print(some_list_even)
# print(some_list)
#
# user_input = input().split()
# user_input = [int(i) for i in user_input]
# print(user_input)
#
# lists = [[0]*3 for i in range(10)]
# print(lists)

some_list = [(i,j) for i in "abc" for j in [1,2,3]]
print(some_list)