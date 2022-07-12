some_list = [1, -2, 3, -5, -4]
abs_with_some_list = list(map(abs, some_list))
print(abs_with_some_list)
string_list = ["asdsada", "sdsa", "hi"]
string_list = list(map(lambda x: x[::-1],string_list))
user_input = list(map(int, input().split()))
print(user_input)

