import random

if __name__ == "__main__":
    for i in range(10):
        print(random.randrange(1, 10), end=" ")

test_list = [n for n in range(5)]
print(f"\n{test_list}")
test_list = [random.random() for i in test_list]
print(f"\n{test_list}")
