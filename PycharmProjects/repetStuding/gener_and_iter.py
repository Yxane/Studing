# gen_expr = (i**2 for i in range(10))
# for i in gen_expr:
#     print(i)
# def genf():
#     s = 1
#     for i in [123, 321, 54]:
#         yield i
#         print(s)
#         s += 1
# # s = genf()
# # print(next(s))
# for i in genf():
#     print(i)
def fact(n):
    pr = 1
    for i in range(1,n+1):
        pr = pr*i
        yield pr

if __name__ == '__main__':
    for i in fact(10):
        print(i, end = " ")