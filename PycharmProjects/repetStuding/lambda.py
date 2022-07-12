r = lambda x: x ** 2
t = lambda x: "positive" if x > 0 else "negative"
#triangle_perimetr = lambda a, b, c: a + b + c
some_list = [123, 321, 543, 123, 765, 86, 324, 87, 54, 236, 987]
some_list.sort(key=lambda x: x % 10)
print(some_list)
